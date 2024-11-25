# Generated by Django 5.1 on 2024-10-21 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0002_rename_typerequest_support_typerequest_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='image',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='ips',
            name='cod_ips',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ips',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='ips',
            name='nombre_ips',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='subtyperequest',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='subtyperequest',
            name='subtype_request',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='support',
            name='answer',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='support',
            name='email',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='support',
            name='how_it_conclude',
            field=models.TextField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='support',
            name='name_solicited',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='support',
            name='number',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='support',
            name='requirement',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='typerequest',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='typerequest',
            name='typerequest',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
