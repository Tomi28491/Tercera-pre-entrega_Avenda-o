# Generated by Django 5.0.1 on 2024-02-03 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0003_rename_contraseña_crear_cuenta_contrasenia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crear_cuenta',
            old_name='contrasenia',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='crear_cuenta',
            old_name='nombre',
            new_name='usuario',
        ),
    ]
