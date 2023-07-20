# Generated by Django 4.2.3 on 2023-07-20 18:03

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_phone', models.CharField(max_length=20)),
                ('deleted_flag', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ingestion_timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_email', models.EmailField(max_length=254)),
                ('client_phone', models.CharField(max_length=20)),
                ('client_first_name', models.CharField(max_length=50)),
                ('client_last_name', models.CharField(max_length=50)),
                ('deleted_flag', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ingestion_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_subscription_status', models.CharField(max_length=50)),
                ('company_email', models.EmailField(max_length=254)),
                ('company_phone', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=50)),
                ('owner_first_name', models.CharField(max_length=50)),
                ('owner_last_name', models.CharField(max_length=50)),
                ('company_can_contact', models.BooleanField(default=False)),
                ('company_can_email', models.BooleanField(default=False)),
                ('company_address_lines', models.TextField(max_length=200)),
                ('company_city', models.CharField(max_length=50)),
                ('company_state', models.CharField(max_length=50)),
                ('company_country', models.CharField(max_length=50)),
                ('company_zip_code', models.CharField(max_length=50)),
                ('first_sign_up_date', models.DateTimeField(auto_now_add=True)),
                ('last_sign_up_date', models.DateTimeField(auto_now_add=True)),
                ('first_subscription_date', models.DateTimeField(auto_now_add=True)),
                ('last_subscription_date', models.DateTimeField(auto_now_add=True)),
                ('first_cancelation_date', models.DateTimeField(auto_now_add=True)),
                ('last_cancelation_date', models.DateTimeField(auto_now_add=True)),
                ('deleted_flag', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ingestion_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_order_date', models.DateTimeField(auto_now_add=True)),
                ('work_order_due_date', models.DateTimeField(auto_now_add=True)),
                ('work_order_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('work_order_currency', models.CharField(max_length=10)),
                ('quoted_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('quoted_currency', models.CharField(max_length=10)),
                ('work_order_type', models.CharField(max_length=50)),
                ('work_order_status', models.CharField(max_length=50)),
                ('work_order_description', models.TextField(max_length=200)),
                ('deleted_flag', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ingestion_timestamp', models.DateTimeField(auto_now=True)),
                ('client_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.client')),
                ('company_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.company')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=50)),
                ('plan_frequency', models.CharField(max_length=50)),
                ('plan_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('plan_currency', models.CharField(max_length=50)),
                ('plan_description', models.TextField(max_length=200)),
                ('plan_features', models.TextField(max_length=200)),
                ('plan_trial_period', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ingestion_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ingestion_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_role_name', models.CharField(max_length=50)),
                ('user_role_description', models.TextField(max_length=200)),
                ('deleted_flag', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ingestion_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Activity_Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_activity_time', models.DateTimeField(auto_now_add=True)),
                ('deleted_flag', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ingestion_timestamp', models.DateTimeField(auto_now=True)),
                ('client_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.client')),
                ('user_action_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.user_action')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('work_order_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.order')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='company_current_plan_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.plan'),
        ),
        migrations.AddField(
            model_name='client',
            name='company_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.company'),
        ),
        migrations.CreateModel(
            name='Billing_Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_date', models.DateTimeField(auto_now_add=True)),
                ('billing_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('billing_status', models.CharField(max_length=50)),
                ('billing_period_start_date', models.DateTimeField(auto_now_add=True)),
                ('billing_period_end_date', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ingestion_timestamp', models.DateTimeField(auto_now=True)),
                ('plan_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.plan')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='company_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.company'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='role_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.user_role'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
