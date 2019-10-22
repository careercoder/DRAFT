from django import template
from pydoc import locate

register = template.Library()

""":returns the primary component of the page to be rendered. 
"""
@register.inclusion_tag('swish/component/display.html', takes_context=True)
def component(context):

    request = context['request']
    elements = "this is a story of a girl"
    position = position

    return {'elements': elements, 'position': position, 'request': request}


@register.inclusion_tag('swish/block/display.html', takes_context=True)
def block(context, position):

    request = context['request']
    elements = "this is a story of a girl"
    position = position

    return {'elements': elements, 'position': position, 'request': request}
