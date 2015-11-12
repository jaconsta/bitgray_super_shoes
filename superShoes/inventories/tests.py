from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from models import Store, Article

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

class ArticleMethosTests(TestCase):
    '''
    Test the article methods and behaviours
    '''
    def test_create_article(self):
        '''
        Create an article
        '''
        store = create_store(storeName='Choke', storeAddress='Main Strees with second block')
        article = { 'name':'basic show', 
                    'description':'Wooden shoe for foot', 
                    'price':5000, 
                    'total_in_shelf': 4, 
                    'total_in_vault': 100, 
                    'store': store.id}
        articleResponse = self.client.post(reverse('inventories:articleIndex'), 
                                            article, 
                                            content_type='application/json')
        self.assertEqual(articleResponse.status_code, 200)

    def load_all_articles(self):
        articleResponse = self.client.get(reverse('inventories:articleIndex'))
        self.assertEqual(articleResponse.status_code, 200)

    def load_articles_of_a_store(self):
        articleResponse = self.client.get(reverse('inventories:storeArticle', kwargs={'app_label': 1}))
        self.assertEqual(articleResponse.status_code, 200)

    def load_store_articles_error_id_is_not_number(self):
        articleResponse = self.client.get(reverse('inventories:storeArticle', kwargs={'app_label': 'noId'}))
        self.assertEqual(articleResponse.status_code, 400)
        self.assertConstains(articleResponse, 'Bad request')

    def load_store_articles_error_id_not_exists(self):
        articleResponse = self.client.get(reverse('inventories:storeArticle', kwargs={'app_label': 9999}))
        self.assertEqual(articleResponse.status_code, 404)
        self.assertConstains(articleResponse, 'Record not found')