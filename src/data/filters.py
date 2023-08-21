
from django_filters import rest_framework as df_filters
from .models import Campaign, AdSet, Creative


class CampaignFilter(df_filters.FilterSet):
    adAccountNo = df_filters.CharFilter(field_name='account__adAccountNo', lookup_expr='exact')
    cost__gt = df_filters.NumberFilter(field_name="cost", lookup_expr='gt')
    cost__lt = df_filters.NumberFilter(field_name="cost", lookup_expr='lt')
    cost__gte = df_filters.NumberFilter(field_name="cost", lookup_expr='gte')
    cost__lte = df_filters.NumberFilter(field_name="cost", lookup_expr='lte')
    
    clickCount__gt = df_filters.NumberFilter(field_name="clickCount", lookup_expr='gt')
    clickCount__lt = df_filters.NumberFilter(field_name="clickCount", lookup_expr='lt')
    clickCount__gte = df_filters.NumberFilter(field_name="clickCount", lookup_expr='gte')
    clickCount__lte = df_filters.NumberFilter(field_name="clickCount", lookup_expr='lte')

    convSales__gt = df_filters.NumberFilter(field_name="convSales", lookup_expr='gt')
    convSales__lt = df_filters.NumberFilter(field_name="convSales", lookup_expr='lt')
    convSales__gte = df_filters.NumberFilter(field_name="convSales", lookup_expr='gte')
    convSales__lte = df_filters.NumberFilter(field_name="convSales", lookup_expr='lte')
    
    convCount__gt = df_filters.NumberFilter(field_name="convCount", lookup_expr='gt')
    convCount__lt = df_filters.NumberFilter(field_name="convCount", lookup_expr='lt')
    convCount__gte = df_filters.NumberFilter(field_name="convCount", lookup_expr='gte')
    convCount__lte = df_filters.NumberFilter(field_name="convCount", lookup_expr='lte')
    
    class Meta:
        model = Campaign
        fields = {
        }

class AdSetFilter(df_filters.FilterSet):
    adAccountNo = df_filters.CharFilter(field_name='account__adAccountNo', lookup_expr='exact')
    campaignNo = df_filters.CharFilter(field_name='campaign__campaignNo', lookup_expr='exact')
    cost__gt = df_filters.NumberFilter(field_name="cost", lookup_expr='gt')
    cost__lt = df_filters.NumberFilter(field_name="cost", lookup_expr='lt')
    cost__gte = df_filters.NumberFilter(field_name="cost", lookup_expr='gte')
    cost__lte = df_filters.NumberFilter(field_name="cost", lookup_expr='lte')
    
    clickCount__gt = df_filters.NumberFilter(field_name="clickCount", lookup_expr='gt')
    clickCount__lt = df_filters.NumberFilter(field_name="clickCount", lookup_expr='lt')
    clickCount__gte = df_filters.NumberFilter(field_name="clickCount", lookup_expr='gte')
    clickCount__lte = df_filters.NumberFilter(field_name="clickCount", lookup_expr='lte')

    convSales__gt = df_filters.NumberFilter(field_name="convSales", lookup_expr='gt')
    convSales__lt = df_filters.NumberFilter(field_name="convSales", lookup_expr='lt')
    convSales__gte = df_filters.NumberFilter(field_name="convSales", lookup_expr='gte')
    convSales__lte = df_filters.NumberFilter(field_name="convSales", lookup_expr='lte')
    
    convCount__gt = df_filters.NumberFilter(field_name="convCount", lookup_expr='gt')
    convCount__lt = df_filters.NumberFilter(field_name="convCount", lookup_expr='lt')
    convCount__gte = df_filters.NumberFilter(field_name="convCount", lookup_expr='gte')
    convCount__lte = df_filters.NumberFilter(field_name="convCount", lookup_expr='lte')
    
    class Meta:
        model = AdSet
        fields = {
        }

class CreativeFilter(df_filters.FilterSet):
    adAccountNo = df_filters.CharFilter(field_name='account__adAccountNo', lookup_expr='exact')
    adSetNo = df_filters.CharFilter(field_name='ad_set__adSetNo', lookup_expr='exact')
    cost__gt = df_filters.NumberFilter(field_name="cost", lookup_expr='gt')
    cost__lt = df_filters.NumberFilter(field_name="cost", lookup_expr='lt')
    cost__gte = df_filters.NumberFilter(field_name="cost", lookup_expr='gte')
    cost__lte = df_filters.NumberFilter(field_name="cost", lookup_expr='lte')
    
    clickCount__gt = df_filters.NumberFilter(field_name="clickCount", lookup_expr='gt')
    clickCount__lt = df_filters.NumberFilter(field_name="clickCount", lookup_expr='lt')
    clickCount__gte = df_filters.NumberFilter(field_name="clickCount", lookup_expr='gte')
    clickCount__lte = df_filters.NumberFilter(field_name="clickCount", lookup_expr='lte')

    convSales__gt = df_filters.NumberFilter(field_name="convSales", lookup_expr='gt')
    convSales__lt = df_filters.NumberFilter(field_name="convSales", lookup_expr='lt')
    convSales__gte = df_filters.NumberFilter(field_name="convSales", lookup_expr='gte')
    convSales__lte = df_filters.NumberFilter(field_name="convSales", lookup_expr='lte')
    
    convCount__gt = df_filters.NumberFilter(field_name="convCount", lookup_expr='gt')
    convCount__lt = df_filters.NumberFilter(field_name="convCount", lookup_expr='lt')
    convCount__gte = df_filters.NumberFilter(field_name="convCount", lookup_expr='gte')
    convCount__lte = df_filters.NumberFilter(field_name="convCount", lookup_expr='lte')
    
    class Meta:
        model = Creative
        fields = {
        }
