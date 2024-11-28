from django.test import TestCase
from django.utils.timezone import now, timedelta
from django.contrib.auth.models import User
from .models import Task




class TaskManagerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        Task.objects.create(title="Task 1", date_of_task=now() + timedelta(days=1), user=self.user)
        Task.objects.create(title="Task 2", date_of_task=now() - timedelta(days=1), user=self.user)

    def test_get_cached_tasks(self):
        tasks = Task.objects.get_cached_tasks(user=self.user)
        self.assertEqual(len(tasks), 2)

    def test_expire_task(self):
        expired_tasks = Task.objects.expire_task(user=self.user)
        self.assertEqual(len(expired_tasks), 1)  # یک تسک منقضی شده است

    def test_going_task(self):
        going_tasks = Task.objects.going_task(user=self.user)
        self.assertEqual(len(going_tasks), 1)  # یک تسک در آینده است






