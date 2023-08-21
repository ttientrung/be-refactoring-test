from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, AdSetViewSet, CreativeViewSet, AccountViewSet

router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet, basename='campaign')
router.register(r'adsets', AdSetViewSet, basename='adset')
router.register(r'creatives', CreativeViewSet, basename='creative')
router.register(r'accounts', AccountViewSet, basename='account')

urlpatterns = router.urls
