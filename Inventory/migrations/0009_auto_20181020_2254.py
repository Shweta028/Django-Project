# Generated by Django 2.1.2 on 2018-10-20 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0008_auto_20181020_1922'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='devicegroup',
            options={'verbose_name_plural': 'groups'},
        ),
        migrations.RenameField(
            model_name='device',
            old_name='group',
            new_name='groups',
        ),
    ]