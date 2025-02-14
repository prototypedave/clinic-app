from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class AdminRegistrationTest(TestCase):
    """
        Set invalid and valid credentials for testing
    """
    def setUp(self):
        self.client = APIClient()
        self.valid_payload = {
            "email": "admin@example.com",
            "first_name": "Admin",
            "last_name": "User",
            "password": "SecurePassword123",
        }
        self.invalid_payload = {
            "email": "",  
            "first_name": "Admin",
            "last_name": "User",
            "password": "Short1",  
        }

    def test_admin_registration_success(self):
        """
        Test registering an admin with valid data.
        """
        response = self.client.post(reverse('admin-registration'), self.valid_payload, format='json')
        print("Response Data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "Admin registered successfully!")
        from users.models import User
        self.assertTrue(User.objects.filter(email=self.valid_payload["email"]).exists())