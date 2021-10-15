from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.test import TestCase
from .models import *
from django.contrib import auth
# Create your tests here.

user = UserInfo.objects.filter(username='syx', )
if user:
    print(1)
else:
    print(2)