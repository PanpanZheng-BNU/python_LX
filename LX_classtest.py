class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if  0 <= self.score <=100:
            if self.score >= 80:
                return 'A'
            if self.score >= 60:
                return 'B'
            return 'C'
        else:
            raise ValueError('the score should between 0 and 100')
