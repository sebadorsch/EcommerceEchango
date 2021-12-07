from django.conf.urls import url
from api.views import api_home, get_user

urlpatterns = [
    url(r'^$', api_home, name='api_home'),
    # url(r'/user/get', get_user, name="get_user")
    url(r'user/get', get_user, name="get_user")
]