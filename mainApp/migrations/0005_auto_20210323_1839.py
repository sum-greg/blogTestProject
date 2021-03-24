# Generated by Django 3.1.7 on 2021-03-23 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainApp', '0004_delete_extendeduser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userblogsubscription',
            name='blog_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.blog'),
        ),
        migrations.AlterField(
            model_name='userblogsubscription',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]