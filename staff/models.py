from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model
from wagtail.fields import RichTextField
from wagtail.images import get_image_model


class StaffIndex(Page):
    max_count = 1
    parent_page_types = ['home.HomePage']
    subpage_types = ['staff.StaffPage']  # Restrict child page types
    # Add any specific fields for the category if needed
    staff_hero = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    subtitle = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    
    def get_context(self, request):
        context = super().get_context(request)
        context['staffpage'] = StaffPage.objects.live().public()
        return context

    content_panels = Page.content_panels + [
        FieldPanel('staff_hero'),
        FieldPanel('subtitle'),
        FieldPanel('description'),
    ]

    
    
    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"

class StaffPage(Page):
    parent_page_types = ['staff.StaffIndex']
    sub_page_types = []
    
    ROLE_CHOICES = (
        ('owner', 'Owner / CEO'),
        ('office', 'Office Staff'),
        ('sales', 'Sales'),
        ('project_manager', 'Project Manager'),
    )
    
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True)
    job_catagory = models.CharField(
        max_length=255, choices=ROLE_CHOICES)
    email = models.EmailField( blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    bio = RichTextField(blank=True)
    image = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'  
    )
    def get_admin_display_title(self):
        return "Custom Home Page Title"
    
    content_panels = Page.content_panels + [
        FieldPanel('first_name'),
        FieldPanel('last_name'),
        FieldPanel('job_title'),
        FieldPanel('job_catagory'),
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('bio'),
        FieldPanel('image'),
    ]
    
    