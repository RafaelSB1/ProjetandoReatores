# Generated by Django 4.2.3 on 2023-08-04 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exemplos', '0006_dados_v'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dados',
            name='V',
        ),
    ]