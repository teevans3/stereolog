# Generated by Django 3.0.2 on 2020-07-20 21:51

import django.contrib.postgres.fields
import django.contrib.postgres.fields.hstore
from django.db import migrations, models
from django.contrib.postgres.operations import HStoreExtension



class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20200720_2148'),
    ]

    operations = [
        HStoreExtension(),
        migrations.AlterField(
            model_name='list',
            name='albums_info',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.hstore.HStoreField(), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='list',
            name='title_slug',
            field=models.SlugField(null=True),
        ),
    ]
