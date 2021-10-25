# Generated by Django 3.2.5 on 2021-09-16 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0010_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('partner', models.CharField(max_length=60)),
                ('branches', models.CharField(blank=True, max_length=60, null=True)),
                ('product_type', models.CharField(max_length=60)),
                ('approx_fee', models.CharField(max_length=60)),
                ('revenue_type', models.CharField(blank=True, max_length=60, null=True)),
                ('intake_month', models.CharField(blank=True, max_length=60, null=True)),
                ('duration', models.CharField(blank=True, max_length=60, null=True)),
                ('description', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
    ]