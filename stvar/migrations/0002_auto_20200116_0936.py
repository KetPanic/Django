# Generated by Django 3.0.2 on 2020-01-16 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stvar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stvar',
            name='grad',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stvar',
            name='telefon',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
