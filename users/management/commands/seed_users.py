from django.core.management.base import BaseCommand
from users.models import User
from django_seed import Seed
import random
from django.contrib.admin.utils import flatten


class Command(BaseCommand):
    help = 'This command is '

    def add_arguments(self, parser):
        parser.add_argument("--number", default=2, type=int,
                            help="How many users create")

    def handle(self, *args, **options):
        number = options.get("number")

        seeder = Seed.seeder()
        seeder.add_entity(User, number, {
            'stu_id': lambda x: random.randint(200000000, 202200000),
            'email': lambda x: seeder.faker.email(),
        })
        # python manage.py seed_users --numbers 50
        seeder.execute()
