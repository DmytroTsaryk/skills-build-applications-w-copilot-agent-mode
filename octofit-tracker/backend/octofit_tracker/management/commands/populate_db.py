
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting all data using Django ORM...'))
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))

        marvel = Team.objects.create(id=1, name='Marvel')
        dc = Team.objects.create(id=2, name='DC')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        tony = User.objects.create(id=1, email='tony@stark.com', name='Tony Stark', team=marvel)
        steve = User.objects.create(id=2, email='steve@rogers.com', name='Steve Rogers', team=marvel)
        bruce = User.objects.create(id=3, email='bruce@wayne.com', name='Bruce Wayne', team=dc)
        clark = User.objects.create(id=4, email='clark@kent.com', name='Clark Kent', team=dc)

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        Activity.objects.create(id=1, user=tony, type='run', duration=30, distance=5)
        Activity.objects.create(id=2, user=steve, type='cycle', duration=60, distance=20)
        Activity.objects.create(id=3, user=bruce, type='swim', duration=45, distance=2)
        Activity.objects.create(id=4, user=clark, type='run', duration=50, distance=10)

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        Workout.objects.create(id=1, name='Morning Cardio', description='A quick morning run', duration=30)
        Workout.objects.create(id=2, name='Strength Training', description='Weight lifting session', duration=60)

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        Leaderboard.objects.create(id=1, user=tony, team=marvel, score=100)
        Leaderboard.objects.create(id=2, user=steve, team=marvel, score=90)
        Leaderboard.objects.create(id=3, user=bruce, team=dc, score=95)
        Leaderboard.objects.create(id=4, user=clark, team=dc, score=98)

        self.stdout.write(self.style.SUCCESS('Ensuring unique index on email field for users...'))
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client[settings.DATABASES['default']['NAME']]
        db['octofit_tracker_user'].create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
