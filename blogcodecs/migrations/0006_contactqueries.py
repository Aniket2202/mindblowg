# Generated by Django 3.2.4 on 2021-06-30 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogcodecs', '0005_newslettersubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactQueries',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.BigIntegerField()),
                ('name', models.CharField(max_length=1000)),
                ('message', models.TextField()),
            ],
        ),
    ]
