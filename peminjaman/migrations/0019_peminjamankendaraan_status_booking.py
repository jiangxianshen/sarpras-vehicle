# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-29 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peminjaman', '0018_peminjamankendaraan_metode_transfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='peminjamankendaraan',
            name='status_booking',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]