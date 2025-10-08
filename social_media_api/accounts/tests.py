# accounts/tests.py (example)
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class FollowTests(APITestCase):
    def setUp(self):
        self.u1 = User.objects.create_user(username='a', password='pass')
        self.u2 = User.objects.create_user(username='b', password='pass')

    def test_follow_unfollow(self):
        self.client.login(username='a', password='pass')
        url = reverse('follow-user', args=[self.u2.pk])
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(self.u1.is_following(self.u2))

        url_un = reverse('unfollow-user', args=[self.u2.pk])
        resp = self.client.post(url_un)
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(self.u1.is_following(self.u2))

