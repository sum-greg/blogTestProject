# Generated by Django 3.1.7 on 2021-03-24 09:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainApp', '0015_auto_20210324_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='readers',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]