# Generated by Django 2.2 on 2020-05-13 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('KM', '0016_personalevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalevent',
            name='owner',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
