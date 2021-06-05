from django.core.management.base import BaseCommand

from lostcats.models import LostCat


class Command(BaseCommand):
    help = "(Re)generate thumbnails for all lost cat models."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for cat in LostCat.objects.all():
            self.stdout.write(
                "Generating thumbnails for LostCat %s... " % cat, ending=""
            )
            cat.generate_thumbnails()
            cat.save()
            self.stdout.write("OK")
