# Generated by Django 3.1.7 on 2021-04-24 06:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('email', models.TextField(max_length=255)),
                ('password', models.TextField(max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
