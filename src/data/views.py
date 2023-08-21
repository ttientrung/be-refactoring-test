from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as df_filters
from rest_framework import viewsets, permissions, filters
from .models import Campaign, AdSet, Creative, Account
from .serializers import CampaignSerializer, AdSetSerializer, CreativeSerializer, AccountSerializer
from .filters import CampaignFilter, AdSetFilter, CreativeFilter


class CampaignViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CampaignSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = CampaignFilter
    search_fields = ['campaign_name']

    def get_queryset(self):
        return Campaign.objects.all()

class AdSetViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AdSetSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = AdSetFilter
    search_fields = ['adset_name']

    def get_queryset(self):
        return AdSet.objects.all()

class CreativeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CreativeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = CreativeFilter
    search_fields = ['ad_name']

    def get_queryset(self):
        return Creative.objects.all()

class AccountViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Account.objects.all()
