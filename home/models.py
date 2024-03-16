from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from blocks import blocks as custom_blocks
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel, FieldRowPanel, HelpPanel, MultipleChooserPanel, TitleFieldPanel

class HomePage(Page):
    max_count = 1
    body = StreamField([
        ('rich_text', custom_blocks.ParagraphBlock()),
        ('carousel', custom_blocks.CarouselBlock()),
        ('hero', custom_blocks.HeroBlock()),
        ('video', custom_blocks.VideoBlock()),
        
        
    ],
        block_counts={},
        use_json_field=True, 
        blank=True,
        null=True
        )
    content_panels = Page.content_panels + [
        
        FieldPanel('body'),
    ]
                       
