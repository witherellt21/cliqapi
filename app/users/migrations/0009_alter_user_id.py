# Generated by Django 4.0.2 on 2023-08-30 04:50

import app.users.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default=app.users.utils.generate_user_identifier, max_length=40, primary_key=True, serialize=False, unique=True),
        ),
    ]
