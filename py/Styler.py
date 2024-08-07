import csv
import os
import sys
import comfy.utils

# Global Config
csv_file_path1 = os.path.join(os.path.dirname(__file__), "..", "styles", "styles1.csv")
csv_file_path2 = os.path.join(os.path.dirname(__file__), "..", "styles", "styles2.csv")
csv_file_path3 = os.path.join(os.path.dirname(__file__), "..", "styles", "styles3.csv")
csv_file_path4 = os.path.join(os.path.dirname(__file__), "..", "styles", "styles4.csv")
csv_file_path5 = os.path.join(os.path.dirname(__file__), "..", "styles", "styles5.csv")
csv_file_path6 = os.path.join(os.path.dirname(__file__), "..", "styles", "styles6.csv")
csv_file_path7 = os.path.join(os.path.dirname(__file__), "..", "styles", "styles7.csv")
csv_file_path8 = os.path.join(os.path.dirname(__file__), "..", "styles", "styles8.csv")
csv_file_path9 = os.path.join(os.path.dirname(__file__), "..", "styles", "styles9.csv")
csv_file_path10 = os.path.join(os.path.dirname(__file__), "..", "styles", "styles10.csv")

class FansStyler:
    styles1 = None
    styles2 = None
    styles3 = None
    styles4 = None
    styles5 = None
    styles6 = None
    styles7 = None
    styles8 = None
    styles9 = None
    styles10 = None

    def __init__(self):
        pass


    @classmethod
    def INPUT_TYPES(cls):        
        #1
        if not os.path.exists(csv_file_path1):
            cls.styles1 = [["No Styles1.csv", "styles1", "styles1"]]
        else:
            with open(csv_file_path1, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                cls.styles1 = [row for row in reader if len(row) == 2 and row[1] != "prompt" and row[0] != "None"]
        #2                
        if not os.path.exists(csv_file_path2):
            cls.styles2 = [["No Styles2.csv", "styles2", "styles2"]]
        else:
            with open(csv_file_path2, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                cls.styles2 = [row for row in reader if len(row) == 2 and row[1] != "prompt" and row[0] != "None"]
        #3                
        if not os.path.exists(csv_file_path3):
            cls.styles3 = [["No Styles3.csv", "styles3", "styles3"]]
        else:
            with open(csv_file_path3, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                cls.styles3 = [row for row in reader if len(row) == 2 and row[1] != "prompt" and row[0] != "None"]
        #4                
        if not os.path.exists(csv_file_path4):
            cls.styles4 = [["No Styles4.csv", "styles4", "styles4"]]
        else:
            with open(csv_file_path4, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                cls.styles4 = [row for row in reader if len(row) == 2 and row[1] != "prompt" and row[0] != "None"]
        #5                
        if not os.path.exists(csv_file_path5):
            cls.styles5 = [["No Styles5.csv", "styles5", "styles5"]]
        else:
            with open(csv_file_path5, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                cls.styles5 = [row for row in reader if len(row) == 2 and row[1] != "prompt" and row[0] != "None"]
        #6
        if not os.path.exists(csv_file_path6):
            cls.styles6 = [["No Styles6.csv", "styles6", "styles6"]]
        else:
            with open(csv_file_path6, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                cls.styles6 = [row for row in reader if len(row) == 2 and row[1] != "prompt" and row[0] != "None"]
        #7
        if not os.path.exists(csv_file_path7):
            cls.styles7 = [["No Styles7.csv", "styles7", "styles7"]]
        else:
            with open(csv_file_path7, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                cls.styles7 = [row for row in reader if len(row) == 2 and row[1] != "prompt" and row[0] != "None"]
        #8                
        if not os.path.exists(csv_file_path8):
            cls.styles8 = [["No Styles8.csv", "Styles8", "Styles8"]]
        else:
            with open(csv_file_path8, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                cls.styles8 = [row for row in reader if len(row) == 2 and row[1] != "prompt" and row[0] != "None"]
        #9
        if not os.path.exists(csv_file_path9):
            cls.styles9 = [["No Styles9.csv", "styles9", "styles9"]]
        else:
            with open(csv_file_path9, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                cls.styles9 = [row for row in reader if len(row) == 2 and row[1] != "prompt" and row[0] != "None"]
        #10
        if not os.path.exists(csv_file_path10):
            cls.styles10 = [["No Styles10.csv", "styles10", "styles10"]]
        else:
            with open(csv_file_path10, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                cls.styles10 = [row for row in reader if len(row) == 2 and row[1] != "prompt" and row[0] != "None"]

        cls.styles1.insert(0, ["None", ""])
        cls.styles2.insert(0, ["None", ""])
        cls.styles3.insert(0, ["None", ""])
        cls.styles4.insert(0, ["None", ""])
        cls.styles5.insert(0, ["None", ""])
        cls.styles6.insert(0, ["None", ""])
        cls.styles7.insert(0, ["None", ""])
        cls.styles8.insert(0, ["None", ""])
        cls.styles9.insert(0, ["None", ""])
        cls.styles10.insert(0, ["None", ""])

        style_names1 = [row[0] for row in cls.styles1]
        style_names2 = [row[0] for row in cls.styles2]
        style_names3 = [row[0] for row in cls.styles3]
        style_names4 = [row[0] for row in cls.styles4]
        style_names5 = [row[0] for row in cls.styles5]
        style_names6 = [row[0] for row in cls.styles6]
        style_names7 = [row[0] for row in cls.styles7]
        style_names8 = [row[0] for row in cls.styles8]
        style_names9 = [row[0] for row in cls.styles9]
        style_names10 = [row[0] for row in cls.styles10]

        return {
            "required": {
                "with_comma_condition": (["Yes", "No"],{"default":"Yes"}),               
                "style1": (style_names1, {"default": style_names1[1]}),
                "style2": (style_names2, {"default": style_names2[1]}),
                "style3": (style_names3, {"default": style_names3[1]}),
                "style4": (style_names4, {"default": style_names4[1]}),
                "style5": (style_names5, {"default": style_names5[1]}),
                "style6": (style_names6, {"default": style_names6[1]}),
                "style7": (style_names7, {"default": style_names7[1]}),
                "style8": (style_names8, {"default": style_names8[1]}),
                "style9": (style_names9, {"default": style_names9[1]}),
                "style10": (style_names10, {"default": style_names10[1]}),
            },
        }

    RETURN_TYPES = ("STRING","STRING","STRING","STRING","STRING","STRING","STRING","STRING","STRING","STRING",)
    RETURN_NAMES = ("STYLE 1", "STYLE 2", "STYLE 3", "STYLE 4", "STYLE 5", "STYLE 6", "STYLE 7", "STYLE 8", "STYLE 9", "STYLE 10",)
    FUNCTION = "func"
    OUTPUT_NODE = False
    CATEGORY = "utils"

    def func(self, with_comma_condition, style1, style2, style3, style4, style5, style6, style7, style8, style9, style10):
        result1 = ""
        result2 = ""
        result3 = ""
        result4 = ""
        result5 = ""
        result6 = ""
        result7 = ""
        result8 = ""
        result9 = ""
        result10 = ""

        #1
        if style1 == "None":
            result1 = ""
        else:
            for row in self.styles1:
                if row[0] == style1:
                    if with_comma_condition == 'Yes':
                        result1 += row[1] + ", "
                    else:
                        result1 += row[1] + " "
        #2
        if style2 == "None":
            result2 = ""
        else:
            for row in self.styles2:
                if row[0] == style2:
                    if with_comma_condition == 'Yes':
                        result2 += row[1] + ", "
                    else:
                        result2 += row[1] + " "
        #3
        if style3 == "None":
            result3 = ""
        else:
            for row in self.styles3:
                if row[0] == style3:
                    if with_comma_condition == 'Yes':
                        result3 += row[1] + ", "
                    else:
                        result3 += row[1] + " "
        #4
        if style4 == "None":
            result4 = ""
        else:
            for row in self.styles4:
                if row[0] == style4:
                    if with_comma_condition == 'Yes':
                        result4 += row[1] + ", "
                    else:
                        result4 += row[1] + " "
        #5
        if style5 == "None":
            result5 = ""
        else:
            for row in self.styles5:
                if row[0] == style5:
                    if with_comma_condition == 'Yes':
                        result5 += row[1] + ", "
                    else:
                        result5 += row[1] + " "
        #6
        if style6 == "None":
            result6 = ""
        else:
            for row in self.styles6:
                if row[0] == style6:
                    if with_comma_condition == 'Yes':
                        result6 += row[1] + ", "
                    else:
                        result6 += row[1] + " "
        #7
        if style7 == "None":
            result7 = ""
        else:
            for row in self.styles7:
                if row[0] == style7:
                    if with_comma_condition == 'Yes':
                        result7 += row[1] + ", "
                    else:
                        result7 += row[1] + " "
        #8
        if style8 == "None":
            result8 = ""
        else:
            for row in self.styles8:
                if row[0] == style8:
                    if with_comma_condition == 'Yes':
                        result8 += row[1] + ", "
                    else:
                        result8 += row[1] + " "
        #9
        if style9 == "None":
            result9 = ""
        else:
            for row in self.styles9:
                if row[0] == style9:
                    if with_comma_condition == 'Yes':
                        result9 += row[1] + ", "
                    else:
                        result9 += row[1] + " "
        #10
        if style10 == "None":
            result10 = ""
        else:
            for row in self.styles10:
                if row[0] == style10:
                    if with_comma_condition == 'Yes':
                        result10 += row[1] + ", "
                    else:
                        result10 += row[1] + " "

        return result1, result2, result3, result4, result5, result6, result7, result8, result9, result10

NODE_CLASS_MAPPINGS = {
    "Fans Styler": FansStyler,
}
