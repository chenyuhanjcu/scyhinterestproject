from module import Module
from assessment import Assessment
from operator import attrgetter


class ModuleCollections:
    def __init__(self):
        self.modules = []

    def load_data(self, filename):
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
            # print(module)
            # print("")
            # print(module.get_total_score())
            self.modules.append(module)
        print(*self.modules)

    def add_module(self, module):
        if isinstance(module, Module):
            self.modules.append(module)

    def sort(self, sort_method):
        if sort_method == "Finished":
            self.modules.sort(key=attrgetter("is_finished"))
        elif sort_method == "Unfinished":
            self.modules.sort(key=attrgetter("name"))
        elif sort_method == "Module Name":
            self.modules.sort(key=attrgetter("name"))

# load_data(FILENAME)
# modules = ModuleCollections()
# modules.load_data("score.txt")