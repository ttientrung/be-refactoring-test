import random
from faker import Faker
from django.contrib.auth import get_user_model
from .models import Account, Campaign, AdSet, Creative

fake = Faker()
User = get_user_model()

def generate_test_data():
    # Create 4 accounts
    accounts = []
    for _ in range(4):
        account = Account.objects.create(
            name=fake.company(),
            adAccountNo=fake.unique.random_number(digits=5),
            user=User.objects.first()
        )
        accounts.append(account)

    # Create 26 campaigns
    campaigns = []
    for _ in range(26):
        campaign = Campaign.objects.create(
            user=User.objects.first(),
            account=random.choice(accounts),
            campaign_name=fake.sentence(),
            campaignNo=fake.unique.random_number(digits=6),
            cost=random.uniform(100, 10000),
            targetDate=fake.date(),
            clickCount=random.randint(100, 1000),
            convCount=random.uniform(10, 100),
            convSales=random.uniform(1000, 10000)
        )
        campaigns.append(campaign)

    # Create 300 adsets
    adsets = []
    for _ in range(300):
        adset = AdSet.objects.create(
            user=User.objects.first(),
            campaign=random.choice(campaigns),
            account=random.choice(accounts),
            adset_name=fake.sentence(),
            adSetNo=fake.unique.random_number(digits=6),
            cost=random.uniform(100, 10000),
            targetDate=fake.date(),
            clickCount=random.randint(100, 1000),
            convCount=random.uniform(10, 100),
            convSales=random.uniform(1000, 10000)
        )
        adsets.append(adset)

    # Create 996 creatives
    for _ in range(996):
        Creative.objects.create(
            user=User.objects.first(),
            ad_set=random.choice(adsets),
            account=random.choice(accounts),
            creative_name=fake.sentence(),
            creativeNo=fake.unique.random_number(digits=6),
            creativeType=random.choice(['Type 1', 'Type 2', 'Type 3']),
            cost=random.uniform(100, 10000),
            targetDate=fake.date(),
            clickCount=random.randint(100, 1000),
            convCount=random.uniform(10, 100),
            convSales=random.uniform(1000, 10000)
        )

generate_test_data()