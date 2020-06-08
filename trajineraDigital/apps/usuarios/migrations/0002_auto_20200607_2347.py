# Generated by Django 3.0.3 on 2020-06-07 23:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='administrador', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.RemoveField(
            model_name='repartidor',
            name='apellidos',
        ),
        migrations.RemoveField(
            model_name='repartidor',
            name='contrasena',
        ),
        migrations.RemoveField(
            model_name='repartidor',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='repartidor',
            name='nombre',
        ),
        migrations.AddField(
            model_name='repartidor',
            name='telefono',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^(55)\\d{8}', 'El número debe estár en formato LADA.')]),
        ),
        migrations.AddField(
            model_name='repartidor',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='repartidor', to=settings.AUTH_USER_MODEL),
        ),
    ]
