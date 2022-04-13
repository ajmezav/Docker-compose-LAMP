import pytest
import requests
import json
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


client = APIClient()

@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create_user(
        username = 'Estevan',
        email = 'dragonleon88@gmail.com',
        password = '12345'
    )
    assert user.username == "Estevan"

@pytest.mark.django_db
def test_superuser_creation():
    user = User.objects.create_superuser(
        username = 'Estevan',
        email = 'dragonleon88@gmail.com',
        password = '12345'
    )
    assert user.is_superuser

@pytest.mark.django_db
def test_staffuser_creation():
    user = User.objects.create_user(
        username = 'Estevan',
        email = 'dragonleon88@gmail.com',
        password = '12345',
        is_staff = True
    )
    assert user.is_staff


