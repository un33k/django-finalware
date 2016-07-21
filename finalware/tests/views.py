from django.template import context_processors
from django.template.loader import get_template
from django.http import HttpResponse


def request_processor(request):
    context = {
        'processors': [context_processors.request],
    }
    template = get_template('finalware/context_processors.html')
    return HttpResponse(template.render(context, request))
