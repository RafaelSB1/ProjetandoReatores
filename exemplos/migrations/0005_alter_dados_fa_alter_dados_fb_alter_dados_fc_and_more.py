# Generated by Django 4.2.3 on 2023-08-03 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exemplos', '0004_dados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados',
            name='FA',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='dados',
            name='FB',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='dados',
            name='FC',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='dados',
            name='T',
            field=models.FloatField(),
        ),
    ]
