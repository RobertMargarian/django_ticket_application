# Generated by Django 4.2.3 on 2023-10-31 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_country',
            field=models.CharField(default='United States', max_length=50),
            preserve_default=False,
        ),
    ]
