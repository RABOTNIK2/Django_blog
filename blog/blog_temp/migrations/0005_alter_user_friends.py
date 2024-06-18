# Generated by Django 5.0.6 on 2024-06-18 09:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_temp', '0004_rename_fields_user_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='friend_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
