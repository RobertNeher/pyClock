from enum import Flag, auto

class TickType(Flag):
    HOURS_ONLY = auto()
    MINUTES_ONLY = auto()
    ALL = HOURS_ONLY | MINUTES_ONLY
