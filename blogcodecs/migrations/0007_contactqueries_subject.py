# Generated by Django 3.2.4 on 2021-06-30 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogcodecs', '0006_contactqueries'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactqueries',
            name='subject',
            field=models.CharField(default=0, max_length=10000),
            preserve_default=False,
        ),
    ]
