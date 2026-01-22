from collections.abc import Hashable
import datetime

import numpy as np
import pandas as pd
from pandas.core.indexes.accessors import PeriodIndexFieldOps
from pandas.core.indexes.datetimelike import DatetimeIndexOpsMixin

from pandas._libs.tslibs import (
    Period,
)
from pandas._typing import (
    Frequency,
)

class PeriodIndex(DatetimeIndexOpsMixin[Period, np.object_], PeriodIndexFieldOps):
    ...
    # def __new__(
    #     cls,
    #     data: AxesData | None = None,
    #     freq: Frequency | None = None,
    #     dtype: Dtype | None = None,
    #     copy: bool = False,
    #     name: Hashable | None = None,
    # ) -> Self: ...
    # @property
    # def values(self) -> np_1darray_object: ...
    # def __add__(  # type: ignore[override] # pyright: ignore[reportIncompatibleMethodOverride] # pyrefly: ignore[bad-override] # ty: ignore[invalid-method-override]
    #     self, other: datetime.timedelta
    # ) -> Self: ...
    # def __radd__(  # type: ignore[override] # pyright: ignore[reportIncompatibleMethodOverride] # pyrefly: ignore[bad-override] # ty: ignore[invalid-method-override]
    #     self, other: datetime.timedelta
    # ) -> Self: ...
    # @overload  # type: ignore[override]
    # def __sub__(self, other: Period) -> Index: ...  # pyrefly: ignore[bad-override]
    # @overload
    # def __sub__(self, other: Self) -> Index: ...
    # @overload
    # def __sub__(self, other: PeriodAddSub) -> Self: ...
    # @overload
    # def __sub__(self, other: NaTType) -> NaTType: ...
    # @overload
    # def __sub__(  # pyright: ignore[reportIncompatibleMethodOverride] # ty: ignore[invalid-method-override]
    #     self, other: TimedeltaIndex | pd.Timedelta
    # ) -> Self: ...
    # @overload  # type: ignore[override]
    # def __rsub__(self, other: Period) -> Index: ...  # pyrefly: ignore[bad-override]
    # @overload
    # def __rsub__(self, other: Self) -> Index: ...
    # @overload
    # def __rsub__(  # pyright: ignore[reportIncompatibleMethodOverride] # ty: ignore[invalid-method-override]
    #     self, other: NaTType
    # ) -> NaTType: ...
    # def asof_locs(
    #     self, where: pd.DatetimeIndex | Self, mask: np_ndarray_bool
    # ) -> np_1darray_intp: ...
    # @property
    # def is_full(self) -> bool: ...
    # @property
    # def inferred_type(self) -> str: ...
    # @property
    # def freqstr(self) -> str: ...
    # def shift(self, periods: int = 1, freq: Frequency | None = None) -> Self: ...

def period_range(
    start: (
        str | datetime.datetime | datetime.date | pd.Timestamp | pd.Period | None
    ) = None,
    end: (
        str | datetime.datetime | datetime.date | pd.Timestamp | pd.Period | None
    ) = None,
    periods: int | None = None,
    freq: Frequency | None = None,
    name: Hashable | None = None,
) -> PeriodIndex: ...
