# Generated by Django 4.2.1 on 2023-06-01 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pengguna',
            name='telpon',
            field=models.IntegerField(null=True),
        ),
    ]