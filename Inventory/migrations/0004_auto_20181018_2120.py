# Generated by Django 2.1.2 on 2018-10-18 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0003_auto_20181018_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='group',
        ),
        migrations.AddField(
            model_name='device',
            name='group',
            field=models.ManyToManyField(default=None, null=True, to='Inventory.DeviceGroup'),
        ),
    ]
