# Generated by Django 2.2.13 on 2020-09-04 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0094_multi_day_settings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multidaysettings',
            name='max_days',
        ),
        migrations.RemoveField(
            model_name='multidaysettings',
            name='min_days',
        ),
        migrations.AddField(
            model_name='multidaysettings',
            name='duration_unit',
            field=models.CharField(choices=[('day', 'Day'), ('week', 'Week'), ('month', 'Month')], default='day', max_length=5, verbose_name='Duration type'),
        ),
        migrations.AddField(
            model_name='multidaysettings',
            name='max_duration',
            field=models.IntegerField(default=7, verbose_name='Max duration'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='multidaysettings',
            name='min_duration',
            field=models.IntegerField(default=7, verbose_name='Min duration'),
            preserve_default=False,
        ),
    ]
