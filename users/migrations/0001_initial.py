# Generated by Django 3.1.4 on 2021-01-14 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=250, unique=True)),
                ('passphrase', models.CharField(max_length=1834)),
                ('pubk', models.CharField(max_length=400)),
                ('privk', models.CharField(max_length=400)),
            ],
        ),
    ]
