# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request, template_name='home/index.html'):
    content = {}
    content['title'] = 'Emailstat.us'

    return render_to_response(template_name, content, context_instance=RequestContext(request))
