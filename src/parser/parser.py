from lark import Lark, Transformer, Tree, Token

from src.render_engine.rendering_api import LynRenderingApi as Lyn
import src.render_engine.primitives as primitives
import src.render_engine.compounds as compounds

with open(__file__.removesuffix("parser.py") + "lyn.lark") as file:
    grammar = file.read()


def camel_to_snake(s):
    return ''.join(['_' + c.lower() if c.isupper() else c for c in s]).lstrip('_')


parser = Lark(grammar)

source_code = """
Animate {
  Circle my_circle {
    radius: 50,
    x: 100, y: 300
  }

  Rectangle my_rect {
    x: 500, y: 500,
    width: 200, height: 100, stroke_width: 10
  }

  Line my_line {
    x1: 700, y1: 20, x2: 100, y2: 700
  }

  play WriteLine {
    object: my_line
  }

  play FadeIn {
    object: my_rect
  }

  play Delay {
    duration: 2
  }

  play FadeIn {
    object: my_circle
  }

}
"""


# noinspection PyMethodMayBeStatic,PyPep8Naming
class Parser(Transformer):
    def __init__(self):
        super().__init__()
        self.globals = {}
        self.animate_sequence = []
        self.api = Lyn()
        self.api.init_window("Lyn Compiler", 1000, 800)

    def start(self, tokens):
        print(tokens)
        return tokens

    def main_assignment(self, tokens):
        rt_val = []
        for token in tokens:
            if type(token) == Token:
                rt_val.append(token.value)
        return tokens

    def assignment(self, tokens):
        var_type, var_name, kwargs = tokens
        object_class = getattr(primitives, var_type) or getattr(compounds, var_type)
        obj = self.globals[var_name] = object_class(**kwargs)
        return obj

    def animate_instruction(self, tokens):
        animation_type, animation_params = tokens[1], tokens[-1]
        if "object" in animation_params.keys():
            animation_params["primitive"] = animation_params["object"]
            del animation_params["object"]
        animation_type = getattr(self.api, camel_to_snake(animation_type))
        for key, val in animation_params.items():
            if type(val) == str:
                animation_params[key] = self.globals[val]
        animation_type(**animation_params)
        return animation_type, animation_params

    def python_blocks(self, tokens):
        print(tokens)
        return tokens

    def OBJECT(self, token):
        return token.value

    def var_name(self, tokens):
        string = ""
        for token in tokens:
            string += token
        return string

    def letter(self, tokens):
        string = ""
        for token in tokens:
            string += token.value
        return string

    def dict(self, tokens):
        return dict(tokens)

    def key_value_pair(self, tokens):
        key = tokens[0]
        value = tokens[-1]
        return key, value

    def value(self, tokens):
        return tokens[0]

    def number(self, tokens):
        num = ""
        for token in tokens:
            num += token.value
        return int(num)


p = Parser()
p.transform(parser.parse(source_code))
p.api.start_window_loop()
# print(parser.parse(source_code).pretty())
