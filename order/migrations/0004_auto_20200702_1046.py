# Generated by Django 3.0.6 on 2020-07-02 10:46

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_remove_address_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
