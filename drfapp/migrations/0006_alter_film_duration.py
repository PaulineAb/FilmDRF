# Generated by Django 4.0.2 on 2022-03-02 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfapp', '0005_film_userlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='duration',
            field=models.CharField(max_length=100),
        ),
    ]
