from .views import (
    ShortUrlsSet,
    # ShortUrlViewApi,  
    optout
)
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register(r'shorturls', ShortUrlsSet, basename='shorturls')
urlpatterns = [
    # path('short_url/<str:short_url>/', ShortUrlViewApi.as_view(),
    #     name='api_short_url'),
    path('optout/<str:short_url>/', optout, name='api_short_url')

]


urlpatterns += router.urls