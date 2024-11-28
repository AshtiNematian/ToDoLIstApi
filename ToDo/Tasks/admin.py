from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'priority', 'date_of_task', 'active_task')
    list_filter = ('priority', 'active_task', 'date_of_task')
    search_fields = ('title', 'description', 'categories')
    prepopulated_fields = {'slug': ('title',)}
