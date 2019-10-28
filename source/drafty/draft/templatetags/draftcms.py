from django import template
from draft.models.menu import MenuItem

import collections
from pydoc import locate
from importlib import import_module

register = template.Library()

@register.inclusion_tag('draft/component/render.html', takes_context=True)
def component(context):

    request = context['request']
    uri_path = request.META['PATH_INFO']

    try:
        app = MenuItem.objects.get(link=uri_path)
    except MenuItem.DoesNotExist:
        # Try to get by path break down /component/action/
        Component = collections.namedtuple('Component', 'app action id')
        app = Component(app=uri_path.split('/')[1], action=uri_path.split('/')[2], id=False)

    app_class = str(app.app).capitalize() + str(app.action).capitalize() + 'Component'
    app_module_path = app.app.lower() + '.components.' + str(app.action.lower())
    app_module_path_main = app_module_path

    try:
        im = import_module(app_module_path)
    except TypeError as e:
        app_module_path = 'draft.components.error'
        im = import_module(app_module_path)
        request.error = e
        app_class = 'DraftErrorComponent'
    finally:
        # Do some logging?
        pass

    app = getattr(im, app_class)
    app_response = app.render(self=app, request=request)

    return {'content':  app_response['Content']}


""":returns a block position with generated block components
that have been assigned to that position. 
"""
@register.inclusion_tag('draft/blocks/render.html', takes_context=True)
def blocks(context, position):


    request = context['request']
    elements = "this is a story of a girl"
    position = position

    return {'elements': elements, 'position': position, 'request': request}
