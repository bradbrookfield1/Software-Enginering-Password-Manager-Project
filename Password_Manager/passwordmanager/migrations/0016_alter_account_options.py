# Generated by Django 3.2.8 on 2021-10-24 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passwordmanager', '0015_alter_account_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ('author', 'name')},
        ),
    ]
