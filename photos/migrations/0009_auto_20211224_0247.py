# Generated by Django 2.2.5 on 2021-12-23 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0008_auto_20211224_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.ImageField(null=True, upload_to='cat_photos'),
        ),
    ]
