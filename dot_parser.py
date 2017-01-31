import ast

from .core.abc_dotgen_parser import AbcDotGenBaseParser


def enumerate_flatten(obj_or_list):
    """Iterator for all objects arbitrarily nested in lists."""
    if isinstance(obj_or_list, list):
        for n, gen in enumerate(map(enumerate_flatten, obj_or_list)):
            for k, elem in gen:
                yield (n,)+k, elem
    else:
        yield (), obj_or_list


class DotGenParser(AbcDotGenBaseParser):
    """
    Generates a representation of the AST in the DOT graph language.
    See http://en.wikipedia.org/wiki/DOT_(graph_description_language)
    """
    def to_dot(self, node):
        return "digraph dotTree {{\n{0}}}".format(self.visit(node))

    def generic_visit(self, node):
        # label this node
        out_string = 'n{0} [label="{1}"{2}];\n'.\
            format(id(node), self.label(node), self.format(node))

        # edges to children
        for field_name, field_value in ast.iter_fields(node):
            for index, child in enumerate_flatten(field_value):
                if isinstance(child, ast.AST):
                    suffix = "".join(["[%d]" % i for i in index])
                    out_string += 'n{} -> n{} [label="{}{}"];\n'.format(
                        id(node), id(child), field_name, suffix)
                    out_string += self.visit(child)
        return out_string
