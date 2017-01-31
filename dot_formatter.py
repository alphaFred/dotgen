from .core import abc_dotgen_parser


class DotGenFormatter(abc_dotgen_parser.AbcDotGenBaseParser):
    def to_dot(self, node) -> str:
        pass

    def generic_visit(self, node) -> str:
        pass
