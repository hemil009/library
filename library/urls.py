from django.contrib import admin
from django.conf.urls import url, include
from books import views as book_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^books/', include('books.urls')),
    url(r'^$', book_views.book_list, name="home")
]

urlpatterns += staticfiles_urlpatterns()