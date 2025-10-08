# posts/test_views.py
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from .models import Post

User = get_user_model()

class PostAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u1', password='pass')
        self.post = Post.objects.create(author=self.user, title='T1', content='C1')

    def test_list_posts(self):
        url = reverse('post-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_create_post_requires_auth(self):
        url = reverse('post-list')
        data = {'title': 'New', 'content': 'New content'}
        # unauthenticated should be 403 or 401 depending on permission classes
        resp = self.client.post(url, data)
        self.assertIn(resp.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))
        # authenticate and retry
        self.client.login(username='u1', password='pass')
        resp2 = self.client.post(url, data, format='json')
        self.assertEqual(resp2.status_code, status.HTTP_201_CREATED)

