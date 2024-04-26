# Generated by Django 5.0.3 on 2024-04-11 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(default=None, max_length=200)),
                ('valor_produto', models.FloatField()),
                ('tipo_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.categoriaproduto')),
            ],
        ),
    ]
