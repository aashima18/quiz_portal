# Generated by Django 2.2.7 on 2019-11-07 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191106_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='emails',
        ),
    ]
