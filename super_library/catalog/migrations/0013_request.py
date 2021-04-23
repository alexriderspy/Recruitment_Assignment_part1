# Generated by Django 3.2 on 2021-04-22 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0012_alter_bookinstance_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookinst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookinst', to='catalog.bookinstance')),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrower', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('can_grant_decline_request', 'Grant or decline a Request'),),
            },
        ),
    ]
