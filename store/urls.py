from django.conf.urls import url

from store import views

urlpatterns = [
    url(
        regex=r'^products/$',
        view=views.ProductView.as_view(),
        name="product-list"
    ),
]
