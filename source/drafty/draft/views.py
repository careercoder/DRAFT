from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def draft_cms(request):

    context = {}
    template = 'base.html'

    return render(request, template, context)
