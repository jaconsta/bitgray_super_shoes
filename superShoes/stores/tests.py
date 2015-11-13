from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from .models import Store

def create_store(storeName, storeAddress):
    '''
    Creates a store record for testing
    '''
    return Store.object.create(name=storeName, address=storeAddress)

class StoreMethodTests(TestCase):
    '''
    Test the store methods and behaviours
    For TDD instead of pure url the reverse method is used
    '''
    def test_create_store(self):
        store = {'name':'Manhathan', 'address':}
        storeResponse = self.client.post(reverse('inventories:storeIndex'), 
                                            store, 
                                            content_type='application/json')
        self.assertEqual(storeResponse.status_code, 200)

    def load_all_stores(self):
        storeResponse = self.client.get(reverse('inventories:storeIndex'))
        self.assertEqual(storeResponse.status_code, 200)
