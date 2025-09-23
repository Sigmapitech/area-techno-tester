import re


class TableNameProvider:
    def __init_subclass__(cls, **kwargs):
        cls.__tablename__ = re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower()
        super().__init_subclass__(**kwargs)
