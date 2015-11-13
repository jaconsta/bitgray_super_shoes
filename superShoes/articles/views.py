from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Article
from stores.models import Store

def getStore(storeId):
    '''
    Check if the store exists and return it's object
    '''
    try:
        store = Store.objects.get(pk=storeId)
    except ObjectDoesNotExist:
        store = None
    return store
    
def getStoreArticles(storeId):
    '''
    Get the articles that belongs to a store from it's Id
    '''
    store = getStore(storeId)
    if store is None:
        return None
    articles = Article.objects.filter(store__pk=store)
    articleJson = map(lambda article: article.toJson(), articles)
    return articles

def getAllArticles():
    '''
    Returns a list of all available stores.

    When the table grows in size, optimization is required.
    '''
    articles = Article.objects.all()
    articleJson = map(lambda article: article.toJson(), articles)
    return list(articleJson)

####################
####################

def index(request):
    '''
    General management of articles.
    '''
    if request.method == 'GET':
        article = getAllArticles()
        return JsonResponse({'success':True, 'articles': article, 
                             'total_elements': len(article)})
    else:
        return JsonResponse({'success': False, 
                             'error_code':400, 
                             'error_msg':'Request methos unavailable.'}, status=400)

def storeArticles(request, storeId):
    '''
    Load all the articles from a specific store.
    '''
    if request.method == 'GET':
        article = getStoreArticles(storeId)
        if article == None:
            return JsonResponse({'success': False, 
                                 'error_code':404, 
                                 'error_msg':'Record not Found.'}, status=404)
        return JsonResponse({'success':True, 'articles': article, 
                             'total_elements': len(article)})
    else:
        return JsonResponse({'success': False, 
                             'error_code':400, 
                             'error_msg':'Request methos unavailable.'}, status=400)

