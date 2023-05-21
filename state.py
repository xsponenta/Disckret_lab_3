"""
Module for states
"""

from enum import Enum

class State(Enum):
    """
    Class for my states
    """
    COFFEE = 1
    STUDY = 2
    REST = 3
    EAT = 4
    ROAD = 5

class Place(Enum):
    """
    Class for my locations
    """
    UNI = 1
    HOME = 2
    CAFE = 3
    SOMEWHERE = 4

class ActRoad:
    """
    Action for road
    """
    def __init__(self, start: float, duration: float,
finish: Place, action_type = State.ROAD):
        self.start = start
        self.duration = duration
        self.finish = finish
        self.action_type = action_type

class ActRoadRes:
    """
    Results for road action
    """
    def __init__(self, duration: float, 
finish: Place, success: bool = True):
        self.duration = duration
        self.finish = finish
        self.success = success

class Education(Enum):
    """
    Class for my type of education
    """
    OP = 1
    DISCKRET = 2
    MATAN = 3
    ELSE = 4

class ActT(Enum):
    """
    Enum class for work action types
    """
    IMMEDIATE = 1
    WITH_DEADLINE = 2
    SECONDARY = 3

class ActEdu:
    """
    Education actions
    """
    def __init__(self, start: float, duration: float, 
edu_type: Education, action_type = State.STUDY):
        self.duration = duration
        self.start = start
        self.edu_type = edu_type
        self.action_type = action_type

class ActEduRes:
    """
    Result of education
    """
    def __init__(self, place: Place, success: bool = True):
        self.place = place
        self.success = success

class Rest(Enum):
    """
    Class for my rest
    """
    LONG = 1
    SHORT = 2

class ActRest:
    """
    Rest actions
    """
    def __init__(self, start: float, duration: float,
rest_type: Rest, action_type: State = State.REST):
        self.start = start
        self.duration = duration
        self.rest_type = rest_type
        self.action_type = action_type

class AcrRestRes:
    """
    Result of rest
    """
    def __init__(self, finish: float, place: Place, success:bool = True):
        self.finish = finish
        self.place = place
        self.success = success

class ActEat:
    """
    Eat action
    """
    def __init__(self, start: float, duration: float, action_type: State = State.EAT):
        self.start = start
        self.duration = duration
        self.action_type = action_type

class ActEatRes:
    """
    Result of eating action
    """
    def __init__(self, finish: float, place: Place, success:bool = True):
        self.finish = finish
        self.place = place
        self.success = success

class ActCoffee:
    """
    CoffeE Action
    """
    def __init__(self, start: float, duration: float, action_type: State = State.COFFEE):
        self.start = start
        self.duration = duration
        self.action_type = action_type

class ActCoffeeRes:
    """
    Result of coffeE action
    """
    def __init__(self, finish: float, place: Place, success: bool = True):
        self.finish = finish
        self.place = place
        self.success = success

ACTION = ActCoffee | ActRest | ActEat | ActEdu | ActRoad
RESULT = ActCoffeeRes | AcrRestRes | ActEatRes | ActEduRes | ActRoadRes
