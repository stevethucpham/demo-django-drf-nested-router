from django.urls import path, include
from rest_framework.routers import DefaultRouter

from library import views


router = DefaultRouter()
router.register('authors', views.AuthorViewSet)

app_name = 'library'

urlpatterns = [
    path('', include(router.urls))
]