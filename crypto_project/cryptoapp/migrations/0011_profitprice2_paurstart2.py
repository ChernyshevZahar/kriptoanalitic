# Generated by Django 4.2.1 on 2024-01-20 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoapp', '0010_rename_balance_profitprice2_balance1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profitprice2',
            name='paurstart2',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
