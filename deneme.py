import numpy as np
import pytest

from pandas.errors import InvalidIndexError

from pandas.core.dtypes.common import (
    is_float_dtype,
    is_scalar,
)

from pandas import (
    NA,
    DatetimeIndex,
    Index,
    IntervalIndex,
    MultiIndex,
    NaT,
    PeriodIndex,
    TimedeltaIndex,
)
import pandas._testing as tm
# This is true
i = Index([], name='a')
assert i.name == 'a'
assert i.names == ('a',)

# This is false (fails assertion)
i = Index([], names=('a',))
assert i.name == 'a'
assert i.names == ('a',)