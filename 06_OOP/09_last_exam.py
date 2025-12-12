class StudentGrade:
    min_points = 60

    def __init__(self, name, points):
        self.name = name
        self.points = points

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        if value < 0:
            value = 0

        self.__points = value

    @property
    def passed(self):
        return self.points >= StudentGrade.min_points

    @classmethod
    def set_pass_threshold(cls, points):
        cls.min_points = max(0, int(points))