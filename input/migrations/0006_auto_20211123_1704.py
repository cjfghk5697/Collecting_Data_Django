# Generated by Django 2.2.5 on 2021-11-23 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0005_auto_20211123_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='file',
            field=models.ImageField(null=True, upload_to='cat_photos'),
        ),
    ]