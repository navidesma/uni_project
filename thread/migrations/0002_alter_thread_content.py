# Generated by Django 4.2.1 on 2023-05-16 12:08

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
