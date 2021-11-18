# Generated by Django 2.2.5 on 2021-11-18 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='stu_id',
            field=models.IntegerField(null=True),
        ),
    ]
