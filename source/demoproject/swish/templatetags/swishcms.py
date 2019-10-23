from django import template
from swish.models.menu import MenuItem

import collections
from pydoc import locate
from importlib import import_module

register = template.Library()

@register.inclusion_tag('swish/component/display.html', takes_context=True)
def component(context):

    request = context['request']

    try:
        app = MenuItem.objects.get(link=request.META['PATH_INFO'])
    except MenuItem.DoesNotExist:
        # Try to get by path break down /component/action/
        Component = collections.namedtuple('Component', 'app action id')
        app = Component(app="content", action="single", id=False)
        pass

    app_class = str(app.app).capitalize() + str(app.action).capitalize() + 'Component'

    """ This should follow the guidelines but will eventually be moved to a dynamic way to change this... """
    app_module_path = app.app.lower() + '.components.' + str(app.action.lower())
    im = import_module(app_module_path)

    app_class = getattr(im, app_class)
    app_class = app_class.render(self=app_class, request=request)

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
