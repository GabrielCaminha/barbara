# Generated by Django 5.1.1 on 2024-10-28 00:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbara_app', '0003_alter_agressor_historico_ocorrencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agressor',
            name='historico_ocorrencia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='agressores', to='barbara_app.ocorrencia'),
        ),
    ]