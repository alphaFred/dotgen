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

