from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Q

# Create your views here.
def Signin(request):
    return render(request, 'Netflix/login.html')

def Signup(request):
    return render(request, 'Netflix/Signup.html')



def home(request):
    query = request.GET.get('q', '')
    content_type = request.GET.get('type', '')

    # Filter content based on search query and content type
    if query:
        if content_type == 'Series' or content_type == '':
            Series_results = Series.objects.filter(Name__icontains=query)
        else:
            Series_results = Series.objects.none()
        
        if content_type == 'Movies' or content_type == '':
            Movies_results = Movies.objects.filter(Name__icontains=query)
        else:
            Movies_results = Movies.objects.none()
        
        if content_type == 'Anime' or content_type == '':
            Anime_results = Anime.objects.filter(Name__icontains=query)
        else:
            Anime_results = Anime.objects.none()

        if content_type == 'Sitcom' or content_type == '':
            Sitcom_results = Sitcom.objects.filter(Name__icontains=query)
        else:
            Sitcom_results = Sitcom.objects.none()

        if content_type == 'Cartoon' or content_type == '':
            Cartoon_results = Cartoon.objects.filter(Name__icontains=query)
        else:
            Cartoon_results = Cartoon.objects.none()
    else:
        # If no query is provided, return all items
        Series_results = Series.objects.all()
        Movies_results = Movies.objects.all()
        Anime_results = Anime.objects.all()
        Sitcom_results = Sitcom.objects.all()
        Cartoon_results = Cartoon.objects.all()

    # Context to pass to the template
    context = {
        'query': query,
        'content_type': content_type,
        'Series': Series_results,
        'Movies': Movies_results,
        'Anime': Anime_results,
        'Sitcom': Sitcom_results,
        'Cartoon': Cartoon_results,
    }

    return render(request, 'Netflix/index.html', context)




