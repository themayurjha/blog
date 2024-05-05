from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Post

class PostAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client.force_authenticate(user=self.user)

    def test_create_post(self):
        url = '/posts/'
        data = {'title': 'Test Post', 'content': 'This is a test post.', 'author': self.user.id}
        # Test creating a new post
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Test creating a post without required fields
        response = self.client.post(url, {'content': 'This is a test post.'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_posts(self):
        url = '/posts/'
        # Test retrieving all posts
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_post(self):
        post = Post.objects.create(title='Test Post', content='This is a test post.', author=self.user)
        url = f'/posts/{post.id}/'
        # Test retrieving a single post by ID
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test retrieving a non-existent post
        response = self.client.get('/posts/999999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_post(self):
        post = Post.objects.create(title='Test Post', content='This is a test post.', author=self.user)
        url = f'/posts/{post.id}/'
        # Test updating an existing post
        updated_data = {'title': 'Updated Post', 'content': 'This is an updated post.', 'author': self.user.id}
        response = self.client.put(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test updating a non-existent post
        response = self.client.put('/posts/999999/', updated_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_post(self):
        post = Post.objects.create(title='Test Post', content='This is a test post.', author=self.user)
        url = f'/posts/{post.id}/'
        # Test deleting an existing post
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Test deleting a non-existent post
        response = self.client.delete('/posts/999999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
