import abc
import ast


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
