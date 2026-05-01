from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes team')
        dc = Team.objects.create(name='DC', description='DC superheroes team')

        # Create Users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create Workouts
        workout1 = Workout.objects.create(name='Super Strength', description='Strength training for heroes')
        workout2 = Workout.objects.create(name='Agility Drill', description='Agility and speed workout')
        workout1.suggested_for.set(users)
        workout2.suggested_for.set(users)

        # Create Activities
        Activity.objects.create(user=users[0], activity_type='Web Swing', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], activity_type='Suit Upgrade', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], activity_type='Lasso Practice', duration=40, date=timezone.now().date())
        Activity.objects.create(user=users[3], activity_type='Batmobile Training', duration=50, date=timezone.now().date())

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=120, rank=1)
        Leaderboard.objects.create(user=users[1], score=110, rank=2)
        Leaderboard.objects.create(user=users[2], score=105, rank=3)
        Leaderboard.objects.create(user=users[3], score=100, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
