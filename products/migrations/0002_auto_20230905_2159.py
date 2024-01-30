# Generated by Django 3.2.21 on 2023-09-06 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryproduct',
            options={'verbose_name': 'Category Product', 'verbose_name_plural': 'Category Product'},
        ),
        migrations.AlterModelOptions(
            name='historicalcategoryproduct',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Category Product'},
        ),
        migrations.AlterModelOptions(
            name='historicalindicator',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Indicador de Oferta'},
        ),
        migrations.AlterModelOptions(
            name='historicalmeasureunit',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Unidad de Medida'},
        ),
        migrations.AlterModelOptions(
            name='historicalproduct',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Producto'},
        ),
        migrations.AlterField(
            model_name='historicalcategoryproduct',
            name='history_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='historicalindicator',
            name='history_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='historicalmeasureunit',
            name='history_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='historicalproduct',
            name='history_date',
            field=models.DateTimeField(),
        ),
    ]
