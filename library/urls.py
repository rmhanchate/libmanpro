from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^search$', views.search, name="search"),
    url(r'^predict$', views.pred, name="predict"),
    url(r'^addtodb$', views.addtodb, name="insert_page"),
    url(r'^addingtodb$', views.database_entry, name="inserting_page"),
    url(r'genre/(?P<genre_name>[\w|\W]+)$', views.get_genre_details, name="genre_page"),
]