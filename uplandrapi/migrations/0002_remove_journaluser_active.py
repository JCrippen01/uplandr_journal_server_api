# Generated by Django 3.2.9 on 2022-01-03 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uplandrapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journaluser',
            name='active',
        ),
    ]
