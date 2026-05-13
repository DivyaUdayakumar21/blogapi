from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.
from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123'
        )
        testuser1.save()

        testpost = Post.objects.create(
            title = 'django', author=testuser1, body='body content ...'
        )
        testpost.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        title = f'{post.title}'
        author = f'{post.author}'
        body = f'{post.body}'
        self.assertEqual(title, 'django')
        self.assertEqual(author, 'testuser1')
        self.assertEqual(body, 'body content ...')
