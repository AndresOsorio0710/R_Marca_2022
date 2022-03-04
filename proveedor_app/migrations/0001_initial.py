# Generated by Django 3.2.4 on 2022-03-04 03:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tipo_identificacion', models.CharField(choices=[['C.C.', 'CEDULA DE CIUDADANIA'], ['C.E.', 'CEDULA DE EXTRANJERIA'], ['N.I.P.', 'NUMERO DE IDENTIFICACION PERSONAL'], ['N.I.T.', 'NUMERO DE IDENTIFICACION TRIBUTARIA'], ['T.I.', 'TARJETA DE IDENTIDAD'], ['P.A.P.', 'PASAPORTE']], max_length=7)),
                ('identificacion', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=80)),
                ('numero_telefonico', models.CharField(max_length=10)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('descripcion', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
