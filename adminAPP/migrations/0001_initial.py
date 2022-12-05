# Generated by Django 4.1.3 on 2022-11-21 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InsmoOficina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.IntegerField(max_length=50)),
                ('Tipo', models.CharField(choices=[['Papeleria', 'Papeleria'], ['Muebleria', 'Muebleria'], ['Sillas', 'Sillas'], ['Lapices', 'Lapices'], ['Otros', 'Otros']], max_length=100)),
                ('Ubicacion', models.CharField(max_length=100)),
                ('Stock', models.IntegerField(max_length=50)),
                ('Descripcion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='InsumoComputacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.IntegerField(max_length=50)),
                ('Tipo', models.CharField(choices=[['Monitor', 'Monitor'], ['Desktop', 'Desktop'], ['Laptop', 'Laptop'], ['Mouse', 'Mouse'], ['Teclados', 'Teclados'], ['Impresoras', 'Impresoras'], ['perisfericos', 'perisfericos'], ['Otros', 'Otros']], max_length=100)),
                ('Marca', models.CharField(max_length=100)),
                ('Fecha_de_adquisicion', models.DateField(max_length=100)),
                ('Stock', models.IntegerField(max_length=50)),
                ('Descripcion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroVehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.IntegerField(max_length=50)),
                ('Tipo', models.CharField(choices=[['Papeleria', 'Papeleria'], ['Muebleria', 'Muebleria'], ['Sillas', 'Sillas'], ['Lapices', 'Lapices'], ['Otros', 'Otros']], max_length=100)),
                ('Patente', models.IntegerField(max_length=100)),
                ('Numero_de_chasis', models.IntegerField(max_length=50)),
                ('Marca', models.CharField(max_length=100)),
                ('Modelo', models.CharField(max_length=100)),
                ('Ultima_revision', models.DateField(max_length=100)),
                ('Proxima_revision', models.DateField(max_length=100)),
                ('Observaciones', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Perfil', models.CharField(choices=[['Administrador', 'Administrador'], ['Insumos Computacionales', 'Insumos Computacionales'], ['Insumos Oficina', 'Insumos Oficina'], ['Registro Vehiculos', 'Registro Vehiculos']], max_length=100)),
                ('Nombre_de_usuario', models.CharField(max_length=100)),
                ('Nombre_completo', models.CharField(max_length=100)),
                ('Correo_electronico', models.EmailField(max_length=100)),
            ],
        ),
    ]
