from django.shortcuts import render



class ContentSingleComponent:

    __name__ = 'Single'
    __description__ = 'Will display a single piece of content/article.'
    __version__ = '0.0.1.10'

    def __init__(self):
        pass

    def render(self, request):

        response = {'Content':self.__version__}
        return response


