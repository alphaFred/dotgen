from .core.abc_dotgen_labeler import AbcDotLabeler


class DotGenLabeler(AbcDotLabeler):
    def generic_visit(self, node) -> str:
        pass

    def label(self, node) -> str:
        pass
