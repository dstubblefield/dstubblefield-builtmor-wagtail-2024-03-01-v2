from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model
from django.core.exceptions import ValidationError
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.fields import StreamField

class BlogIndex(Page):
    max_count = 1
    parent_page_types = ['home.HomePage']
    subpage_types = ['blog.BlogDetail']
    template = "blog/blog_index_page.html"
    
    subtitle = models.CharField(max_length=255, blank=True)
    body = RichTextField(
        blank=True, 
        help_text="This text will appear on the blog landing page",
        features=['h2', 'h3', 'bold', 'italic', 'strikethrough', 'link', 'ol', 'ul', 'blockquote']
        )
    
    hero_image = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('hero_image'),
        FieldPanel('subtitle'),
        FieldPanel('body'),
        
    ]
    
    def get_context(self, request):
        context = super().get_context(request)
        context['blogpages'] = BlogDetail.objects.live().public().order_by('-first_published_at')
        return context
    
    class Meta:
        verbose_name = "Blog Landing Page"
        verbose_name_plural = "Blog Landing Pages"

class BlogPageTags(TaggedItemBase):
    content_object = ParentalKey(
        'blog.BlogDetail',
        related_name='tagged_items',
        on_delete=models.CASCADE,
        )

class BlogDetail(Page):
    parent_page_types = ['blog.BlogIndex']
    subpage_types = []
    template = "blog/blog_detail.html"
    
    hero_image = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    subtitle = models.CharField(max_length=255, blank=True)
    
    tags = ClusterTaggableManager(through=BlogPageTags, blank=True)
    
    


    content_panels = Page.content_panels + [
        
        FieldPanel('hero_image'),
        FieldPanel('tags'),
        FieldPanel('subtitle'),
        
        
    ]
    
    def clean(self):
        super().clean()
        
        errors = {}
        
        if 'blog' in self.title.lower():
            errors['title'] = ValidationError("The word 'Blog' in the title is not allowed")
            
        if 'blog' in self.subtitle.lower():
            errors['subtitle'] = ValidationError("The word 'Blog' in the subtitle is not allowed")
            
        if 'blog' in self.slug.lower():
            errors['slug'] = ValidationError("The word 'Blog' in the slug is not allowed")
        
        if 'post' in self.title.lower():
            errors['title'] = ValidationError("The word 'Post' in the title is not allowed")
            
        if 'post' in self.subtitle.lower():
            errors['subtitle'] = ValidationError("The word 'Post' in the subtitle is not allowed")
            
        if 'post' in self.slug.lower():
            errors['slug'] = ValidationError("The word 'Post' in the slug is not allowed")
        
        
        if errors:
            raise ValidationError(errors)
        
        
        
    

    


