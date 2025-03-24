from django.test import TestCase,Client
from rest_framework.test import APIClient,APITestCase
from .models import CustomUser
# Create your tests here.

class TestCustomUser(TestCase):
     def test_model(self):
          
          customuser = CustomUser(
               role="blogger",
               username = "user",
               first_name = "user",
               last_name = "some",
               email = "user@mail.com",
               password = 'qwerty@123'
          )
          self.assertEqual(customuser.role,'blogger')
          self.assertEqual(customuser.username,'user1')

class TestAuthor(TestCase):
     def setUp(self):
          self.client = Client()
          return super().setUp()  

     def test_create_author(self):
          pass
