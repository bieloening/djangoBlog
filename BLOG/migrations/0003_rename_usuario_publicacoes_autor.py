# Generated by Django 4.1.3 on 2022-11-10 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG', '0002_publicacoes_criado_em'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicacoes',
            old_name='usuario',
            new_name='autor',
        ),
    ]
