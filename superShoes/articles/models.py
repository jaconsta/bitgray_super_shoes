from django.db import models
from articles.models import Store

class Article(models.Model):
    '''
    Description of the articles in the inventory.
    '''
    name = models.CharField(max_length=150)
    description = models.textField()
    price = models.FloatField()
    total_in_shelf = models.PositiveIntegerField()
    total_in_vault = models.PositiveIntegerField()
    store = models.ForeignKey('Store') 
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'name:%s, price: $%s.' % (self.name, self.price)
    def toJson(self):
        return {'id': self.pk,
                'description': self.description,
                'name': self.name,
                'price': self.price,
                'total_in_shelf': self.total_in_shelf,
                'total_in_vault': self.total_in_vault,
                'store_name': self.store.name}
