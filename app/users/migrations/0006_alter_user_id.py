# Generated by Django 4.0.2 on 2023-08-30 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_email_address_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]
