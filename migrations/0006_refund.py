# Generated by Django 4.2.5 on 2023-12-20 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('busname', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('nofseats', models.DecimalField(decimal_places=0, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('refundprice', models.PositiveIntegerField(max_length=50)),
            ],
        ),
    ]
