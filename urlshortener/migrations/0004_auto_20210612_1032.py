# Generated by Django 3.2.4 on 2021-06-12 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0003_shortner_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shortner',
            name='created',
        ),
        migrations.RemoveField(
            model_name='shortner',
            name='updated',
        ),
    ]
