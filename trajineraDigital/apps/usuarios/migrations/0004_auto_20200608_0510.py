# Generated by Django 3.0.3 on 2020-06-08 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20200608_0256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administrador',
            name='tipo_usuario',
        ),
        migrations.RemoveField(
            model_name='repartidor',
            name='tipo_usuario',
        ),
    ]
