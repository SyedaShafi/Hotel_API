# Generated by Django 5.0.3 on 2024-04-28 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='per_day_price',
            field=models.IntegerField(default=0),
        ),
    ]
