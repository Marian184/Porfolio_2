from .models import Job
from django.shortcuts import render, get_object_or_404


# Create your views here.
def home(request):
    jobs = Job.objects.all
    return render(request, 'jobs/home.html',{"jobs": jobs})

def jobdetail(request,job_id):
    detailjob = get_object_or_404(Job, pk=job_id)
    return render(request, 'blog/personal_data.html', {'blog':detailjob})