# Generated by Django 3.0.2 on 2020-01-26 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200126_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='giver',
            field=models.TextField(choices=[('prapor', 'Prapor'), ('therapist', 'Therapist'), ('skier', 'Skier'), ('peacekeeper', 'Peacekeeper'), ('mechanic', 'Mechanic'), ('ragman', 'Ragman'), ('jaeger', 'Jaeger'), ('fence', 'Fence')], default='prapor'),
        ),
        migrations.AlterField(
            model_name='task',
            name='map',
            field=models.TextField(choices=[('customs', 'Customs'), ('factory', 'Factory'), ('woods', 'Woods'), ('interchange', 'Interchange'), ('reserve', 'Reserve'), ('shoreline', 'Shoreline'), ('labs', 'Labs')], default='customs'),
        ),
    ]
