# Generated by Django 3.2.6 on 2021-09-19 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_orderdetail_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
