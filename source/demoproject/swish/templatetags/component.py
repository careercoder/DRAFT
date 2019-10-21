from django import template
from pydoc import locate

register = template.Library()

""":returns a block position with generated block components
that have been assigned to that position. 
"""
@register.inclusion_tag('swish/menu/main.tmpl.html', takes_context=True)
def block_position(context, position):

    request = context['request']
    elements = "this is a story of a girl"
    position = position

    return {'elements': elements, 'position': position, 'request': request}
