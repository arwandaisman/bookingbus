# Generated by Django 2.2 on 2020-12-08 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0005_databus_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='databus',
            name='jml_bus',
            field=models.IntegerField(default=None),
        ),
    ]