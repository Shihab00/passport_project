# Generated by Django 3.0.6 on 2020-06-14 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counselor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='WIAWDP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_profile', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Please enter the course name.', max_length=70)),
                ('slug', models.SlugField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('location', models.CharField(choices=[('southplainfield-g', 'South Plainfield G'), ('southplainfield-b', 'South Plainfield B'), ('southplainfield-c', 'South Plainfield C'), ('southplainfield-d', 'South Plainfield D'), ('southplainfield-e', 'South Plainfield E'), ('southplainfield-a', 'South Plainfield A'), ('southplainfield-h', 'South Plainfield H'), ('southplainfield-f', 'South Plainfield F'), ('fairfield-e', 'Fairfield E'), ('fairfield-a', 'Fairfield A'), ('fairfield-b', 'Fairfield B'), ('fairfield-c', 'Fairfield C'), ('fairfield-d', 'Fairfield D'), ('eatontown-a', 'Eatontown A'), ('eatontown-b', 'Eatontown B'), ('eatontown-c', 'Eatontown C'), ('eatontown-d', 'Eatontown D'), ('eatontown-e', 'Eatontown E')], max_length=32)),
                ('counselor', models.ManyToManyField(blank=True, null=True, related_name='Counselor', to='courses.Counselor')),
                ('student', models.ManyToManyField(blank=True, null=True, related_name='Student', to='courses.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='courses.Subject')),
                ('wiawdp', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='WIAWDP', to='courses.WIAWDP')),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
                'ordering': ['-created'],
                'permissions': (('can_list_courses', 'List All The Courses'),),
            },
        ),
    ]