from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Store

from middlewares.auth.basicAuth import basicauth

def getStore(storeId):
    '''
    Check if the store exists and return it's object
    '''
    try:
        store = Store.objects.get(pk=storeId)
    except ObjectDoesNotExist:
        store = None
    return store

def getAllStores():
    '''
    Returns a list of all available stores.

    When the table grows in size, optimization is required.
    '''
    stores = Store.objects.all()
    storeJson = map(lambda store: store.toJson(), stores)
    return list(storeJson)

####################
####################
@basicauth
def index(request):
    '''
    General management of stores.
    '''
    if request.method == 'GET':
        store = getAllStores()
        return JsonResponse({'success':True, 'stores': store, 
                             'total_elements': len(store)})
    else:
        return JsonResponse({'success': False, 
                             'error_code':400, 
                             'error_msg':'Request methos unavailable.'}, status=400)

