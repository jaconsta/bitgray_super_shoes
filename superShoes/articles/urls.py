from django.conf.urls import url

from . import views 

urlpatterns = [
    # /services/articles/
    url(r'^$', views.index, name='articleIndex'),
    url(r'^stores/(?P<storeId>[0-9]+)$', views.crud, name='articleStore')
]