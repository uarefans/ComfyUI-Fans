import csv
import os
import sys
import comfy.utils

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "styles", "styles-negative.csv")

class FansPromptStylerNegative:
    styles = None

    def __init__(self):
        pass
    
    def handle_prompt_change(self, value):
        print("New prompt value:", value)
    
    @classmethod
    def INPUT_TYPES(cls):
        if not os.path.exists(csv_file_path):
            cls.styles = [["No Styles.csv", "", ""]]
        else:
            with open(csv_file_path, "r") as f:
                reader = csv.reader(f, dialect='excel')
                cls.styles = [row for row in reader if len(row) == 2 and row[1] != "prompt" and row[0] != "None"]

        cls.styles.insert(0, ["None", "", ""])
        style_names = [row[0] for row in cls.styles]

        return {
            "required": {
                "style": (style_names, {"default": style_names[0]}),
                "structure": (["Beginning", "End"],{"default":"Beginning"}),               
                "prompt": ("STRING", {"multiline": True, "default": "Input Your Negative Prompt Here"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result",)
    FUNCTION = "func"
    OUTPUT_NODE = False
    CATEGORY = "utils"

    def func(self, style, structure, prompt):
        result=""

        if style=="None":
            result=prompt
        else:
            for row in self.styles:
                if row[0] == style:
                    result += row[1]              

            if structure == 'Beginning':
                result =  prompt + ", " + result
            else:
                result =  result + ", " + prompt

        return result,

NODE_CLASS_MAPPINGS = {
    "Fans Prompt Styler Negative": FansPromptStylerNegative
}
