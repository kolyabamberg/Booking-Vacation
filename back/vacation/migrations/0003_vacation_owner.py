# Generated by Django 2.0.4 on 2018-04-13 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacation', '0002_auto_20180413_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacation',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='vacation', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
