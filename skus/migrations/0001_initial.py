# Generated by Django 5.0.6 on 2024-06-26 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('medication_name', models.CharField(max_length=500)),
                ('dose', models.CharField(max_length=500)),
                ('presentation', models.CharField(max_length=500)),
                ('unit', models.CharField(max_length=50)),
                ('countries', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]