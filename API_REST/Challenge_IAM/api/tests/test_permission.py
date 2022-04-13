import pytest
import requests
import json
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class TestPermission(APITestCase):

    url = 'permissions/api/'

    @pytest.mark.django_db
    def test_permission_creation():

        PermissionError.objects.create(codename = 'can_print')

    @pytest.mark.django_db
    def test_get_permission(self):
        
        response = self.client.get(self.url)
        result = response.json()

        self.assertEqual(response.status_code,201)
    
   

    


    