# Generated by Django 4.2.3 on 2023-08-15 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0018_remove_user_user_role_user_user_role_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_role_name',
        ),
        migrations.AddField(
            model_name='user',
            name='user_role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Owner'), (2, 'Admin'), (3, 'Employee')], null=True),
        ),
    ]
