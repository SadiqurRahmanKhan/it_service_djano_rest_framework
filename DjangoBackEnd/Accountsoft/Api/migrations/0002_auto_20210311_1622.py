# Generated by Django 3.1.4 on 2021-03-11 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recept',
            name='invoice_number',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]
