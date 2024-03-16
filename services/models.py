from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model
from wagtail.documents import get_document_model
from blog.models import Author

class ServicesIndex(Page):
    max_count = 1
    parent_page_types = ['home.HomePage']
    subpage_types = ['services.ServicesCategoryPage']  # Restrict child page types
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
        verbose_name = "Services"
        verbose_name_plural = "Services"

class ServicesCategoryPage(Page):
    # Fields specific to the subcategory
    
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

    parent_page_types = ['services.ServicesIndex']  # Restrict parent page type
    subpage_types = ['services.ServicePage']  # Restrict child page types
    
    class Meta:
        verbose_name = "Service Category"
        verbose_name_plural = "Services Categories"

class ServicePage(Page):
    # Service specific fields
    service_hero = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    brochure = models.ForeignKey(
        get_document_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    description = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('service_hero'),
        FieldPanel('brochure'),
        FieldPanel('description'),
    ]

    parent_page_types = ['services.ServicesCategoryPage']  # Restrict parent page type
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        

