# Generated by Django 3.2.3 on 2021-05-20 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_goods_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='image',
            field=models.ImageField(upload_to='goods_images'),
        ),
    ]
