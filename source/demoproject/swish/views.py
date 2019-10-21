from django.shortcuts import render

# Create your views here.


def test_view(request):

    context = {}
    template = 'base.html'

    return render(request, template, context)