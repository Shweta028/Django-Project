# Generated by Django 2.1.2 on 2018-10-17 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicegroup',
            name='devices',
        ),
        migrations.AddField(
            model_name='device',
            name='group',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Inventory.DeviceGroup'),
        ),
    ]