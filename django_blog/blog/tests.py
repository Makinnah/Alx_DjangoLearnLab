# blog/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment

class CommentTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='u1', password='pass1')
        self.user2 = User.objects.create_user(username='u2', password='pass2')
        self.post = Post.objects.create(title='P', content='C', author=self.user1)

    def test_create_comment_authenticated(self):
        self.client.login(username='u2', password='pass2')
        url = reverse('comment-create', kwargs={'post_pk': self.post.pk})
        response = self.client.post(url, {'content': 'Nice post!'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Comment.objects.filter(post=self.post, author=self.user2, content='Nice post!').exists())

    def test_create_comment_unauthenticated_redirects(self):
        url = reverse('comment-create', kwargs={'post_pk': self.post.pk})
        response = self.client.post(url, {'content': 'Hi'})
        # should redirect to login
        self.assertNotEqual(response.status_code, 200)

