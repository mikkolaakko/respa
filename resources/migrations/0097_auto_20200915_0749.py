# Generated by Django 2.2.13 on 2020-09-15 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0096_multidaysettings_must_end_on_start_day'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='multidaysettings',
            options={'verbose_name': 'Multiday settings'},
        ),
        migrations.AlterModelOptions(
            name='multidaystartday',
            options={'verbose_name': 'Multiday settings start day'},
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='reservation_length_type',
            new_name='length_type',
        ),
    ]
