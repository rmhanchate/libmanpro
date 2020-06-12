import json
from django.shortcuts import render
from django.http import JsonResponse
from django.db import IntegrityError
from haystack.query import SearchQuerySet
from .models import Book, Author, Genre
from .predict import *

def home(request):
    return render(request, "home.html")

def search(request):
    print(request)
    query = request.GET.get("query", "").strip()
    result = {"book": [], "author": [], "genre": []}
    print('Query: ' + query)
    if not query and len(query) < 3:
        return JsonResponse(result)
    book_pks = list(SearchQuerySet().autocomplete(i_book_name=query).values_list("pk", flat=True))
    print('Books Queried')
    author_pks = list(SearchQuerySet().autocomplete(i_author_name=query).values_list("pk", flat=True))
    print('Authors Queried')
    genre_pks = list(SearchQuerySet().autocomplete(i_genre_name=query).values_list("pk", flat=True))
    print('Genres Queried')
    
    result["books"] = [ Book.objects.filter(pk=book_pk).values().first() for book_pk in book_pks ]
    result["authors"] = [ Author.objects.filter(pk=author_pk).values().first() for author_pk in author_pks ]
    res = [ Genre.objects.filter(pk=genre_pk).values().first() for genre_pk in genre_pks ]
    if (len(res) > 0):
        result["genres"] = [res[0]]
    else:
        result["genres"] = res
    return render(request, "search_results.html", result)

def get_genre_details(request, genre_name):
    result = {"books": [], "authors": [], "genre": genre_name}
    ids = Genre.objects.values_list('id', flat=True).filter(genre = genre_name)
    result["books"] = [ Book.objects.filter(id = idi).values().first() for idi in ids ]
    result["authors"] = [ Author.objects.filter(id = idi).values().first() for idi in ids ]
    return render(request, "genre.html", result)

def pred(request):
    query = request.GET.get("query", "")
    print('Query: ' + query)
    result = {"predicted": ''}
    predicted = NaivBay(query)
    result["predicted"] = predicted
    return render(request, "predict_results.html", result)

def addtodb(request):
    query = request.GET.get("query", "")
    result = {'temp': 1}
    print(result)
    return render(request, "database_entry.html", result)  
    
def database_entry(request):
    query = request.GET.get("query").strip()
    query = json.loads(query.replace("'", "\""))
    print('Inerting into DB: ' + str(query))
    title = query["title"]
    author = query["author"]
    ids = query["ids"]
    genre = query["genre"]
    link = query["link"]
    result = list(Genre.objects.filter(genre = genre).values())
    classs = round(result[-1]['clas'] + 0.001,5)
    print(classs)
    result = {"class": []}
    try:
        Book.objects.create(title=title, id = ids, link = link)
        Author.objects.create(id = ids, author = author)
        Genre.objects.create(id = ids, clas = classs, genre = genre)
        print('1')
    except IntegrityError:
        result = {"success": None, "message": "Book already exists"}
        print('2')
        return JsonResponse(result)
    result['class'] = classs
    result = {'class': classs}
    
    return render(request, "successful.html", result)
