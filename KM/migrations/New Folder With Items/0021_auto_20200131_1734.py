# Generated by Django 2.1.7 on 2020-01-31 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KM', '0020_auto_20200131_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publikasi_staff',
            name='judul',
            field=models.CharField(max_length=200),
        ),
    ]
