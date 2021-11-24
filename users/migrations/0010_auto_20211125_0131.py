# Generated by Django 2.2.5 on 2021-11-24 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20211123_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, default=False, max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='stu_id',
            field=models.IntegerField(blank=True, default=False),
        ),
    ]
