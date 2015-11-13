from django.db import models

class Store(models.Model):
    '''
    The stores where the articles are held.
    '''
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=350)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'name: %s, address: %s.' % (self.name, self.address)
    def toJson(self):
        return {'id': self.pk,
                'name':self.name,
                'address': self.address}
