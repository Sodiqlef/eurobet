# Generated by Django 4.0.2 on 2022-10-31 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_bet_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='away',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bet',
            name='away_h1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bet',
            name='draw',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bet',
            name='draw_h1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bet',
            name='gg',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bet',
            name='home_h1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bet',
            name='ng',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bet',
            name='over_2p5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bet',
            name='over_3p5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bet',
            name='over_4p5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bet',
            name='under_2p5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bet',
            name='under_3p5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bet',
            name='under_4p5',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
