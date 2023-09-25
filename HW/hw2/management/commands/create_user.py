from django.core.management.base import  BaseCommand
from hw2.models import User

class Command(BaseCommand):
    help = "Create User"
    def handle(self, *args, **kwargs):
        user = User(name='Vitaly', email='vital-nvl@mail.ru', password='pass', phone='89610000123', address='Bryansk')
        user.save()

        self.stdout.write(f'{user}')