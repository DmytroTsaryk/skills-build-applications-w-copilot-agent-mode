from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name="Marvel", description="Marvel Team")
        user = User.objects.create(name="Iron Man", email="ironman@marvel.com", team=team)
        self.assertEqual(user.name, "Iron Man")
        self.assertEqual(user.team.name, "Marvel")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="DC", description="DC Team")
        self.assertEqual(team.name, "DC")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name="Marvel", description="Marvel Team")
        user = User.objects.create(name="Hulk", email="hulk@marvel.com", team=team)
        activity = Activity.objects.create(user=user, type="Running", duration=30, date="2024-01-01")
        self.assertEqual(activity.type, "Running")
        self.assertEqual(activity.user.name, "Hulk")

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Pushups", description="Upper body workout")
        self.assertEqual(workout.name, "Pushups")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Marvel", description="Marvel Team")
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.team.name, "Marvel")
        self.assertEqual(leaderboard.points, 100)
