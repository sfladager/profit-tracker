# Generated by Django 4.1.4 on 2022-12-08 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_date', models.DateField()),
                ('session_rating', models.PositiveIntegerField()),
                ('session_notes', models.TextField()),
                ('owner_of_session', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dail_sessions', to=settings.AUTH_USER_MODEL)),
                ('session_trades', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='daily_sessions', to='trades.trade')),
            ],
        ),
    ]