# Generated by Django 3.1.7 on 2021-05-04 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210504_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic_url',
            field=models.TextField(default='https://i.stack.imgur.com/l60Hf.png', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]
