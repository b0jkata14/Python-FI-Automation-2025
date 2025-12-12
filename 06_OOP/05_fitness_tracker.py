class Exercise:
    def __init__(self, name, reps, weight_kg, difficulty):
        self.name = name
        self.reps = reps if reps > 0 else 1
        self.weight_kg = weight_kg if weight_kg >= 0 else 0

        difficulty = min(10, max(1, difficulty))

        self._difficulty = difficulty

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value):
        if 1 <= value <= 10:
            self._difficulty = value

    def total_load(self):
        return self.reps * self.weight_kg * self.difficulty


def rank_exercises(exercises):
    return sorted(
        exercises,
        key=lambda ex: (-ex.total_load(), ex.name)
    )