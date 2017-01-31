import abc
import ast


class AbcDotGenBaseParser(abc.ABC, ast.NodeVisitor):
    def __init__(self, node_formatter=None, node_labeler=None):
        """

        Args:
            node_labeler ():
        """
        super(AbcDotGenBaseParser, self).__init__()
        self.labeler = node_labeler.label()
        self.formatter = node_formatter

    @abc.abstractmethod
    def to_dot(self, node) -> str:
        pass

    def label(self, node) -> str:
        if self.labeler is not None:
            node_label = self.labeler.label(node)
        else:
            node_label = ""
        return r"%s\n%s" % (type(node).__name__, node_label)

    def format(self, node) -> str:
        if self.formatter is not None:
            return self.formatter.format(node)
        else:
            return ""

    @abc.abstractmethod
    def generic_visit(self, node) -> str:
        pass
