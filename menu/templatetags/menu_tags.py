from django import template
from ..models import MenuItem
from django.template import Template, Context

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(menu_name=menu_name).prefetch_related('children')
    current_url = context['request'].path

    def draw_item(item):
        children = item.children.all()
        active_class = '_active' if current_url == item.url else None
        if children:
            return f'<li class="list-group-item"><a href="{item.url}" class="{active_class}">• {item.item_name}</a><ul class="list-group list-group-flush">{"".join([draw_item(child) for child in children])}</ul></li>'
        else:
            active_class = '_active' if current_url == item.url else None
            return f'<li class="list-group-item"><a href="{item.url}" class="{active_class}">• {item.item_name}</a></li>'

    menu_html = ''.join([draw_item(item) for item in menu_items])

    return Template('{% autoescape off %} <ul class="list-group list-group-flush"> {{ menu_html }} </ul> {% endautoescape %}').render(Context({"menu_html": menu_html}))
