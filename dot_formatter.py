from .core import AbcDotFormatter


class DotGenFormatter(AbcDotFormatter):
    def __init__(self, color_scheme="pastel19"):
        """
        Initialize dot formatter, add attributes for node groups and set
        color scheme
        Args:
            color_scheme (str): graphviz color scheme (only schemes with 9
            colors are supported!)
        """
        super(DotGenFormatter, self).__init__()
        if not color_scheme.endswith("9"):
            raise AttributeError("Only color schemes with 9 elements "
                                 "supported!")
        self.color_scheme = color_scheme
        self.format_string = "style={style}, colorscheme={scheme}, " \
                             "fillcolor={fcolor}, color={color}"
        # add visitor methods for node groups

        expr_contexts = ["Load", "Store", "Del", "AugLoad", "AugStore", "Param"]
        [setattr(self, "visit_" + i, self.visit_ExprContext)
         for i in expr_contexts]

        operators = ["Add", "Sub", "Mult", "MatMult", "Div", "Mod", "Pow",
                     "LShift", "RShift", "BitOr", "BitXor", "BitAnd",
                     "FloorDiv"]
        [setattr(self, "visit_" + i, self.visit_Operator)
         for i in operators]

        expr = ["BoolOp", "BinOp", "UnaryOp", "Lambda", "IfExp", "Dict", "Set",
                "ListComp", "SetComp", "DictComp", "GeneratorExp", "Await",
                "Yield", "YieldFrom", "Compare", "Call", "Num", "Str",
                "FormattedValue", "JoinedStr", "Bytes", "NameConstant",
                "Ellipsis", "Constant", "Attribute", "Subscript", "Starred",
                "Name", "List", "Tuple"]
        [setattr(self, "visit_" + i, self.visit_Expr)
         for i in expr]

        stmt = ["FunctionDef", "AsyncFunctionDef", "ClassDef", "expr",
                "keyword", "stmt", "expr", "Return", "Delete", "Assign",
                "AugAssign", "AnnAssign", "For", "AsyncFor", "While", "If",
                "With", "AsyncWith", "Raise", "Try", "Assert", "Import",
                "ImportFrom", "Global", "Nonlocal", "Expr", "Pass", "Break",
                "Continue"]
        [setattr(self, "visit_" + i, self.visit_Stmt)
         for i in stmt]

    def format(self, node) -> str:
        return self.visit(node)

    def visit_Stmt(self, node):
        return self.format_string.format(style="filled",
                                         scheme=self.color_scheme,
                                         fcolor=4,
                                         color="black")

    def visit_Expr(self, node):
        return self.format_string.format(style="filled",
                                         scheme=self.color_scheme,
                                         fcolor=6,
                                         color="black")

    def visit_Operator(self, node):
        return self.format_string.format(style="filled",
                                         scheme=self.color_scheme,
                                         fcolor=3,
                                         color="black")

    def visit_ExprContext(self, node):
        return self.format_string.format(style="filled",
                                         scheme=self.color_scheme,
                                         fcolor="white",
                                         color="black")

    def generic_visit(self, node) -> str:
        return self.format_string.format(style="filled",
                                         scheme=self.color_scheme,
                                         fcolor=9,
                                         color="black")
