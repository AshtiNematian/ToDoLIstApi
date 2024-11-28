from django.db import models
from django.utils.timezone import now
from django.core.cache import cache
from django.urls import reverse
from datetime import datetime

class TaskManager(models.Manager):
    def get_cached_tasks(self, user=None):
        """
        بازگرداندن وظایف از کش یا ایجاد کش جدید. کش به‌صورت خاص برای هر کاربر ذخیره می‌شود.
        """
        cache_key = f"tasks_user_{user.id}" if user else "all_tasks"
        tasks = cache.get(cache_key)  # تلاش برای بازیابی از کش
        if not tasks:
            # در صورت نبودن داده در کش، بازیابی از پایگاه داده
            query = Task.objects.filter(user=user) if user else Task.objects.all()
            tasks = list(query)
            cache.set(cache_key, tasks, timeout=300)  # ذخیره در کش برای ۵ دقیقه
        return tasks

    def expire_task(self, user=None):
        """
        فیلتر کردن تسک‌های منقضی‌شده از کش یا دیتابیس.
        """
        tasks = self.get_cached_tasks(user)
        return [task for task in tasks if task.date_of_task < now()]

    def going_task(self, user=None):
        """
        فیلتر کردن تسک‌های جاری از کش یا دیتابیس.
        """
        tasks = self.get_cached_tasks(user)
        return [task for task in tasks if task.date_of_task >= now()]

class Task(models.Model):
    PRIORITY = [
        ('Necessary', 'Necessary'),
        ('Normal', 'Normal'),
        ('Poor Priority', 'Poor Priority'),
    ]
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=200, null=True, blank=True)
    priority = models.CharField(
        choices=PRIORITY, max_length=20, null=True, blank=True, default='Normal')
    date_of_task = models.DateTimeField()
    date_create = models.DateTimeField(default=datetime.now)
    active_task = models.BooleanField(default=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # تسک مربوط به کاربر
    slug = models.SlugField(unique=True, blank=True, null=True)

    objects = TaskManager()

    class Meta:
        ordering = ['date_of_task']

    @property
    def age(self):
        return self.date_of_task - self.date_create

    def get_absolute_url(self):
        return reverse('task', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title}'

    # مدیریت کش هنگام ذخیره یا حذف
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f"tasks_user_{self.user.id}")  # حذف کش تسک‌های کاربر
        cache.delete("all_tasks")  # حذف کش عمومی

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        cache.delete(f"tasks_user_{self.user.id}")  # حذف کش تسک‌های کاربر
        cache.delete("all_tasks")  # حذف کش عمومی
