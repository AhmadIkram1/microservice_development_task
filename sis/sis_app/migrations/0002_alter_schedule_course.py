# Generated by Django 5.1.1 on 2024-10-06 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='course',
            field=models.CharField(max_length=100),
        ),
    ]
