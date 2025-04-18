# Generated by Django 5.1.7 on 2025-04-16 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('requirements', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=75)),
                ('location_type', models.CharField(choices=[('ON-SITE', 'On-Site'), ('REMOTE', 'Remote'), ('HYBRID', 'Hybrid')], max_length=7)),
                ('company_name', models.CharField(max_length=75)),
                ('date_posted', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
