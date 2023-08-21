from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Account(models.Model):
    name = models.CharField(max_length=255)
    adAccountNo = models.CharField(max_length=255, unique=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Campaign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    campaign_name = models.CharField(max_length=100)
    campaignNo = models.CharField(max_length=100, unique=True)
    cost = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True) 
    targetDate = models.DateField(blank=True, null=True)
    clickCount = models.IntegerField(blank=True, null=True)
    convCount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    convSales = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.campaignNo + ' - ' + self.campaign_name
    

class AdSet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='adsets')
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    adset_name = models.CharField(max_length=100)
    adSetNo = models.CharField(max_length=100, unique=True)
    cost = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True) 
    targetDate = models.DateField(blank=True, null=True)
    clickCount = models.IntegerField(blank=True, null=True)
    convCount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    convSales = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.adSetNo + ' - ' +  self.adset_name

    class Meta:
        verbose_name = 'Ad Set'
        verbose_name_plural = 'Ad Sets'
        
class Creative(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad_set = models.ForeignKey(AdSet, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    creative_name = models.CharField(max_length=100)
    creativeNo = models.CharField(max_length=100, unique=True)
    creativeType = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True) 
    targetDate = models.DateField(blank=True, null=True)
    clickCount = models.IntegerField(blank=True, null=True)
    convCount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    convSales = models.IntegerField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.creativeNo + ' - ' + self.creative_name
    
    
    class Meta:
        verbose_name = 'Creative'
        verbose_name_plural = 'Creatives'