# Generated by Django 4.0.1 on 2022-05-18 23:54

from django.db import migrations, models
import django.db.models.deletion
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=sqlalchemy.sql.expression.true, serialize=False, verbose_name='Id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('patente', models.CharField(max_length=6, primary_key=sqlalchemy.sql.expression.true, serialize=False, verbose_name='Patente')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca vehiculo')),
                ('modelo', models.CharField(blank=sqlalchemy.sql.expression.true, max_length=20, null=sqlalchemy.sql.expression.true, verbose_name='Modelo')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]
