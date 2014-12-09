# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('short_name', models.CharField(max_length=63)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('short_name', models.CharField(max_length=63)),
            ],
            options={
                'verbose_name_plural': 'counties',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('short_name', models.CharField(max_length=63)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('shoot_type', models.CharField(choices=[('I', 'Indoor Target'), ('O', 'Outdoor Target'), ('F', 'Field'), ('C', 'Clout'), ('W', 'Wand'), ('L', 'Flight'), ('O', 'Other'), ('M', 'Mixed')], max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'series',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=511)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('listed', 'Listed'), ('open', 'Entries open'), ('full', 'Full'), ('ongoing', 'Happening now'), ('past', 'Completed')], max_length=31)),
                ('shoot_type', models.CharField(choices=[('I', 'Indoor Target'), ('O', 'Outdoor Target'), ('F', 'Field'), ('C', 'Clout'), ('W', 'Wand'), ('L', 'Flight'), ('O', 'Other'), ('M', 'Mixed')], max_length=1)),
                ('record_status', models.CharField(choices=[('None', 'No record status'), ('UKRS', 'UK record status'), ('WRS', 'World record status'), ('Rose', 'Rose & UK record status'), ('AH', 'Arrowhead'), ('Tassel', 'Tassel status'), ('TUKRS', 'Tassel & UK record status')], max_length=7)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('organising_club', models.ForeignKey(blank=True, null=True, to='tournaments.Club')),
                ('organising_county', models.ForeignKey(blank=True, null=True, to='tournaments.County')),
                ('rounds', models.ManyToManyField(to='tournaments.Round')),
                ('series', models.ForeignKey(blank=True, null=True, to='tournaments.Series')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='county',
            name='region',
            field=models.ForeignKey(blank=True, null=True, to='tournaments.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='club',
            name='county',
            field=models.ForeignKey(blank=True, null=True, to='tournaments.County'),
            preserve_default=True,
        ),
    ]
