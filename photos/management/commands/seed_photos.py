from django.core.management.base import BaseCommand
from photos.models import Photo as photo_model
from django_seed import Seed


class Command(BaseCommand):
    help = 'This command is '

    def add_arguments(self, parser):
        parser.add_argument("--number", default=2, type=int,
                            help="How many photos create")

    def handle(self, *args, **options):
        number = options.get("number", 1)

        seeder = Seed.seeder()
        seeder.add_entity(photo_model.Photo, number)
        # python manage.py seed_users --numbers 50
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} photos created'))
