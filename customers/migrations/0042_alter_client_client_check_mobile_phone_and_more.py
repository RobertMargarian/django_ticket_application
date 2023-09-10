# Generated by Django 4.2.3 on 2023-09-08 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0041_alter_client_client_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_check_mobile_phone',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_first_name',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_last_name',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
