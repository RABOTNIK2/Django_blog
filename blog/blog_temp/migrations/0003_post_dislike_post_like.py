# Generated by Django 5.0.6 on 2024-06-18 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_temp', '0002_alter_post_images_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislike',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
