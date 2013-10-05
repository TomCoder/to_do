# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from main.models import Event

def home(request):
    if request.method == "POST":
        import pdb; pdb.set_trace() 

    return render_to_response("create.html", {}, context_instance=RequestContext(request))

def to_dos(request):
    events = Event.objects.all()
    return render_to_response("list.html", {"events":events}, context_instance=RequestContext(request))
