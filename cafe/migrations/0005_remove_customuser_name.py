# Generated by Django 3.2.8 on 2021-10-24 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0004_auto_20211024_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='name',
        ),
    ]
