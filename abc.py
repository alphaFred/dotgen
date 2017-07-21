import abc
import ast


class AbcDotFormatter(abc.ABC, ast.NodeVisitor):
    @abc.abstractmethod
    def format(self, node) -> str:
        """
        Return dot format commands for node
        Args:
            node: node to format

        Returns:
            str: dot format command
        """
        return ""

    @abc.abstractmethod
    def generic_visit(self, node) -> str:
        """
        Return dot format commands for node
        Args:
            node: node to format

        Returns:
            str: generic dot format command for node
        """
        return ""


class AbcDotLabeler(abc.ABC, ast.NodeVisitor):
    @abc.abstractmethod
    def label(self, node) -> str:
        """
        Return label for node
        Args:
            node: node to label

        Returns:
            str: label for node
        """
        return ""

    @abc.abstractmethod
    def generic_visit(self, node) -> str:
        """
        Return generic label for node
        Args:
            node: node to label

        Returns:
            str: generic label for node
        """
        return ""


class AbcDotGenBaseParser(abc.ABC, ast.NodeVisitor):
    """
    ABC for parsing an AST.
    """
    def __init__(self, node_formatter=None, node_labeler=None):
        """
        Initialize node parser and inject formatter and labeler
        Args:
            node_labeler: node visitor implementing |AbcDotLabeler|
            node_formatter: node visitor implementing [AbcDotFormatter]
        """
        super(AbcDotGenBaseParser, self).__init__()
        self.labeler = node_labeler
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
