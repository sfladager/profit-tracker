# Generated by Django 4.1.4 on 2022-12-08 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('executions', '0002_execution_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='execution',
            name='commissions',
            field=models.FloatField(default=0),
        ),
    ]
