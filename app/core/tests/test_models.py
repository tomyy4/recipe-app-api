from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ test creating new user with email is successful"""
        email = 'test@gmail.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ test the email for the new user is normalized """
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(
            email=email,
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '12345')

    def test_create_new_superuser(self):
        """ test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email='email@email.com',
            password='1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)