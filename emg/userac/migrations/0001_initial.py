# Generated by Django 5.0.6 on 2024-07-07 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=20)),
                ('grand_father_name', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('region', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('religion', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('emergency_name', models.CharField(max_length=20)),
                ('emergency_phone', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=128)),
                ('user_name', models.CharField(max_length=20, unique=True)),
                ('created_by', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('A', 'Active'), ('D', 'Deactivated')], max_length=1)),
                ('type_of_account', models.CharField(max_length=20)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
