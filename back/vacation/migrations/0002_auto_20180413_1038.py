# Generated by Django 2.0.4 on 2018-04-13 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacation',
            old_name='linenos',
            new_name='confirm',
        ),
        migrations.RemoveField(
            model_name='vacation',
            name='code',
        ),
        migrations.RemoveField(
            model_name='vacation',
            name='highlighted',
        ),
        migrations.RemoveField(
            model_name='vacation',
            name='language',
        ),
        migrations.RemoveField(
            model_name='vacation',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='vacation',
            name='style',
        ),
        migrations.RemoveField(
            model_name='vacation',
            name='title',
        ),
        migrations.AddField(
            model_name='vacation',
            name='comments',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='vacation',
            name='end',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacation',
            name='start',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]
