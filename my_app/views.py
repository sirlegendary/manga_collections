from django.shortcuts import render
from .models import MangaCollection
from bs4 import BeautifulSoup


def home(request):
    
    for url in MangaCollection.objects.all():
        
        response = request.POST.get(url.url)
        # soup = BeautifulSoup(response, features='html.parser')
        print (response)


    
    # response = requests.get(final_url)
    # data = response.text
    # soup = BeautifulSoup(data, features='html.parser')
    manga = "hi"
    stuff_for_frontend = {
            'mangas': manga,
        }
    return render(request, 'base.html', stuff_for_frontend)
