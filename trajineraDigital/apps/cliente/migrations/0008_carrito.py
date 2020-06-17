# Generated by Django 3.0.3 on 2020-06-17 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_remove_alimento_cantidad'),
        ('cliente', '0007_auto_20200608_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('alimentos', models.ManyToManyField(blank=True, null=True, to='menu.Alimento')),
            ],
        ),
    ]