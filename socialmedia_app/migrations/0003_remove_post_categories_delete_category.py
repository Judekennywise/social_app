# Generated by Django 4.2 on 2023-04-21 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia_app', '0002_remove_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
