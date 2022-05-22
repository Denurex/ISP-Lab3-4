
"""local URL binding of the application"""

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='main_page'),
    #path('info', views.about, name='info_page'),
    path('create', views.create, name='create_page'),
    path('product', views.shop, name='products_page'),
    path('shopping_cart', views.shop_cart, name='shopcart_page'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

