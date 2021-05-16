# Generated by Django 2.2.13 on 2021-04-28 12:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BedData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=240, null=True, verbose_name='Hospital Type')),
                ('update', models.CharField(blank=True, max_length=240, null=True, verbose_name='Update date time')),
                ('total', models.CharField(blank=True, max_length=240, null=True, verbose_name='Total Beds')),
                ('occupied', models.CharField(blank=True, max_length=240, null=True, verbose_name='Total Occupied beds')),
                ('vacant', models.CharField(blank=True, max_length=240, null=True, verbose_name='Total Vacant beds')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'COVID BEDS DATA',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='HospitalData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=240, null=True, verbose_name='Hospital Type')),
                ('address', models.CharField(blank=True, max_length=240, null=True, verbose_name='Hospital Address')),
                ('contact_number', models.CharField(blank=True, max_length=240, null=True, verbose_name='Hospital contact number')),
                ('map_link', models.URLField(blank=True, max_length=240, null=True, verbose_name='Hospital contact number')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Hospital Data',
            },
        ),
    ]
