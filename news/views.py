from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.

from news.models import *


# def index(request):
#     return render_to_response('index.html',
#             {'variable': 'Yo soy una vista'},
#             context_instance=RequestContext(request))

def index(request):
    news = News.objects.all().order_by('-posted_date')
    return render_to_response('index.html',
            {'news': news},
            context_instance=RequestContext(request))