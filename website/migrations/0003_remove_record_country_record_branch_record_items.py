# Generated by Django 5.2.1 on 2025-05-20 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_records_record'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='country',
        ),
        migrations.AddField(
            model_name='record',
            name='branch',
            field=models.CharField(blank=True, choices=[('sm', 'Smouha'), ('bo', 'Boukla'), ('mi', 'Miami')], max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='items',
            field=models.IntegerField(default=0),
        ),
    ]
