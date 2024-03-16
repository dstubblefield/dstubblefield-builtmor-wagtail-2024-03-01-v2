from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultipleChooserPanel
from wagtail.images import get_image_model
from wagtail.documents import get_document_model
from modelcluster.fields import ParentalKey

class ProductsIndex(Page):
    max_count = 1
    parent_page_types = ['home.HomePage']
    subpage_types = ['products.ProductsCategoryPage']  # Restrict child page types
    # Add any specific fields for the category if needed
    category_hero_desktop = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Image needs to be landscape 1920-w x1080-h pixels.",
        related_name='+'
    )
    category_hero_mobile = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Image needs to be portrait 800-w x1200-h pixels.",
        related_name='+'
    )
    description = RichTextField(blank=True)
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context['categories'] = ProductsCategoryPage.objects.live().public()
        return context
        

    content_panels = Page.content_panels + [
        FieldPanel('category_hero_desktop'),
        FieldPanel('category_hero_mobile'),
        FieldPanel('description'),
    ]

    
    
    class Meta:
        verbose_name = "Products"
        verbose_name_plural = "Products"

class ProductsCategoryPage(Page):
    # Fields specific to the subcategory
    subcategory_hero_desktop = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Image needs to be landscape 1920-w x1080-h pixels.",
        related_name='+'
    )
    subcategory_hero_mobile = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Image needs to be portrait 800-w x1200-h pixels.",
        related_name='+'
    )
    
    category_brochure = models.ForeignKey(
        get_document_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    details = RichTextField(blank=True)
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['products'] = ProductPage.objects.child_of(self).live().public()
        return context

    content_panels = Page.content_panels + [
        FieldPanel('subcategory_hero_desktop'),
        FieldPanel('subcategory_hero_mobile'),
        FieldPanel('category_brochure'),
        FieldPanel('details'),
    ]

    parent_page_types = ['products.ProductsIndex']  # Restrict parent page type
    subpage_types = ['products.ProductPage']  # Restrict child page types
    
    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Products Categories"

class ProductPage(Page):
    # Product specific fields
    product_hero_desktop = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Image needs to be landscape 1920-w x1080-h pixels.",
        related_name='+'
    )
    product_hero_mobile = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Image needs to be portraits 800-w x 1,200-h pixels.",
        related_name='+'
    )
    brochure = models.ForeignKey(
        get_document_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('product_hero_desktop'),
        FieldPanel('product_hero_mobile'),
        MultipleChooserPanel('gallery_images', label="Gallery images", chooser_field_name="image"),
        FieldPanel('brochure'),
        FieldPanel('description'),
    ]

    parent_page_types = ['products.ProductsCategoryPage']  # Restrict parent page type
    child_page_types = []  # No child pages allowed
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
class ProductPageGalleryImage(Orderable):
    page = ParentalKey(ProductPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        get_image_model(), 
        on_delete=models.CASCADE, 
        related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]
