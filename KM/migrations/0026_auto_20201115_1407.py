# Generated by Django 3.1 on 2020-11-15 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KM', '0025_auto_20201113_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publikasi',
            name='kategori',
            field=models.CharField(choices=[('0', 'Materi Pengetahuan HIV AIDS'), ('1', 'Laporan Penelitian'), ('2', 'Policy Brief'), ('3', 'Modul'), ('4', 'SOP'), ('5', 'Infografis'), ('6', 'Artikel Jurnal Nasional & Internasional'), ('7', 'Conference'), ('8', 'Regulasi'), ('9', 'buku'), ('10', 'Laporan Pelayanan Komunitas'), ('11', 'Lainnya')], max_length=2),
        ),
    ]
