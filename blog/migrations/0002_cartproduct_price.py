# Generated by Django 3.2.3 on 2021-05-17 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
