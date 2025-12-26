from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], activity_type='Running', duration_minutes=30, date=date.today())
        Activity.objects.create(user=users[1], activity_type='Cycling', duration_minutes=45, date=date.today())
        Activity.objects.create(user=users[2], activity_type='Swimming', duration_minutes=60, date=date.today())
        Activity.objects.create(user=users[3], activity_type='Yoga', duration_minutes=40, date=date.today())

        # Create workouts
        w1 = Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout')
        w2 = Workout.objects.create(name='Strength Training', description='Build muscle strength')
        w1.suggested_for.set([users[0], users[2]])
        w2.suggested_for.set([users[1], users[3]])

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, total_points=150, rank=1)
        Leaderboard.objects.create(team=dc, total_points=120, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
