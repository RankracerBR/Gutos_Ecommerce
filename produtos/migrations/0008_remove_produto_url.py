# Generated by Django 5.0.3 on 2024-05-02 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0007_alter_produto_foto_produto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='url',
        ),
    ]
