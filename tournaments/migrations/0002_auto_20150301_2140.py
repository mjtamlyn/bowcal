# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address_1', models.CharField(max_length=255)),
                ('address_2', models.CharField(default='', blank=True, max_length=255)),
                ('town', models.CharField(default='', blank=True, max_length=255)),
                ('postcode', models.CharField(default='', blank=True, max_length=255)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='longitude',
        ),
        migrations.AddField(
            model_name='tournament',
            name='venue',
            field=models.ForeignKey(null=True, to='tournaments.Venue', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='round',
            name='shoot_type',
            field=models.CharField(choices=[('I', 'Indoor Target'), ('O', 'Outdoor Target'), ('F', 'Field'), ('C', 'Clout'), ('W', 'Wand'), ('L', 'Flight'), ('H', 'Other'), ('M', 'Mixed')], max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='shoot_type',
            field=models.CharField(choices=[('I', 'Indoor Target'), ('O', 'Outdoor Target'), ('F', 'Field'), ('C', 'Clout'), ('W', 'Wand'), ('L', 'Flight'), ('H', 'Other'), ('M', 'Mixed')], max_length=1),
            preserve_default=True,
        ),
    ]
