# Generated by Django 4.2.1 on 2023-05-15 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0005_searchrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchrequest',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='searchrequest',
            name='user_request',
            field=models.TextField(default='NONE', null=True),
        ),
    ]