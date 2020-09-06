from django.urls import path, include
from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from library import views


router = DefaultRouter()
router.register('libraries', views.LibraryViewSet)

app_name = 'library'

urlpatterns = [
    path('', include(router.urls)),
    # 1
    url(r'^libraries/(?P<library_id>\d+)/books/?$', 
        views.BookViewSet.as_view({'get': 'list', 'post': 'create'}), name='library-books'),
    # 2
    url(r'^libraries/(?P<library_id>\d+)/books/(?P<pk>\d+)/?$', 
        views.BookViewSet.as_view({'get': 'retrieve'}), name='library-book-detail'),
]