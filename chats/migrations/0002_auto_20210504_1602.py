# Generated by Django 3.1.7 on 2021-05-04 16:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chats',
            name='id',
            field=models.UUIDField(default=uuid.UUID('58260e78-b638-4fdb-8d4b-c4068f969cdd'), primary_key=True, serialize=False, unique=True),
        ),
    ]