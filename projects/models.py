from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model
from wagtail.documents import get_document_model
from wagtail.fields import RichTextField
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

class ProjectPageTags(TaggedItemBase):
    content_object = ParentalKey(
        'projects.ProjectPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class ProjectsIndex(Page):
    max_count = 1
    parent_page_types = ['home.HomePage']
    subpage_types = ['projects.ProjectsCategoryPage']  # Restrict child page types
    # Add any specific fields for the category if needed
    category_hero = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    description = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('category_hero'),
        FieldPanel('description'),
    ]

    
    
    class Meta:
        verbose_name = "Projects"
        verbose_name_plural = "Projects"

class ProjectsCategoryPage(Page):
    # Fields specific to the subcategory
    template = "projects/projects_category_page.html"
    parent_page_types = ['projects.ProjectsIndex']  # Restrict parent page type
    subpage_types = ['projects.ProjectPage']  # Restrict child page types
    
    subcategory_hero = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    category_brochure = models.ForeignKey(
        get_document_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    details = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subcategory_hero'),
        FieldPanel('category_brochure'),
        FieldPanel('details'),
    ]

    
    class Meta:
        verbose_name = "Project Category"
        verbose_name_plural = "Projects Categories"

class ProjectPage(Page):
    # Project specific fields
    template = "projects/project_page.html"
    parent_page_types = ['projects.ProjectsCategoryPage']  # Restrict parent page type
    child_page_types = []  # No child page types
    
    tags = ClusterTaggableManager(through=ProjectPageTags, blank=True)
    project_hero = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    subtitle = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=20, blank=True, default="Illinois")
    special_features = models.TextField(blank=True)
    project_dimensions = models.CharField(max_length=100, blank=True)
    sales_person = models.CharField(max_length=100, blank=True)
    
    description = models.TextField()
    
    review = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('project_hero'),
        FieldPanel('subtitle'),
        FieldPanel('tags'),
        FieldPanel('description'),
    ]
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        

