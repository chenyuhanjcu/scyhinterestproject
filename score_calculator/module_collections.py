from module import Module
from assessment import Assessment
FILENAME = "score.txt"


def load_data(filename):
    with open(filename, "r") as in_file:
        lines = in_file.readlines()
    for line in lines:
        line = line.strip().split(",")
        module = Module(line[0])
        assessments = line[1:]
        for assessment in assessments:
            assessment_detail = assessment.split("_")
            name = assessment_detail[0]
            score = assessment_detail[1]
            max_score = assessment_detail[2]
            percentage = assessment_detail[3]
            new_assessment = Assessment(name, score, max_score, percentage)
            # print(new_assessment)
            module.assessments.append(new_assessment)
        print(module)
        print("")
        # print(module.get_total_score())

load_data(FILENAME)