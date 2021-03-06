# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 10:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_polisi', models.CharField(max_length=100)),
                ('jenis', models.CharField(max_length=100)),
                ('kapasitas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Peminjam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('bagian_jurusan', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PeminjamanKendaraan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bukti_transfer', models.IntegerField()),
                ('no_surat', models.CharField(max_length=100)),
                ('tanggal_surat', models.DateTimeField()),
                ('tanggal_booking', models.DateTimeField()),
                ('odometer_sebelum', models.FloatField()),
                ('odometer_sesudah', models.FloatField()),
                ('acara', models.CharField(max_length=100)),
                ('tujuan', models.CharField(max_length=100)),
                ('tanggal_pemakaian', models.DateTimeField()),
                ('tanggal_pengembalian', models.DateTimeField()),
                ('tempat_berkumpul', models.CharField(max_length=100)),
                ('keterangan', models.CharField(max_length=200)),
                ('mobil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peminjaman.Mobil')),
                ('peminjam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peminjaman.Peminjam')),
            ],
        ),
        migrations.CreateModel(
            name='Supir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TeleponPeminjam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_telepon', models.CharField(max_length=100)),
                ('peminjam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peminjaman.Peminjam')),
            ],
        ),
        migrations.CreateModel(
            name='TeleponSupir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_telepon', models.CharField(max_length=100)),
                ('supir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peminjaman.Supir')),
            ],
        ),
        migrations.AddField(
            model_name='peminjamankendaraan',
            name='supir',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peminjaman.Supir'),
        ),
    ]
