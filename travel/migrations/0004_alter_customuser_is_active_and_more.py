# Generated by Django 5.1.6 on 2025-02-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_customuser_is_verified_alter_customuser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_verified',
            field=models.BooleanField(default=True),
        ),
    ]
