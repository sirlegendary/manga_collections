from django.shortcuts import render
from .models import MangaCollection
from bs4 import BeautifulSoup
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
            html = urlopen(url.url)
        except HTTPError as e:
            error = e
            print(e)
        except URLError:
            error = "Server down or incorrect domain"
            print("Server down or incorrect domain")
        else:
            soup = BeautifulSoup(html, features='html.parser')
            
            # Get cover image
            if soup.img:
                coverImgRaw = soup.img
                print(f"Raw Cover Image: {coverImgRaw}")
                coverImg = str(coverImgRaw).split('=')[2].strip('"/>')
                print(f"Cover Image: {coverImg}")
            else: # if not found, add placeholder
                coverImg = "https://via.placeholder.com/150"
            
            # Get manga name
            if soup.find("h2", {"class": "aname"}):
                title = soup.find("h2", {"class": "aname"}).text
                print(f"Title: {title}")
            else:
                title = "No Title Found."
            
            # Get Chapter Name, Link to chapter and published date
            if soup.find("table", {"id": "listing"}):
                table = soup.find("table", {"id": "listing"})
                rows = table.findAll('tr')
                for tr in rows:
                    aTag = tr.find('a')
                    urlChapter = str(aTag)
                    print(urlChapter)
                # urlChapter = str(table).split('td')
                # chapterTitle = "chh"
                # chapterRelease = "hh"

                # print(f"Chpater details: {urlChapter}")
            else:
                print("Nothing found")

                # <td>
                # <div class="chico_manga"></div>
                # <a href="/tate-no-yuusha-no-nariagari/61">Tate no Yuusha no Nariagari 61</a> : </td>
                # <td>

            mangaData = {
                'title':title,
                'coverImg': coverImg,
                'name': 'HELLO',
            }

            collection.append(mangaData)

    print(collection)

        # else:
        #     error = "No Data returned from HTML request to managareader." 
        #     print (f"Error! No Data returned from HTML request for {url.name}")

 
    stuff_for_frontend = {
            'error': error,
            'collection': collection,
        }
    return render(request, 'base.html', stuff_for_frontend)
