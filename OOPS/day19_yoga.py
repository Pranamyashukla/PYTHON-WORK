class Yoga:
    def __init__(self, level):
        self.level = level

    def display_level(self):
        print(f"Yoga Level: {self.level}")

class HathaYoga(Yoga):
    def pose(self):
        print("Hatha Yoga Pose: mountain pose")

class PowerYoga(Yoga):
    def pose(self):
        print("Power Yoga Pose: plank pose")

class MeditationYoga(Yoga):
    def pose(self):
        print("Meditation Yoga Pose: lotus pose")


y1 = HathaYoga("Beginner")
y2 = PowerYoga("Intermediate")
y3 = MeditationYoga("Advanced")

y1.display_level()
y1.pose()

print()

y2.display_level()
y2.pose()
print()
y3.display_level()
y3.pose()