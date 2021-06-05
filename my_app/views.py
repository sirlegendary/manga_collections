from django.shortcuts import render
from .models import MangaCollection
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import re


def home(request):
    error = None
    collection = []
    
    #Get all the manga urls from the database
    for url in MangaCollection.objects.all():

        try:
            # Get the Html page for the url
            req = urllib.request.Request(url.url, headers = {"User-Agent": "Chrome"})
            html = urlopen(req)
        except HTTPError as e:
            error = e
            print(f"\n HTTPError: {e}\n")
        except URLError:
            error = "Server down or incorrect domain"
            print(f"\n Server down or incorrect domain \n")
        else:
            soup = BeautifulSoup(html, features='html.parser')
            
            # Get cover image
            coverImgRaw = soup.find("meta",  property="og:image")
            coverImg = coverImgRaw["content"] if coverImgRaw else "https://via.placeholder.com/150"
            
            # Get manga title
            titleRaw = soup.find("meta",  property="og:title")
            title = titleRaw["content"] if titleRaw else "Manga Title not found."

            # Get manga url
            mangaUrlRaw = soup.find("meta",  property="og:url")
            mangaUrl = mangaUrlRaw["content"] if mangaUrlRaw else "https://www.taadd.com/"

            # get all chapters
            chapters = []
            for a_tag in soup.find_all(href=True):
                if a_tag['href'].startswith("/chapter/") and "-" in a_tag['href']:
                    chapterFilter = a_tag['href'].split("/")
                    chapter = chapterFilter[2].replace('-',' ')
                    chapterUrl = a_tag['href']
                    release_date = a_tag.text
                    
                    chapterDetails = {
                        'chapter':chapter,
                        'chapterUrl':chapterUrl,
                        'release_date':release_date,
                    }
                    
                    chapters.append(chapterDetails)
            
            # sortedChapters = sorted(chapters, key = lambda i: i['chapter'],reverse=True)
            
            mangaData = {
                'title':title,
                'coverImg': coverImg,
                'mangaUrl': mangaUrl,
                'chapters': chapters if len(chapters) > 0 else None,
            }

            collection.append(mangaData)

    # sortedManga = sorted(collection, key = lambda i: i['chapters'],reverse=True)

    stuff_for_frontend = {
            'error': error,
            'collection': collection,
        }
    return render(request, 'base.html', stuff_for_frontend)
