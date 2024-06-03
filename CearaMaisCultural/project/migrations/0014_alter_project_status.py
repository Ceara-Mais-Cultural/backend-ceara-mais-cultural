# Generated by Django 4.2.13 on 2024-06-03 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_alter_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('pending', 'Pendente'), ('approved', 'Aprovado'), ('declined', 'Recusado'), ('waiting', 'Esperando Documentação')], default='pending', max_length=8),
        ),
    ]
