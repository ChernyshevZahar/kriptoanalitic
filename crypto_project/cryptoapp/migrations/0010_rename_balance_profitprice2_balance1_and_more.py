# Generated by Django 4.2.1 on 2024-01-20 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoapp', '0009_profitprice2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profitprice2',
            old_name='balance',
            new_name='balance1',
        ),
        migrations.AddField(
            model_name='profitprice2',
            name='balance2',
            field=models.FloatField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profitprice2',
            name='balance3',
            field=models.FloatField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profitprice2',
            name='balance4',
            field=models.FloatField(max_length=20, null=True),
        ),
    ]
