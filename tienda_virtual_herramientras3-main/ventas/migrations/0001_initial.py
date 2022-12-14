# Generated by Django 4.1.3 on 2022-11-14 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.TextField(max_length=30)),
                ('tipo_doc', models.CharField(max_length=30)),
                ('num_doc', models.IntegerField(default=0)),
                ('correo', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=30)),
                ('depto', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
                ('telefono', models.IntegerField(default=0)),
                ('total_venta', models.DecimalField(decimal_places=3, max_digits=50)),
            ],
        ),
    ]
