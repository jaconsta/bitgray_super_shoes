from django.conf.urls import url

from . import views 

urlpatterns = [
    # /services/stores
    url(r'^$', views.index, name='storeIndex'),
]