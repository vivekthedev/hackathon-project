# Generated by Django 2.1.7 on 2021-09-20 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatcanido', '0002_auto_20210920_2058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='data',
            options={'verbose_name_plural': 'Data'},
        ),
    ]