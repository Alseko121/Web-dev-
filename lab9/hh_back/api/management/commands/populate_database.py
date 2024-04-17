from django.core.management.base import BaseCommand
from your_app.models import Company, Vacancy

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **kwargs):
        # Create sample companies
        company1 = Company.objects.create(name='Company 1', ...)
        company2 = Company.objects.create(name='Company 2', ...)
        # Add more companies as needed

        # Create sample vacancies
        vacancy1 = Vacancy.objects.create(name='Vacancy 1', company=company1, ...)
        vacancy2 = Vacancy.objects.create(name='Vacancy 2', company=company2, ...)


        self.stdout.write(self.sctyle.SUCCESS('Sample data successfully added to the database'))
