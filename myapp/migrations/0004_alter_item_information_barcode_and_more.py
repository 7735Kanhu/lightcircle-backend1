# Generated by Django 5.0.6 on 2024-08-27 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_stockin_present_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_information',
            name='Barcode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='item_information',
            name='Name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='item_information',
            name='Price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='item_information',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='item_information',
            name='initial_quantity',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
