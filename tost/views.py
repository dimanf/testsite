from django.shortcuts import render_to_response
from django.template import RequestContext
from testsite.tost.models import *

import os

def first(request):
    images = FirstClass.objects.all()    
    return render_to_response('main.html', locals(), RequestContext(request))