# views

from django.shortcuts import render_to_response
from django.template import RequestContext

def homepage(request):
    """ View da home """

    context = RequestContext(request)
    return render_to_response('index.html', context)