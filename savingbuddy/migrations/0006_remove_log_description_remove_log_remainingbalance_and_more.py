# Generated by Django 4.2.3 on 2023-08-21 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('savingbuddy', '0005_log'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='description',
        ),
        migrations.RemoveField(
            model_name='log',
            name='remainingbalance',
        ),
        migrations.RemoveField(
            model_name='log',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='log',
            name='value',
        ),
    ]