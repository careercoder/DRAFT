from django.shortcuts import render



class ComponentmanagerAdminComponent:

    __name__ = 'Component Manager'
    __description__ = 'Will display a single piece of content/article.'
    __version__ = '0.0.1.10'

    def __init__(self):
        pass

    def render(self, request):
        return self.__version__



