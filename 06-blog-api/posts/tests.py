from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post


class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@gmail.com",
            password="secret",
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title="A Good Title",
            body="Nice body content",
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "A Good Title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(str(self.post), "A Good Title")
