# Generated by Django 2.1 on 2020-01-03 09:59

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('KM', '0002_auto_20200103_0959'),
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publikasi',
            name='tagging',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='peningkatankapasitas',
            name='pembicara',
            field=models.ManyToManyField(to='KM.Staff'),
        ),
        migrations.AddField(
            model_name='peningkatankapasitas',
            name='sumber_dana',
            field=models.ManyToManyField(to='KM.Donor'),
        ),
        migrations.AddField(
            model_name='penelitian',
            name='PIC',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PIC_penelitian', to='KM.Staff', verbose_name='PIC Penelitian'),
        ),
        migrations.AddField(
            model_name='penelitian',
            name='principal_investigator',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='Principal_investigator', to='KM.Staff', verbose_name='Principal Investigator'),
        ),
        migrations.AddField(
            model_name='penelitian',
            name='sumber_dana',
            field=models.ManyToManyField(to='KM.Donor'),
        ),
        migrations.AddField(
            model_name='penelitian',
            name='tim',
            field=models.ManyToManyField(to='KM.Staff'),
        ),
        migrations.AddField(
            model_name='dokumenpeningkatan',
            name='Judul',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KM.PeningkatanKapasitas'),
        ),
        migrations.AddField(
            model_name='dokumenpenelitian',
            name='penelitian',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KM.Penelitian'),
        ),
    ]
