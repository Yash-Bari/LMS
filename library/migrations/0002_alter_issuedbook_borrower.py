# Generated by Django 3.2.18 on 2024-03-13 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='borrower',
            field=models.CharField(max_length=100),
        ),
    ]
