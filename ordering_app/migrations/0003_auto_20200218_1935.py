# Generated by Django 3.0.3 on 2020-02-18 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering_app', '0002_auto_20200218_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='name',
            field=models.CharField(choices=[('O', 'One Size'), ('S', 'Small'), ('L', 'Large')], max_length=1),
        ),
        migrations.AlterField(
            model_name='topping',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
