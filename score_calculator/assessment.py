class Assessment:
    def __init__(self, name="", score=0, max_score=0, percentage=0):
        self.name = name
        self.score = float(score)
        self.max_score = float(max_score)
        self.percentage = float(percentage)

    def __str__(self):
        return f"{self.name}({self.score}/{self.max_score}){self.percentage*100}%"

    def get_score_percentage(self):
        return f"{self.score/self.max_score*100}%"

    def get_weighted_score(self):
        return self.score*self.percentage

# exam = Assessment("exam", 80, 100, 0.5)
# print(exam.get_weighted_score())
# print(exam)
# print(exam.get_score_percentage())


        #     assessment_name = ""
        #     name = [string for string in assessment if string.isalpha()]
        #     for alpha in name:
        #         assessment_name += alpha
        #     print(assessment_name)
        # print(module_name, assessments)

# load_data(FILENAME)