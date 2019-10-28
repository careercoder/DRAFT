from django.template.loader import render_to_string


class ContentListBlock:

    __name__ = 'List'
    __description__ = 'Creates a List of Articles'
    __version__ = '0.0.1.10'

    def __init__(self):
        pass

    def render(self, request):

        render = render_to_string('content/blocks/list.html', {'foo': 'bar'})
        response = {'Content': render}

        return response

