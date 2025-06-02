from django.shortcuts import render
from .models import App
from django.shortcuts import get_object_or_404
# Create your views here.
def all_template(request):
    apps = App.objects.all()
    return render(request, 'app/all.html', {'apps':apps})

def all_desc(request, app_id):
    desc= get_object_or_404(App, id=app_id)
    return render(request, 'app/desc.html', {'desc': desc})