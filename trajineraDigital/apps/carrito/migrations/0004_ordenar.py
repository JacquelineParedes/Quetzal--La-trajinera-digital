# Generated by Django 3.0.3 on 2020-06-07 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20200606_2127'),
        ('carrito', '0003_auto_20200606_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordenar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Alimento')),
            ],
        ),
    ]
