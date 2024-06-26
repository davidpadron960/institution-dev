# Generated by Django 5.0.2 on 2024-04-22 16:20

import django.core.validators
import django.db.models.deletion
import utils.validates.validates
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeInstitution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(3), utils.validates.validates.validate_letters_numbers_and_spaces], verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo de institución',
                'verbose_name_plural': 'Tipos de instituciones',
            },
        ),
        migrations.CreateModel(
            name='TypeService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(3), utils.validates.validates.validate_letters_numbers_and_spaces], verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo de servicios',
                'verbose_name_plural': 'Tipos de servicios',
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('mision', models.TextField()),
                ('vision', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('telephone_number', models.CharField(max_length=20)),
                ('active', models.BooleanField(default=True)),
                ('in_time', models.TimeField(verbose_name='Hora inicial')),
                ('out_time', models.TimeField(verbose_name='Hora final')),
                ('init_day_of_week', models.IntegerField(choices=[(0, 'Domingo'), (1, 'Lunes'), (2, 'Martes'), (3, 'Miércoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sábado')], default=0, help_text='Selecciona el dia de la semana.', verbose_name='Dia inicial del servicio')),
                ('end_day_of_week', models.IntegerField(choices=[(0, 'Domingo'), (1, 'Lunes'), (2, 'Martes'), (3, 'Miércoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sábado')], default=6, help_text='Selecciona el dia de la semana.', verbose_name='Dia final del servicio')),
                ('image', models.ImageField(upload_to='institucion/', verbose_name='Imagen')),
                ('type_institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.typeinstitution', verbose_name='Tipo de institución')),
            ],
            options={
                'verbose_name': 'Institución',
                'verbose_name_plural': 'Instituciones',
            },
        ),
        migrations.CreateModel(
            name='InstitutionService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(3), utils.validates.validates.validate_letters_numbers_and_spaces], verbose_name='Nombre')),
                ('description', models.TextField(max_length=255, validators=[django.core.validators.MinLengthValidator(3), utils.validates.validates.validate_text], verbose_name='Descripción')),
                ('in_time', models.TimeField(verbose_name='Hora inicial')),
                ('out_time', models.TimeField(verbose_name='Hora final')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('init_day_of_week', models.CharField(choices=[('Domingo', 'Domingo'), ('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miércoles', 'Miércoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sábado', 'Sábado')], default='Domingo', help_text='Selecciona el dia de la semana.', max_length=9, verbose_name='Dia inicial del servicio')),
                ('end_day_of_week', models.CharField(choices=[('Domingo', 'Domingo'), ('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miércoles', 'Miércoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sábado', 'Sábado')], default='Domingo', help_text='Selecciona el dia de la semana.', max_length=9, verbose_name='Dia final del servicio')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.institution', verbose_name='Institución')),
                ('type_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.typeservice', verbose_name='Tipo de servicio')),
            ],
            options={
                'verbose_name': 'Servicio de institución',
                'verbose_name_plural': 'Servicios de instituciones',
            },
        ),
    ]
