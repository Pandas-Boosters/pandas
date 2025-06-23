from __future__ import annotations
from pandas.tseries.holiday import AbstractHolidayCalendar
import pandas as pd

from pandas._libs.tslibs.offsets import (
    FY5253,
    BaseOffset,
    BDay,
    BHalfYearBegin,
    BHalfYearEnd,
    BMonthBegin,
    BMonthEnd,
    BQuarterBegin,
    BQuarterEnd,
    BusinessDay,
    BusinessHour,
    BusinessMonthBegin,
    BusinessMonthEnd,
    BYearBegin,
    BYearEnd,
    CBMonthBegin,
    CBMonthEnd,
    CDay,
    CustomBusinessDay,
    CustomBusinessHour,
    CustomBusinessMonthBegin,
    CustomBusinessMonthEnd,
    DateOffset,
    Day,
    Easter,
    FY5253Quarter,
    HalfYearBegin,
    HalfYearEnd,
    Hour,
    LastWeekOfMonth,
    Micro,
    Milli,
    Minute,
    MonthBegin,
    MonthEnd,
    Nano,
    QuarterBegin,
    QuarterEnd,
    Second,
    SemiMonthBegin,
    SemiMonthEnd,
    Tick,
    Week,
    WeekOfMonth,
    YearBegin,
    YearEnd,
)

__all__ = [
    "FY5253",
    "BDay",
    "BHalfYearBegin",
    "BHalfYearEnd",
    "BMonthBegin",
    "BMonthEnd",
    "BQuarterBegin",
    "BQuarterEnd",
    "BYearBegin",
    "BYearEnd",
    "BaseOffset",
    "BusinessDay",
    "BusinessHour",
    "BusinessMonthBegin",
    "BusinessMonthEnd",
    "CBMonthBegin",
    "CBMonthEnd",
    "CDay",
    "CustomBusinessDay",
    "CustomBusinessHour",
    "CustomBusinessMonthBegin",
    "CustomBusinessMonthEnd",
    "DateOffset",
    "Day",
    "Easter",
    "FY5253Quarter",
    "HalfYearBegin",
    "HalfYearEnd",
    "Hour",
    "LastWeekOfMonth",
    "Micro",
    "Milli",
    "Minute",
    "MonthBegin",
    "MonthEnd",
    "Nano",
    "QuarterBegin",
    "QuarterEnd",
    "Second",
    "SemiMonthBegin",
    "SemiMonthEnd",
    "Tick",
    "Week",
    "WeekOfMonth",
    "YearBegin",
    "YearEnd",
]
# Eski Cython sınıfını Base olarak kullan
_OriginalCustomBusinessDay = CustomBusinessDay

class CustomBusinessDay(_OriginalCustomBusinessDay):
    def __init__(self, n=1, normalize=False, weekmask=None, holidays=None,
                 calendar=None, offset=None, **kwds):

        # Eğer calendar pandas_market_calendars gibi bir nesne ise, holidays üret
        if holidays is None and calendar is not None:
            if hasattr(calendar, "holidays") and callable(calendar.holidays):
                # PMC -> DatetimeIndex
                holidays = calendar.holidays().to_pydatetime()
            elif hasattr(calendar, "valid_days") and callable(calendar.valid_days):
                # Alternatif PMC uyumu
                schedule = calendar.schedule("2000-01-01", "2100-01-01")
                holidays = pd.date_range("2000-01-01", "2100-01-01").difference(schedule.index)

        # Orijinal Cython sınıfına parametreleri geçir
        super().__init__(
            n=n, normalize=normalize, weekmask=weekmask, holidays=holidays,
            calendar=None,  # calendar override edildi, zaten kullanılmıyor
            offset=offset, **kwds
        )
