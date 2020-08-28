# Generated by Django 2.2 on 2020-01-27 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KM', '0008_jabatan_kepakaran_peminatan_posisi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='kepakaran',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='KM.Kepakaran'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='peminatan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='KM.Peminatan'),
        ),
    ]
