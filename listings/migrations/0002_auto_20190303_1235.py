# Generated by Django 2.0.4 on 2019-03-03 12:35

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]