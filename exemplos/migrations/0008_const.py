# Generated by Django 4.2.3 on 2023-08-07 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exemplos', '0007_remove_dados_v'),
    ]

    operations = [
        migrations.CreateModel(
            name='Const',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deltaH1', models.FloatField()),
                ('deltaH2', models.FloatField()),
                ('CpA', models.FloatField()),
                ('cpB', models.FloatField()),
                ('cpC', models.FloatField()),
                ('Ua', models.FloatField()),
                ('Ta', models.FloatField()),
                ('CT0', models.FloatField()),
            ],
        ),
    ]
