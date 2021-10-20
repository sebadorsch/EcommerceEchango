from django.conf.urls import url
from Echango.views import home, shop_product_col_3, shop_single_product, about_us, \
    shop_product_col_3_categoria, carrito

urlpatterns = [
    url(r'^$', home, name='home'),
    url('about_us', about_us, name='about_us'),
    url('lista_productos/(?P<categoria>.*)', shop_product_col_3_categoria, name='shop_product_col_3_categoria'),
    url('lista_productos', shop_product_col_3, name='shop_product_col_3'),
    url(r'producto_(?P<producto_id>\d+)', shop_single_product, name='shop_single_product'),
    url('carrito', carrito, name='carrito'),
]