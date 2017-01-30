import ast


def enumerate_flatten(obj_or_list):
    """Iterator for all objects arbitrarily nested in lists."""
    if isinstance(obj_or_list, list):
        for n, gen in enumerate(map(enumerate_flatten, obj_or_list)):
            for k, elem in gen:
                yield (n,)+k, elem
    else:
        yield (), obj_or_list


class DotGenVisitor(ast.NodeVisitor):
    """
    Generates a representation of the AST in the DOT graph language.
    See http://en.wikipedia.org/wiki/DOT_(graph_description_language)
    """
    def label(self, node):
        """
        A string to provide useful information for visualization, debugging, etc.
        """
        return r"%s\n%s" % (type(node).__name__, node.label())

    def format(self, node):
        """ Format Dot nodes. """
        formats = {"VhdlModule": ', style=filled, fillcolor="#00EB5E"',
                   "VhdlBinaryOp": ', style=filled, fillcolor="#C2FF66"',
                   "VhdlComponent": ', style=filled, fillcolor="#C2FF66"',
                   "VhdlReturn": ', style=filled, fillcolor="#C2FF66"',
                   "VhdlDReg": ', style=filled, shape=rect, fillcolor="#99CCFF"',
                   "VhdlSource": ', style=filled, fillcolor="#FFF066"',
                   "VhdlSink": ', style=filled, fillcolor="#FFF066"',
                   "VhdlConstant": ', style=filled, fillcolor="#FFF066"'
                   }
        return formats.get(type(node).__name__, "")

    def generic_visit(self, node):

        # label this node
        out_string = 'n{0} [label="{1}"{2}];\n'.\
            format(id(node), self.label(node), self.format(node))

        # edges to children
        for fieldname, fieldvalue in ast.iter_fields(node):
            for index, child in enumerate_flatten(fieldvalue):
                if isinstance(child, ast.AST):
                    suffix = "".join(["[%d]" % i for i in index])
                    out_string += 'n{} -> n{} [label="{}{}"];\n'.format(
                        id(node), id(child), fieldname, suffix)
                    out_string += self.visit(child)
        return out_string
