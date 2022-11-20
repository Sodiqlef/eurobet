# Generated by Django 4.0.2 on 2022-11-10 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_away_cleansheet_bet_away_cleansheet_no_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bet',
            old_name='ft_score_home',
            new_name='total_yc_over',
        ),
        migrations.RenameField(
            model_name='bet',
            old_name='ft_score_away',
            new_name='total_yc_under',
        ),
        migrations.RemoveField(
            model_name='bet',
            name='ht_score_away',
        ),
        migrations.RemoveField(
            model_name='bet',
            name='ht_score_home',
        ),
        migrations.RemoveField(
            model_name='bet',
            name='total_goals',
        ),
        migrations.RemoveField(
            model_name='bet',
            name='total_yc',
        ),
        migrations.AddField(
            model_name='bet',
            name='ht_score_away_over',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bet',
            name='ht_score_away_under',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bet',
            name='ht_score_home_over',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bet',
            name='ht_score_home_under',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bet',
            name='total_goals_away_over',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bet',
            name='total_goals_away_under',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bet',
            name='total_goals_home_over',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bet',
            name='total_goals_home_under',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
