# Generated by Django 3.2.18 on 2023-04-01 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('galleryposts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Save',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('galleryposts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved', to='galleryposts.gallerypost')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved', to='posts.post')),
            ],
            options={
                'ordering': ['-created_on'],
                'unique_together': {('owner', 'galleryposts')},
            },
        ),
    ]
