# Generated by Django 3.2.3 on 2021-05-26 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='nome',
            field=models.CharField(help_text='Nome do departamento', max_length=70),
        ),
    ]
