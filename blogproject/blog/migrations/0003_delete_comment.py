# Generated by Django 2.2.13 on 2020-08-09 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200809_2136'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
