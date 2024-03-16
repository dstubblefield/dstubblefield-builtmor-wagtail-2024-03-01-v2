from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from taggit.models import Tag
from blog.models import Author


@register_snippet
class TagSnippetViewSet(SnippetViewSet):
    model = Tag
    icon = 'tag'
    add_to_admin_menu = True
    menu_label = 'Tags'
    menu_order = 500
    list_display = ('name', 'slug')
    search_fields = ('name')
    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]
    
@register_snippet
class AuthorSnippetViewSet(SnippetViewSet):
    model = Author
    icon = 'user'
    add_to_admin_menu = True
    menu_label = 'Authors'
    menu_order = 500
    list_display = ('name', 'bio')
    search_fields = ('name')
    

    
    
