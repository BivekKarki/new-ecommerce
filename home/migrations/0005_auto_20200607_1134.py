# Generated by Django 3.0.6 on 2020-06-07 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200605_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='discounted_price',
            field=models.IntegerField(blank=True),
        ),
    ]