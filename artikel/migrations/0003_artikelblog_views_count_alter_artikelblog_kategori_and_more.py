# Generated by Django 5.0.1 on 2025-06-27 19:11

import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0002_rename_artikel_artikelblog_alter_artikelblog_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikelblog',
            name='views_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='artikelblog',
            name='kategori',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artikelblog', to='artikel.kategori'),
        ),
        migrations.AlterField(
            model_name='artikelblog',
            name='konten',
            field=django_ckeditor_5.fields.CKEditor5Field(default='Konten belum tersedia', verbose_name='Text'),
        ),
    ]
