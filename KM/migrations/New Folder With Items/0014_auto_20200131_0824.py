# Generated by Django 2.1.7 on 2020-01-31 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KM', '0013_peningkatankapasitas_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peningkatankapasitas_staff',
            name='laporan_kegiatan',
            field=models.FileField(blank=True, null=True, upload_to='KM/staff/peningkatan/laporan/'),
        ),
        migrations.AlterField(
            model_name='peningkatankapasitas_staff',
            name='materi',
            field=models.FileField(upload_to='KM/staff/peningkatan/materi/'),
        ),
        migrations.RemoveField(
            model_name='peningkatankapasitas_staff',
            name='pembicara',
        ),
        migrations.AddField(
            model_name='peningkatankapasitas_staff',
            name='pembicara',
            field=models.TextField(blank=True),
        ),
    ]
