# Generated by Django 2.2.12 on 2021-05-08 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bed', '0007_auto_20210428_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='beddata',
            name='oxygen_left_days',
            field=models.CharField(blank=True, max_length=240, verbose_name='Total Days oxygen Left'),
        ),
        migrations.AddField(
            model_name='beddata',
            name='oxygen_left_hour',
            field=models.CharField(blank=True, max_length=240, verbose_name='Total Hours oxygen Left'),
        ),
    ]
