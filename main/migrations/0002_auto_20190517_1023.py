# Generated by Django 2.1.7 on 2019-05-17 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeaccount',
            name='email',
            field=models.CharField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='employeeaccount',
            name='passwordHashAlgorithm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employeeaccount',
            name='passwordReminderExpiration',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employeeaccount',
            name='passwordReminderToken',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employeeaccount',
            name='passwordSalt',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employeeaccount',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='incidencetype',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='endDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]