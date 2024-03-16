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
from wagtail.blocks import TextBlock, StreamBlock, StructBlock, CharBlock, PageChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from blocks import blocks as custom_blocks
from django.contrib.contenttypes.fields import GenericRelation
from wagtail.admin.panels import PublishingPanel
from wagtail.models import DraftStateMixin, RevisionMixin, LockableMixin, PreviewableMixin
from wagtail.contrib.routable_page.models import RoutablePageMixin, path, re_path
from wagtail.search import index
from wagtailmarkdown.fields import MarkdownField


class Author(
        PreviewableMixin,  # Allows previews
        LockableMixin,  # Makes the model lockable
        DraftStateMixin,  # Needed for Drafts
        RevisionMixin,  # Needed for Revisions
        index.Indexed,  # Makes this searchable; don't forget to run python manage.py update_index
        models.Model
    ):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    is_contributor = models.BooleanField(default=False)
    revisions = GenericRelation("wagtailcore.Revision", related_query_name="author")

    panels = [
        FieldPanel("name"),
        FieldPanel("bio"),
        FieldPanel("is_contributor"),
        PublishingPanel(),
    ]

    search_fields = [
        index.FilterField('name'),
        index.SearchField('name'),
        index.AutocompleteField('name'),
    ]

    def __str__(self):
        return self.name

    @property
    def preview_modes(self):
        return PreviewableMixin.DEFAULT_PREVIEW_MODES + [
            ("dark_mode", "Dark Mode")
        ]

    def get_preview_template(self, request, mode_name):
        # return "includes/author.html"  # Default for a single preview template
        templates = {
            "": "includes/author.html", # Default
            "dark_mode": "includes/author_dark_mode.html"
        }
        return templates.get(mode_name, templates[""])

    def get_preview_context(self, request, mode_name):
        context = super().get_preview_context(request, mode_name)
        context['warning'] = "This is a preview"
        return context

class BlogIndex(RoutablePageMixin, Page):
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
    
    hero_image_desktop = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Image needs to be landscape 2560-w x 1400-h pixels.",
        related_name='+'
    )
    hero_image_mobile = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Image needs to be portrait 800-w x12000-h pixels.",
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('hero_image_desktop'),
        FieldPanel('hero_image_mobile'),
        FieldPanel('subtitle'),
        FieldPanel('body'),
        
    ]
    @path('')
    def default_blog_page(self, request):
        blog_name = "This is the blog name"
        
        return self.render(
            request, 
            context_overrides={
                'blog_name': blog_name
            }
            )
        
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
    
    
    hero_image_desktop = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Image needs to be landscape 2560-w x1400-h pixels.",
        related_name='+'
    )
    
    hero_image_mobile = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Image needs to be portrait 800-w x1200-h pixels.",
        related_name='+'
    )
    
    author = models.ManyToManyField(Author, blank=True, related_name="blog_posts")
        
    
    
    subtitle = models.CharField(max_length=255, blank=True)
    
    
    
    body = StreamField([
        
        ('author', SnippetChooserBlock('blog.Author')),
        ('text', custom_blocks.TextBlock()),
        ('paragraph', custom_blocks.ParagraphBlock()),
        ('banner', custom_blocks.ImageBannerBlock()),
    ], block_counts={
        # 'text': {'min_num': 1, 'max_num': 1},
        
    },
    use_json_field=True, 
    blank=True, 
    null=True, 
    verbose_name="Body Content"
    )
    markdown_field = MarkdownField(blank=True, null=True, verbose_name="Markdown Field")
    
    tags = ClusterTaggableManager(through=BlogPageTags, blank=True)
    
    


    content_panels = Page.content_panels + [
        
        FieldPanel('hero_image_desktop'),
        FieldPanel('hero_image_mobile'),
        FieldPanel('tags'),
        FieldPanel('subtitle'),
        FieldPanel('body'),
        FieldPanel('markdown_field'),  
        
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
        
        
        
    

    


