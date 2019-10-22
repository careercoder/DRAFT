from django import template
from pydoc import locate
import collections

# Import Core Things Needed... eg.) menu
from swish.models.menu import MenuItem

register = template.Library()

""":returns the primary component of the page to be rendered. 
"""
@register.inclusion_tag('swish/component/display.html', takes_context=True)
def component(context):

    request = context['request']

    try:
        app = MenuItem.objects.get(link=request.META['PATH_INFO'])
    except MenuItem.DoesNotExist:
        # Try to get by path break down /component/action/
        Component = collections.namedtuple('Component', 'app action id')
        app = Component(app="content", action="single", id=False)

    app_class = str(app.app).capitalize() + str(app.action).capitalize() + 'Component'

    return {'content': app_class}


""":returns a block position with generated block components
that have been assigned to that position. 
"""
@register.inclusion_tag('swish/menu/main.tmpl.html', takes_context=True)
def blocks(context, position):

    request = context['request']
    elements = "this is a story of a girl"
    position = position

    return {'elements': elements, 'position': position, 'request': request}
