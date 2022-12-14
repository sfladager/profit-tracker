# Generated by Django 4.1.4 on 2022-12-14 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0003_alter_trade_mistakes'),
        ('daily_sessions', '0003_remove_session_session_trades_session_session_trades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='session_trades',
            field=models.ManyToManyField(related_name='daily_sessions', to='trades.trade'),
        ),
    ]
