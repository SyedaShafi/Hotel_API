# Generated by Django 5.0.3 on 2024-04-28 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['date']},
        ),
    ]
