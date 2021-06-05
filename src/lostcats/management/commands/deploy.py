import getpass

from django.core.management.base import BaseCommand

from fabric import Connection, Config


class Command(BaseCommand):
    help = "Deploy the application."

    MANAGE_PY = "/home/joel/.cache/pypoetry/virtualenvs/lostcat-3wBeGhIi-py3.8/bin/python manage.py"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        sudo_pass = getpass.getpass("Enter sudo password for the remote user:\n")
        config = Config(overrides={"sudo": {"password": sudo_pass}})
        with Connection("lostcatithaca.com", config=config) as c:
            with c.cd("lostcat/src"):
                c.run("git pull")
                c.run("/home/joel/.poetry/bin/poetry install")
                c.run(f"{self.MANAGE_PY} check --deploy --fail-level=WARNING")
                c.run(f"{self.MANAGE_PY} migrate")
                c.run(f"{self.MANAGE_PY} collectstatic --clear --no-input")
            c.sudo(f"systemctl reload lostcat.service")

        print("\nOK!\n")
