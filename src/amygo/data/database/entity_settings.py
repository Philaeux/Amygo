from sqlalchemy.orm import Mapped, mapped_column

from amygo.data.database.entity_base import BaseEntity


class SettingsEntity(BaseEntity):
    """Table for application settings. Effectively using one row

    Attributes:
        key: unique string defining a setting
    """
    __tablename__ = 'settings'

    key: Mapped[str] = mapped_column(primary_key=True)
    addition_enabled: Mapped[bool] = mapped_column()
    addition_minimum: Mapped[int] = mapped_column()
    addition_maximum: Mapped[int] = mapped_column()
    subtraction_enabled: Mapped[bool] = mapped_column()
    subtraction_allow_negative: Mapped[bool] = mapped_column()
    subtraction_minimum: Mapped[int] = mapped_column()
    subtraction_maximum: Mapped[int] = mapped_column()
    multiplication_enabled: Mapped[bool] = mapped_column()
    multiplication_minimum: Mapped[int] = mapped_column()
    multiplication_maximum: Mapped[int] = mapped_column()
    division_enabled: Mapped[bool] = mapped_column()
    division_force_int: Mapped[bool] = mapped_column()
    division_dividend_minimum: Mapped[int] = mapped_column()
    division_dividend_maximum: Mapped[int] = mapped_column()
    division_divisor_minimum: Mapped[int] = mapped_column()
    division_divisor_maximum: Mapped[int] = mapped_column()

    def __init__(self, key, addition_enabled=True, addition_minimum=0, addition_maximum=20, subtraction_enabled=True,
                 subtraction_allow_negative=True, subtraction_minimum=-10, subtraction_maximum=10,
                 multiplication_enabled=True, multiplication_minimum=0, multiplication_maximum=11,
                 division_enabled=True, division_force_int=True, division_dividend_minimum=1,
                 division_dividend_maximum=10, division_divisor_minimum=0, division_divisor_maximum=10):
        self.key = key
        self.addition_enabled = addition_enabled
        self.addition_minimum = addition_minimum
        self.addition_maximum = addition_maximum
        self.subtraction_enabled = subtraction_enabled
        self.subtraction_allow_negative = subtraction_allow_negative
        self.subtraction_minimum = subtraction_minimum
        self.subtraction_maximum = subtraction_maximum
        self.multiplication_enabled = multiplication_enabled
        self.multiplication_minimum = multiplication_minimum
        self.multiplication_maximum = multiplication_maximum
        self.division_enabled = division_enabled
        self.division_force_int = division_force_int
        self.division_dividend_minimum = division_dividend_minimum
        self.division_dividend_maximum = division_dividend_maximum
        self.division_divisor_minimum = division_divisor_minimum
        self.division_divisor_maximum = division_divisor_maximum

    def __repr__(self) -> str:
        return f"SettingsEntity(key={self.key!r}, addition_minimum={self.addition_minimum!r}, " \
               f"addition_maximum={self.addition_maximum})"
