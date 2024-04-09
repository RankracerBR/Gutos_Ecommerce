# Generated by Django 5.0.3 on 2024-04-08 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(default=None, max_length=100)),
                ('valor_produto', models.FloatField()),
                ('tipo_produto', models.CharField(default=None, max_length=50)),
            ],
        ),
    ]