# Generated by Django 3.0.2 on 2020-01-17 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0002_auto_20200117_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='tickets_bought',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
