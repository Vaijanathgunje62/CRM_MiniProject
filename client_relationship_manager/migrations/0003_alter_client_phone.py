# Generated by Django 4.1.4 on 2022-12-17 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_relationship_manager', '0002_alter_client_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
