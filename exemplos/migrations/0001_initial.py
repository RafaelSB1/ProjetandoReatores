# Generated by Django 4.2.3 on 2023-07-26 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FA0', models.DecimalField(decimal_places=4, max_digits=10)),
                ('FB0', models.DecimalField(decimal_places=4, max_digits=10)),
                ('FC0', models.DecimalField(decimal_places=4, max_digits=10)),
                ('T0', models.DecimalField(decimal_places=2, max_digits=10)),
                ('CT0', models.DecimalField(decimal_places=4, max_digits=10)), 
            ],
        ),
    ]