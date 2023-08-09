import csv
import os
import sys

TEXT_TYPE = "STRING"

class FansTextConcatenate:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_a": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "linebreak_addition": (['false','true'], ),
            },
            "optional": {
                "text_b": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_c": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_d": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_e": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_f": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_g": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_h": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_i": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_j": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "text_concatenate"
    CATEGORY = "utils"

    def text_concatenate(self, text_a, text_b=None, text_c=None, text_d=None, text_e=None, text_f=None, text_g=None, text_h=None, text_i=None, text_j=None, linebreak_addition='false'):
        return_text = text_a + ("\n" if linebreak_addition == 'true' else '')
        if text_b:
            return_text = return_text + ("\n" if linebreak_addition == 'true' else '') + text_b
        if text_c:
            return_text = return_text + ("\n" if linebreak_addition == 'true' else '') + text_c
        if text_d:
            return_text = return_text + ("\n" if linebreak_addition == 'true' else '') + text_d
        if text_e:
            return_text = return_text + ("\n" if linebreak_addition == 'true' else '') + text_e
        if text_f:
            return_text = return_text + ("\n" if linebreak_addition == 'true' else '') + text_f
        if text_g:
            return_text = return_text + ("\n" if linebreak_addition == 'true' else '') + text_g
        if text_h:
            return_text = return_text + ("\n" if linebreak_addition == 'true' else '') + text_h
        if text_i:
            return_text = return_text + ("\n" if linebreak_addition == 'true' else '') + text_i
        if text_j:
            return_text = return_text + ("\n" if linebreak_addition == 'true' else '') + text_j
        return (return_text, )

NODE_CLASS_MAPPINGS = {
    "Fans Text Concatenate": FansTextConcatenate,
}