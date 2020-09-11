from django.urls import path, include
from django.conf.urls import url

from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from library import views

router = SimpleRouter()
router.register('libraries', views.LibraryViewSet)

book_router = routers.NestedSimpleRouter(
    router,
    r'libraries',
    lookup='library')

book_router.register(
    r'books',
    views.BookViewSet,
    basename='library-books'
)

app_name = 'library'

urlpatterns = [
    path('', include(router.urls)),
    path('', include(book_router.urls)),
    # 1
    # url(r'^libraries/(?P<library_id>\d+)/books/?$', 
    #     views.BookViewSet.as_view({'get': 'list'}), name='library-books'),
    # # 2
    # url(r'^libraries/(?P<library_id>\d+)/books/(?P<pk>\d+)/?$', 
    #     views.BookViewSet.as_view({'get': 'retrieve'}), name='library-book-detail'),
]