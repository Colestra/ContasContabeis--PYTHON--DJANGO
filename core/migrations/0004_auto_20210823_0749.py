# Generated by Django 3.2.6 on 2021-08-23 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contas'),
    ]

    operations = [
        migrations.AddField(
            model_name='contas',
            name='iva',
            field=models.CharField(max_length=100, null=True, verbose_name='IVA'),
        ),
        migrations.AlterField(
            model_name='contas',
            name='credito',
            field=models.CharField(max_length=45, verbose_name='Credito'),
        ),
    ]