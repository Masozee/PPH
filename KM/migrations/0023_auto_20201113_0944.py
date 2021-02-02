# Generated by Django 3.1 on 2020-11-13 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KM', '0022_remove_publikasi_rak'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publikasi',
            name='tema',
            field=models.CharField(blank=True, choices=[('HIV AIDS', 'HIV AIDS'), ('Publikasi', 'Publikasi'), ('Regulasi', 'Regulasi'), ('Penelitian', 'Penelitian'), ('Pelayanan Komunitas', 'Pelayanan Komiunitas')], default='HIV AIDS', max_length=20, null=True, verbose_name='Rak'),
        ),
    ]
