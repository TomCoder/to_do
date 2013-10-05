# Create your views here.
import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from main.models import Event


def home(request):
    if request.method == "POST":
        #import pdb; pdb.set_trace() 
        title = request.POST["title"]
        description = request.POST["description"]
        venue = request.POST["venue"]
        date = request.POST["date"].split("-")
        event = Event(
                title=title,
                description=description,
                venue=venue,
                date=datetime.date(int(date[0]), int(date[1]), int(date[2]))
                )
        event.save()
        return HttpResponseRedirect("/list")
        #import pdb; pdb.set_trace()

    return render_to_response("create.html", {}, context_instance=RequestContext(request))

def to_dos(request):
    events = Event.objects.all()
    return render_to_response("list.html", {"events":events}, context_instance=RequestContext(request))
