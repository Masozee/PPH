# Generated by Django 3.1 on 2020-11-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KM', '0026_auto_20201115_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publikasi',
            name='tema',
            field=models.CharField(blank=True, choices=[('0', 'Informasi HIV AIDS'), ('1', 'Publikasi'), ('2', 'Regulasi'), ('3', 'Penelitian'), ('4', 'Pelayanan Komunitas')], default='HIV AIDS', max_length=1, null=True, verbose_name='Rak'),
        ),
    ]
