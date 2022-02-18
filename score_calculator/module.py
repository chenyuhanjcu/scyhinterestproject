from assessment import Assessment


class Module:

    def __init__(self, name=""):
        self.name = name
        self.assessments = []
        # self.is_finished = self.check_finished()
        # self.current_score = current_score
        # self.unknown_score = unknown_score

    def __str__(self):
        if self.is_finished():
            out_string = f"{self.name} finished with {self.get_total_score():.0f} earned."
        else:
            out_string = f"{self.name} unfinished with {self.get_total_score():.0f} earned."
        # for assessment in self.assessments:
        #     out_string += f"{assessment} "
        return out_string

    def add_assessments(new_assessment, self):
        if isinstance(new_assessment, Assessment):
            self.assessments.append(new_assessment)
            print(f"{new_assessment} added")

    def is_finished(self):
        total = 0
        for assessment in self.assessments:
            total += assessment.percentage
        if total == 1:
            return True
        # else:
        #     self.is_finished = False

    def get_total_score(self):
        return sum(assessment.get_weighted_score() for assessment in self.assessments)

