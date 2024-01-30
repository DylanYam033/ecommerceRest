# Generated by Django 3.2.21 on 2023-09-06 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicaluser',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Usuario'},
        ),
        migrations.AlterField(
            model_name='historicaluser',
            name='history_date',
            field=models.DateTimeField(),
        ),
    ]
