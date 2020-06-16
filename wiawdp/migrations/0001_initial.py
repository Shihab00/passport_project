# Generated by Django 3.0.6 on 2020-06-12 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('ext_address', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=30)),
                ('zipcode', models.CharField(max_length=5)),
                ('country', models.CharField(default='US', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CareerPathway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career_pathway', models.CharField(max_length=200)),
                ('cip_code', models.CharField(max_length=7)),
                ('program_title', models.CharField(max_length=200)),
                ('date_approved', models.DateField()),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Workforce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workforce', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('company_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=32)),
                ('first_name', models.CharField(max_length=32)),
                ('desc', models.TextField(blank=True)),
                ('home_phone', models.CharField(max_length=20)),
                ('cell_phone', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=32)),
                ('salutation', models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('None', 'None')], default='None', max_length=8)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiawdp.Address')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_date', models.DateTimeField()),
                ('performance', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiawdp.Person')),
                ('workforce', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wiawdp.Workforce')),
            ],
        ),
    ]