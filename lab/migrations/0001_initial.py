# Generated by Django 2.1.1 on 2018-11-17 14:47

import django.db.models.deletion
import macaddress.fields
from django.conf import settings
from django.db import migrations, models

import lab.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_type', models.CharField(choices=[('Routes IPv4', 'IPv4 routes'), ('Routes IPv6', 'IPv6 routes'),
                                                        ('Received traffic', 'Received traffic'),
                                                        ('NEIGHBORS', 'Import/export'), ('ASN IPv4', 'IPv4 from ASN'),
                                                        ('ASN IPv6', 'IPv6 from ASN'),
                                                        ('AS-SET IPv4', 'IPv4 from AS-SET'),
                                                        ('AS-SET IPv6', 'IPv6 from AS-SET')], max_length=50,
                                               verbose_name='goal type')),
                ('state', models.TextField(blank=True, verbose_name='state')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='last update')),
            ],
            options={
                'verbose_name': 'exercise state',
                'verbose_name_plural': 'exercise states',
                'ordering': ('exercise_node__name', 'goal_type'),
            },
        ),
        migrations.CreateModel(
            name='IRRGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_type', models.CharField(choices=[('NEIGHBORS', 'Import/export'), ('ASN IPv4', 'IPv4 from ASN'),
                                                        ('ASN IPv6', 'IPv6 from ASN'),
                                                        ('AS-SET IPv4', 'IPv4 from AS-SET'),
                                                        ('AS-SET IPv6', 'IPv6 from AS-SET')], max_length=50,
                                               verbose_name='goal type')),
                ('goal_content', models.TextField(blank=True, verbose_name='goal content')),
            ],
            options={
                'verbose_name': 'IRR goal',
                'verbose_name_plural': 'IRR goals',
                'ordering': ('irr_template__name', 'goal_type'),
            },
        ),
        migrations.CreateModel(
            name='IRRTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name')),
                ('instructions',
                 models.TextField(blank=True, help_text='Use markdown for styling', verbose_name='instructions')),
            ],
            options={
                'verbose_name': 'IRR template',
                'verbose_name_plural': 'IRR templates',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='MonitorGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_type', models.CharField(choices=[('Routes IPv4', 'IPv4 routes'), ('Routes IPv6', 'IPv6 routes'),
                                                        ('Received traffic', 'Received traffic')], max_length=50,
                                               verbose_name='goal type')),
                ('goal_content', models.TextField(blank=True, verbose_name='goal content')),
            ],
            options={
                'verbose_name': 'monitor goal',
                'verbose_name_plural': 'monitor goals',
                'ordering': ('monitor_template__name', 'goal_type'),
            },
        ),
        migrations.CreateModel(
            name='MonitorTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name')),
                ('instructions',
                 models.TextField(blank=True, help_text='Use markdown for styling', verbose_name='instructions')),
            ],
            options={
                'verbose_name': 'monitor template',
                'verbose_name_plural': 'monitor templates',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gns3_id', models.UUIDField(editable=False, unique=True, verbose_name='node id')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('mac_address', macaddress.fields.MACAddressField(integer=True, verbose_name='MAC fix_address')),
            ],
            options={
                'verbose_name': 'node',
                'verbose_name_plural': 'nodes',
                'ordering': ('project__name', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gns3_id', models.UUIDField(editable=False, unique=True, verbose_name='project id')),
                ('name', models.CharField(editable=False, max_length=100, verbose_name='name')),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('project_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='lab.Project')),
                ('started', models.DateTimeField(auto_now_add=True, verbose_name='started')),
                ('deadline', models.DateTimeField(blank=True, null=True, verbose_name='deadline')),
            ],
            options={
                'verbose_name': 'exercise',
                'verbose_name_plural': 'exercises',
            },
            bases=('lab.project',),
        ),
        migrations.CreateModel(
            name='ExerciseNode',
            fields=[
                ('node_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='lab.Node')),
            ],
            options={
                'verbose_name': 'exercise node',
                'verbose_name_plural': 'exercise nodes',
            },
            bases=('lab.node',),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('project_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='lab.Project')),
                ('allow_new_exercises', models.BooleanField(default=False,
                                                            help_text='Allow any student to start this exercise without supervision',
                                                            verbose_name='allow self-signup')),
                ('default_time_limit', models.PositiveIntegerField(blank=True, help_text='in minutes', null=True,
                                                                   verbose_name='default time limit')),
                ('instructions', models.TextField(blank=True, help_text='Use markdown for styling',
                                                  verbose_name='exercise instructions')),
            ],
            options={
                'verbose_name': 'exercise template',
                'verbose_name_plural': 'exercise templates',
            },
            bases=('lab.project',),
        ),
        migrations.CreateModel(
            name='TemplateNode',
            fields=[
                ('node_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='lab.Node')),
            ],
            bases=('lab.node',),
        ),
        migrations.AddField(
            model_name='node',
            name='project',
            field=lab.fields.InheritanceForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Project',
                                                   verbose_name='project'),
        ),
        migrations.AddField(
            model_name='monitorgoal',
            name='monitor_template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.MonitorTemplate',
                                    verbose_name='monitor template'),
        ),
        migrations.AddField(
            model_name='irrgoal',
            name='irr_template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.IRRTemplate',
                                    verbose_name='IRR template'),
        ),
        migrations.CreateModel(
            name='IRRNode',
            fields=[
                ('templatenode_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='lab.TemplateNode')),
                ('maintainer', models.CharField(blank=True, max_length=50, verbose_name='maintainer')),
                (
                'maintainer_password', models.CharField(blank=True, max_length=50, verbose_name='maintainer password')),
                ('default_username', models.CharField(blank=True, max_length=50, verbose_name='console username')),
                ('default_password', models.CharField(blank=True, max_length=50, verbose_name='console password')),
                ('irr_template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                   to='lab.IRRTemplate', verbose_name='IRR template')),
            ],
            options={
                'verbose_name': 'IRR node',
                'verbose_name_plural': 'IRR nodes',
            },
            bases=('lab.templatenode',),
        ),
        migrations.CreateModel(
            name='MonitorNode',
            fields=[
                ('templatenode_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='lab.TemplateNode')),
                ('monitor_template',
                 models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                   to='lab.MonitorTemplate', verbose_name='monitor template')),
            ],
            options={
                'verbose_name': 'monitor node',
                'verbose_name_plural': 'monitor nodes',
            },
            bases=('lab.templatenode',),
        ),
        migrations.CreateModel(
            name='WorkNode',
            fields=[
                ('templatenode_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='lab.TemplateNode')),
                ('default_username', models.CharField(blank=True, max_length=50, verbose_name='username')),
                ('default_password', models.CharField(blank=True, max_length=50, verbose_name='password')),
                ('instructions',
                 models.TextField(blank=True, help_text='Use markdown for styling', verbose_name='instructions')),
            ],
            options={
                'verbose_name': 'work node',
                'verbose_name_plural': 'work nodes',
            },
            bases=('lab.templatenode',),
        ),
        migrations.AlterUniqueTogether(
            name='node',
            unique_together={('project', 'mac_address'), ('project', 'gns3_id')},
        ),
        migrations.AlterUniqueTogether(
            name='monitorgoal',
            unique_together={('monitor_template', 'goal_type')},
        ),
        migrations.AlterUniqueTogether(
            name='irrgoal',
            unique_together={('irr_template', 'goal_type')},
        ),
        migrations.AddField(
            model_name='exercisestate',
            name='exercise_node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.ExerciseNode',
                                    verbose_name='exercise node'),
        ),
        migrations.AddField(
            model_name='exercisenode',
            name='template_node',
            field=lab.fields.InheritanceForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.TemplateNode',
                                                   verbose_name='template node'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='based_on',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lab.Template',
                                    verbose_name='template'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL,
                                    verbose_name='student'),
        ),
        migrations.AlterUniqueTogether(
            name='exercisestate',
            unique_together={('exercise_node', 'goal_type')},
        ),
    ]
