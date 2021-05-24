from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shortener.api import views

router = DefaultRouter()
router.register('short_link', views.ShortLinkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]