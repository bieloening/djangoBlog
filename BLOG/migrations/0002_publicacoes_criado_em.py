# Generated by Django 4.1.3 on 2022-11-10 03:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacoes',
            name='criado_em',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]