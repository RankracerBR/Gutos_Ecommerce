# Generated by Django 5.0.3 on 2024-04-22 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='foto_produto',
            field=models.ImageField(default=True, upload_to='imgs/produtos'),
        ),
    ]
