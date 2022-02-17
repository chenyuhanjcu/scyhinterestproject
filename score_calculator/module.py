from assessment import Assessment


class Module:

    def __init__(self, name=""):
        self.name = name
        self.assessments = []
        # self.current_score = current_score
        # self.unknown_score = unknown_score

    def __str__(self):
        out_string = f"{self.name} {self.is_finished()} with {self.get_total_score():.0f} earned.\nDetail:\n"
        for assessment in self.assessments:
            out_string += f"{assessment} "
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
            return "Finished"
        else:
            return "Unfinished"

    def get_total_score(self):
        # total_score = 0
        return sum(assessment.get_weighted_score() for assessment in self.assessments)

