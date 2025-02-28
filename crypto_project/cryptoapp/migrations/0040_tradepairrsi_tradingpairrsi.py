# Generated by Django 4.2.1 on 2024-05-26 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoapp', '0039_tradingpair_price_pair'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradePairRsi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(blank=True, max_length=100, null=True)),
                ('pair', models.CharField(blank=True, max_length=100, null=True)),
                ('pair_up', models.CharField(blank=True, max_length=100, null=True)),
                ('pair_down', models.CharField(blank=True, max_length=100, null=True)),
                ('pair_price', models.CharField(blank=True, max_length=100, null=True)),
                ('pair_rsi', models.CharField(blank=True, max_length=100, null=True)),
                ('lisen_pair_rsi', models.CharField(blank=True, max_length=100, null=True)),
                ('way_pair_rsi', models.CharField(blank=True, max_length=100, null=True)),
                ('price_pair_rsi', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TradingPairRsi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(blank=True, max_length=100, null=True)),
                ('pair', models.CharField(blank=True, max_length=100, null=True)),
                ('pair_up', models.CharField(blank=True, max_length=100, null=True)),
                ('pair_down', models.CharField(blank=True, max_length=100, null=True)),
                ('pair_price', models.CharField(blank=True, max_length=100, null=True)),
                ('pair_rsi', models.CharField(blank=True, max_length=100, null=True)),
                ('lisen_pair_rsi', models.CharField(blank=True, max_length=100, null=True)),
                ('way_pair_rsi', models.CharField(blank=True, max_length=100, null=True)),
                ('price_pair_rsi', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
