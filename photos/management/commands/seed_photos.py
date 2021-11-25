from django.core.management.base import BaseCommand
from photos import models as photo_model
from django_seed import Seed
from django.contrib.admin.utils import flatten
from users import models as user_models
import random


class Command(BaseCommand):
    help = 'This command is '

    def add_arguments(self, parser):
        parser.add_argument("--number", default=2, type=int,
                            help="How many photos create")

    def handle(self, *args, **options):
        number = options.get("number", 1)

        all_users = user_models.User.objects.all()
        CAT_HAK = "학치"
        CAT_BBI = "삐약이"
        CAT_MOK = "목주"
        CAT_UNKNOWN = "모름"

        CAT_CHOICES = [CAT_HAK,
                       CAT_BBI,
                       CAT_MOK,
                       CAT_UNKNOWN,
                       ]
        seeder = Seed.seeder()
        seeder.add_entity(photo_model.Photo, number, {
            "cat_name": lambda x: random.choice(CAT_CHOICES),
            "description": lambda x: seeder.faker.sentence(),
        })
        # python manage.py seed_users --numbers 50
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        for pk in created_clean:
            photo = photo_model.Photo.objects.get(pk=pk)
            photo_model.File.objects.create(
                photo=photo,
                file=f"room_photos/{random.randint(1, 31)}.webp",
            )
        self.stdout.write(self.style.SUCCESS(f'{number} photos created'))
