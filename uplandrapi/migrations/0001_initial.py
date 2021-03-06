# Generated by Django 3.2.9 on 2022-01-07 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('breed', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uplandrapi.dog')),
            ],
        ),
        migrations.CreateModel(
            name='Gear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('notes', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='JournalUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField(auto_now=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('entry_date', models.DateField()),
                ('duration', models.TimeField()),
                ('party', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('weather', models.CharField(max_length=50)),
                ('gear', models.CharField(max_length=100)),
                ('hunt_highlights', models.CharField(max_length=100)),
                ('dogs', models.ManyToManyField(related_name='dogs', through='uplandrapi.DogEntry', to='uplandrapi.Dog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uplandrapi.journaluser')),
            ],
        ),
        migrations.AddField(
            model_name='dogentry',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uplandrapi.journalentry'),
        ),
    ]
