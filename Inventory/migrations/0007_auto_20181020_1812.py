# Generated by Django 2.1.2 on 2018-10-20 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0006_auto_20181019_1030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='devicegroup',
            options={'verbose_name_plural': 'listofgroups'},
        ),
        migrations.AlterField(
            model_name='device',
            name='group',
            field=models.ManyToManyField(blank=True, null=True, to='Inventory.DeviceGroup'),
        ),
    ]
