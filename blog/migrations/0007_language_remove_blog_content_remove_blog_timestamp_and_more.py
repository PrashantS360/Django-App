# Generated by Django 4.1.5 on 2023-01-28 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('code', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('language', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name='blog',
            name='language',
            field=models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.language'),
        ),
    ]
