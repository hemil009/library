from django.conf.urls import url
from . import views


app_name = 'books'

urlpatterns = [
    url(r'^$', views.book_list, name="list"),
    url(r'^create/$', views.book_create, name="create"),
    ]