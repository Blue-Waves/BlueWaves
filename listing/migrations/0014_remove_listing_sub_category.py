# Generated by Django 3.1 on 2021-04-24 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0013_auto_20210422_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='sub_category',
        ),
    ]
