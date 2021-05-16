# Generated by Django 2.2.13 on 2021-04-28 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bed', '0003_hospitaldata_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitaldata',
            name='bed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bed.BedData', verbose_name='bed'),
        ),
    ]