# Generated by Django 2.1.7 on 2020-01-31 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('KM', '0014_auto_20200131_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='peningkatankapasitas_staff',
            name='author',
            field=models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
