# Generated by Django 2.2.7 on 2019-11-30 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_farms'),
    ]

    operations = [
        migrations.AddField(
            model_name='farms',
            name='corp_type',
            field=models.CharField(default='type_1', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='farms',
            name='farm_name',
            field=models.CharField(max_length=500),
        ),
    ]
