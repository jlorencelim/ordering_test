from django.conf.urls import url

from store import views

urlpatterns = [
    url(r'^$', views.ProductView.as_view(), 'product_list'),
]
