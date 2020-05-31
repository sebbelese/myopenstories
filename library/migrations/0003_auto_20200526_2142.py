# Generated by Django 3.0.5 on 2020-05-26 19:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0002_story_uploader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='downvotes',
            field=models.ManyToManyField(blank=True, related_name='downvotes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='story',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]