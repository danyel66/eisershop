# Generated by Django 3.0.6 on 2020-07-02 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20200702_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='number',
        ),
    ]
