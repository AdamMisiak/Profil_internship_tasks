# Generated by Django 3.0.8 on 2020-07-29 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queries', '0006_auto_20200729_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id_value',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
