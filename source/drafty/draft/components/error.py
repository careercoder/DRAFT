from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string

class DraftErrorComponent:


    def render(self, request):


        context = {}
        template = 'draft/errors/render.html'
        content = render_to_string(template, context, request)

        response = {
                    "Content-Type": "text/html",
                    "Content":  content
        }

        return response


