class Score:
    def __init__(self):
        self.score = 100

    def count_score(self, x):
        self.score += x

    def get_score(self):
        return self.score
