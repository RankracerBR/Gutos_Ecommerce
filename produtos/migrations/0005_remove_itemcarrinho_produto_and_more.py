# Generated by Django 5.0.3 on 2024-05-02 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_itemcarrinho_carrinho'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemcarrinho',
            name='produto',
        ),
        migrations.RemoveField(
            model_name='itemcarrinho',
            name='usuario_orgm',
        ),
        migrations.DeleteModel(
            name='Carrinho',
        ),
        migrations.DeleteModel(
            name='ItemCarrinho',
        ),
    ]
