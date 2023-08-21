from rest_framework import serializers
from .models import Campaign, AdSet, Creative, Account


class CreativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creative
        fields = '__all__'

class AdSetSerializer(serializers.ModelSerializer):

    creatives = CreativeSerializer(many=True, read_only=True)
    class Meta:
        model = AdSet
        fields = '__all__'
        
class CampaignSerializer(serializers.ModelSerializer):

    adsets = AdSetSerializer(many=True, read_only=True)
    class Meta:
        model = Campaign
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
