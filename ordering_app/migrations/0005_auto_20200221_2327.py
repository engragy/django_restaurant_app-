# Generated by Django 3.0.3 on 2020-02-21 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering_app', '0004_food_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(null=True, upload_to='food'),
        ),
    ]
