import time
import os.path

class BuildPathAdv:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "path_base": ("STRING", {
                    "multiline": False,
                    "default": "C:\\",
                }),
                "path_prefix": ("STRING", {
                    "multiline": False,
                    "default": "[time(%Y-%m-%d)]",
                }),
                "path_delimiter": ("STRING", {
                    "multiline": False,
                    "default": "-",
                }),
                "path_postfix": ("STRING", {
                    "multiline": False,
                    "default": "",
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Path",)
    FUNCTION = "build_path"
    CATEGORY = "Build Path"

    def build_path(self, path_base, path_prefix, path_delimiter, path_postfix):
        return (os.path.join(path_base, (f"{path_prefix}{path_delimiter}{path_postfix}")),)

#class BuildPathNumerical:
#    def __init__(self):
#        pass

#    @classmethod
#    def INPUT_TYPES(s):
#        return {
#            "required": {
#                "path_base": ("STRING", {
#                    "multiline": False,
#                    "default": "C:\\",
#                }),
#                "path_number": ("INT", {
#                    "default": 0,
#                    "min": 0,
#                    "max": 10000
#                }),
#                "path_padding": ("INT", {
#                    "default": 4,
#                    "min": 0,
#                    "max": 10
#                }),
#            },
#        }

#    RETURN_TYPES = ("STRING",)
#    RETURN_NAMES = ("Path",)
#    FUNCTION = "build_path"
#    CATEGORY = "Build Path"

#    def build_path(self, path_base, path_number, path_padding):
#        return (f"{path_base}{path_number:0{path_padding}d}",)
