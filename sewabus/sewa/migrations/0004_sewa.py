# Generated by Django 2.2 on 2020-12-17 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sewa', '0003_delete_pkl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sewa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pemesan', models.CharField(max_length=240, null=True)),
                ('alamat', models.CharField(max_length=100, null=True)),
                ('intstalasi', models.CharField(max_length=100, null=True)),
                ('jabatan', models.CharField(max_length=100, null=True)),
                ('no_hp', models.IntegerField(null=True)),
            ],
        ),
    ]
