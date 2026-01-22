from pandas._stubs_only import IndexSubclassBase

from pandas._typing import (
    S1,
    GenericT_co,
)
from typing import Generic

# class ExtensionIndex(IndexSubclassBase[S1, GenericT_co]): ...
class ExtensionIndex(Generic[S1, GenericT_co]): ...
