# Generated by Django 5.0.4 on 2024-04-06 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1994-04-06'),
            preserve_default=False,
        ),
    ]
