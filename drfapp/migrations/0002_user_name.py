# Generated by Django 4.0.2 on 2022-03-01 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]