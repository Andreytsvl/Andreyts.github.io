# Generated by Django 5.1.1 on 2024-11-01 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0003_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
