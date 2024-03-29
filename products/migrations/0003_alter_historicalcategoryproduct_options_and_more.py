# Generated by Django 4.2.1 on 2023-09-13 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230905_2159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalcategoryproduct',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Category Product', 'verbose_name_plural': 'historical Category Product'},
        ),
        migrations.AlterModelOptions(
            name='historicalindicator',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Indicador de Oferta', 'verbose_name_plural': 'historical Indicadores de Ofertas'},
        ),
        migrations.AlterModelOptions(
            name='historicalmeasureunit',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Unidad de Medida', 'verbose_name_plural': 'historical Unidades de Medidas'},
        ),
        migrations.AlterModelOptions(
            name='historicalproduct',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Producto', 'verbose_name_plural': 'historical Productos'},
        ),
        migrations.AlterField(
            model_name='historicalcategoryproduct',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalindicator',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalmeasureunit',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalproduct',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]
