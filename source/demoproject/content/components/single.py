from django.shortcuts import render



class ContentSingleComponent:

    __version__ = '0.0.1.0'

    def __init__(self):
        pass

    def render(self, request):
        return self.__version__



