from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'This command is '

    def add_arguments(self, parser):
        parser.add_argument("--times", help="How much")

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(0, times):
            print("I love u")
