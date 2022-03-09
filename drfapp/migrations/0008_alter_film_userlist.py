# Generated by Django 4.0.2 on 2022-03-02 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drfapp', '0007_alter_film_userlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='userlist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='drfapp.user'),
            preserve_default=False,
        ),
    ]