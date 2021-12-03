"""TodoTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Todo import Todo

class TodoTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Todo.create({"subject": "Breakfast", "details": "eat breakfast"})
        Todo.create({"subject": "Lunch", "details": "eat Lunch"})
        Todo.create({"subject": "Dinner", "details": "eat Dinner"})
