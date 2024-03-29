# Generated by Django 2.2.7 on 2019-11-30 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='farms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farm_name', models.CharField(max_length=10, verbose_name='name')),
                ('x1', models.FloatField(blank=True, null=True)),
                ('y1', models.FloatField(blank=True, null=True)),
                ('x2', models.FloatField(blank=True, null=True)),
                ('y2', models.FloatField(blank=True, null=True)),
                ('x3', models.FloatField(blank=True, null=True)),
                ('y3', models.FloatField(blank=True, null=True)),
                ('x4', models.FloatField(blank=True, null=True)),
                ('y4', models.FloatField(blank=True, null=True)),
                ('sustainable', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]
