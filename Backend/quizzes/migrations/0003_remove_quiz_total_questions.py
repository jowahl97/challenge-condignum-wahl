

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_auto_20201215_0712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='total_questions',
        ),
    ]
