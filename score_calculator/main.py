from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from module import Module
from module_collections import ModuleCollections
from kivy.properties import StringProperty

FILENAME = "score.txt"
DARK_BLUE = (0.2, 0.5, 0.7, 0.5)
LIGHT_BLUE = (0.2, 0.6, 0.9, 1)
SORT_METHODS = ["Finished", "Unfinished", "Module Name"]

class ScoreCalculatorApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.module_collection = ModuleCollections()
        self.module_collection.load_data(FILENAME)
        self.sort_methods = SORT_METHODS
        self.current_sort_method = self.sort_methods[1]

    def build(self):
        self.title = "Score Calculator"
        self.root = Builder.load_file("app.kv")
        self.create_widgets()
        # self.status_text = f"{[module.name for module in self.module_collection.modules]}"
        return self.root

    def create_widgets(self):
        for module in self.module_collection.modules:
            button = Button(text=str(module))
            button.bind(on_release=self.show_detail)  # cannot pass parameter
            button.module = module  # unless uses instance attribute
            if module.is_finished():
                button.background_color = DARK_BLUE
            else:
                button.background_color = LIGHT_BLUE
            self.root.ids.modules_box.add_widget(button)

    def add_module(self):
        title = self.root.ids.input_module.text
        if title == "" or title.isspace():
            self.status_text = "Invalid input."
        elif title in [module.name for module in self.module_collection.modules]:
            self.status_text = "Module exist."
        else:
            self.module_collection.add_module(Module(title))
        self.redisplay_modules()

    def show_detail(self, instance):
        detail = "Detail:\n"
        for assessment in instance.module.assessments:
            detail += str(assessment)
            detail += "\n"
        self.status_text = detail

    def redisplay_modules(self):
        self.root.ids.modules_box.clear_widgets()  # clear current movie status
        self.create_widgets()

    def change_sort_method(self, sort_method):
        self.module_collection.sort(sort_method)
        self.redisplay_modules()


if __name__ == '__main__':
    ScoreCalculatorApp().run()