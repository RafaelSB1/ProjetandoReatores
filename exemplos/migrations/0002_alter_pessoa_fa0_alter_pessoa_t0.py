# Generated by Django 4.2.3 on 2023-07-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exemplos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='FA0',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='T0',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
    ]
