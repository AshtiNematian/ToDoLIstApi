# Generated by Django 4.2.16 on 2024-11-27 17:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('priority', models.CharField(blank=True, choices=[('Necessary', 'Necessary'), ('Normal', 'Normal'), ('Poor Priority', 'Poor Priority')], default='Normal', max_length=20, null=True)),
                ('date_of_task', models.DateTimeField()),
                ('date_create', models.DateTimeField(default=datetime.datetime.now)),
                ('active_task', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_of_task'],
            },
        ),
    ]
