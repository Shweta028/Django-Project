# Generated by Django 2.1.2 on 2018-10-20 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0009_auto_20181020_2254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='devicegroup',
            options={'verbose_name_plural': 'devicegroups'},
        ),
        migrations.RenameField(
            model_name='device',
            old_name='groups',
            new_name='devicegroups',
        ),
    ]
