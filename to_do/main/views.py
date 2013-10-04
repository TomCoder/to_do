# Create your views here.

from django.http import HttpResponse

def home(request):
    html = "<html><body>To Do"
    return HttpResponse(html)
