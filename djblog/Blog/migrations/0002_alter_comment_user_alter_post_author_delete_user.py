# Generated by Django 4.0.3 on 2022-03-21 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
