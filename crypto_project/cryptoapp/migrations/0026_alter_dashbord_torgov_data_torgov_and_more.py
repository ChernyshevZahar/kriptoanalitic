# Generated by Django 4.2.1 on 2024-02-18 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoapp', '0025_dashbord_torgov_theer_askprice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='Data_torgov',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='dohod',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='dvizhenie_end',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='dvizhenie_pair1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='dvizhenie_pair2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='dvizhenie_start',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='fakt_dohod',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_askPrice',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_askSize',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_bid',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_bidSize',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_datetime_12h',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_datetime_15m',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_datetime_1d',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_datetime_1h',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_datetime_1m',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_datetime_30m',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_datetime_3h',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_datetime_5m',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_datetime_6h',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_pair',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_pair1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_pair2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_priсe',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_priсe_12h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_priсe_15m',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_priсe_1d',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_priсe_1h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_priсe_1m',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_priсe_30m',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_priсe_3h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_priсe_5m',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='one_priсe_6h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='pair1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='pair2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='pair_end',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='pair_start',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='price_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='price_pair1',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='price_pair2',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='price_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='speed_end',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='speed_pair1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='speed_pair2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='speed_start',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_askPrice',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_askSize',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_bid',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_bidSize',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_datetime_12h',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_datetime_15m',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_datetime_1d',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_datetime_1h',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_datetime_1m',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_datetime_30m',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_datetime_3h',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_datetime_5m',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_datetime_6h',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_pair',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_pair1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_pair2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_priсe',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_priсe_12h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_priсe_15m',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_priсe_1d',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_priсe_1h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_priсe_1m',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_priсe_30m',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_priсe_3h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_priсe_5m',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='theer_priсe_6h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_askPrice',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_askSize',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_bid',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_bidSize',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_datetime_12h',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_datetime_15m',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_datetime_1d',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_datetime_1h',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_datetime_1m',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_datetime_30m',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_datetime_3h',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_datetime_5m',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_datetime_6h',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_pair',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_pair1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_pair2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_priсe',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_priсe_12h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_priсe_15m',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_priсe_1d',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_priсe_1h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_priсe_1m',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_priсe_30m',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_priсe_3h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_priсe_5m',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='two_priсe_6h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashbord_torgov',
            name='type_dohod',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
