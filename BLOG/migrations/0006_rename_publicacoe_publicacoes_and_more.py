# Generated by Django 4.1.3 on 2022-11-10 23:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BLOG', '0005_rename_publicacoes_publicacoe'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Publicacoe',
            new_name='Publicacoes',
        ),
        migrations.AlterModelOptions(
            name='publicacoes',
            options={'verbose_name_plural': 'Publicações'},
        ),
    ]
