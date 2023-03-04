from django.contrib.auth.models import User
from django.test import TestCase

from .models import Message, Thread

# Create your tests here.
class ThreadTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user1',None,'test1234')
        self.user2 = User.objects.create_user('user2',None,'test1234')
        self.thread = Thread.objects.create()

    def test_add_users_to_thread(self):
        self.thread.users.add(self.user1,self.user2)
        self.assertEqual(self.thread.users.all(),2)

    def test_filter_threads_by_users(self):
        self.thread.users.add(self.user1,self.user2)
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(self.thread,threads[0])

    def test_filter_non_existent_threads(self):
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(len(threads),0)