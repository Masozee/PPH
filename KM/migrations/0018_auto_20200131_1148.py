# Generated by Django 2.1.7 on 2020-01-31 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KM', '0017_auto_20200131_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peningkatankapasitasstaff',
            name='materi',
            field=models.FileField(blank=True, null=True, upload_to='KM/staff/peningkatan/materi/'),
        ),
    ]
