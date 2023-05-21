"""
Module for my states
"""

import random
from events import Event
from state import (ACTION, ActT,
AcrRestRes, ActCoffee, 
ActCoffeeRes, ActEat, ActEatRes, ActEdu,
ActEduRes, ActRest, ActRoad, ActRoadRes,
RESULT, Rest, Education, State, Place)

class MyState:
    """
    My States
    """
    def __init__(self, 
    event_queue: Event, cur_state: State,
    cur_pos: Place.HOME, cur_act: ACTION = None,
    cur_rest: bool = True, cur_eat: bool = True,
    prof: float = 1):
        self.event_queue = event_queue
        self.cur_state = cur_state
        self.cur_pos = cur_pos
        self.cur_act = cur_act
        self.cur_rest = cur_rest
        self.cur_eat = cur_eat
        self.prof = prof

    def next_state(self, time: float):
        """
        Determines the next state based on the current state and other conditions.
        """
        if self.cur_state == State.STUDY and 12<=time<=16:
            if not self.cur_rest:
                return State.REST
            elif not self.cur_eat:
                return State.EAT
            else:
                return State.ROAD
        elif self.cur_state == State.ROAD and (7<=time<=9 or 19<=time<=21):
            return random.choice([State.COFFEE, State.EAT])
        elif self.cur_state == State.REST and 12<=time<=18:
            return State.EAT
        else:
            return self.cur_state
        
    def process_action(self, action: ACTION, time: float):
        """
        Processes the given action and updates the person state accordingly.
        """
        if (self.cur_state == State.STUDY or self.cur_state == State.ROAD) and 9 <= time <= 19:
            if action == ActRest:
                self.cur_rest = True
            elif action == ActEat:
                self.cur_eat = True
            elif action == ActCoffee:
                self.cur_rest = True
            else:
                self.cur_rest = False
                self.cur_eat = False

        elif self.cur_state == State.ROAD and 18 <= time <= 22:
            if action == ActEdu:
                self.cur_rest = False
                self.cur_eat = False
            else:
                self.cur_rest = True
                self.cur_eat = True

        elif self.cur_state == State.REST and 10 <= time <= 15:
            if action == ActEdu:
                self.cur_rest = True
                self.cur_eat = False

        elif self.cur_state == State.EAT and 10 <= time <= 18:
            if action == ActEdu:
                self.cur_rest = False
                self.cur_eat = True

        elif self.cur_state == State.COFFEE and 12 <= time <= 18:
            if action == ActRest:
                self.cur_rest = True
                self.cur_eat = False
            elif action == ActEdu:
                self.cur_rest = False
                self.cur_eat = False
            else:
                self.cur_rest = False
                self.cur_eat = False

    def push_edu(self, ed: Education):
        """
        Add education to the queue with different priorities based on the type of education
        """
        if ed == Education.OP:
            priority = 1
        elif ed == Education.DISCKRET:
            priority = 2
        elif ed == Education.MATAN:
            priority = 3
        else:
            priority = 4

        work_action = ActEdu(work_type=ActT.SECONDARY, work=ed, priority=priority)
        self.event_queue.push_after_next_rest(work_action)

    def proced_edu(self, action: ACTION):
        """
        Process the given edu action and return the corresponding work result
        """
        if action == ActEdu:
            if self.cur_state == State.REST:
                if random.random() < 0.8:
                    if random.random() < 0.5:
                        return AcrRestRes
                    else:
                        return ActEduRes
                else:
                    return ActEduRes
            else:
                return AcrRestRes
        
        elif action == ActRest:
            if self.cur_state == State.STUDY:
                if self.cur_rest and self.cur_eat:
                    if random.random() < 0.7:
                        if random.random() < 0.6:
                            return ActEduRes
                        else:
                            return AcrRestRes
                    else:
                        return AcrRestRes
                else:
                    return ActEduRes
            else:
                return ActEduRes
        
        elif action == ActEat:
            if self.cur_state == State.EAT:
                if random.random() < 0.9:
                    if random.random() < 0.3:
                        return ActEatRes
                    else:
                        return ActCoffeeRes
                else:
                    return ActCoffeeRes
            else:
                return ActEduRes
        else:
            return AcrRestRes
        
    def push_commute(self, action: ActRoad):
        """
        Push commute action
        """
        self.event_queue.top_push(action)

    def process_commmute(self, action: ActRoad) -> ActRoadRes:
        """
        Process commute action
        """
        return ActRoadRes(duration=action.duration, finish = Place.SOMEWHERE)

    def push_rest(self, action: ActRest):
        """
        Push next rest action
        """
        self.event_queue.push_after_next_edu(action)

    def process_rest(self) -> AcrRestRes:
        """
        Process rested
        """
        return AcrRestRes(
            rested=random.uniform(0, 1) < 0.75, location=self.cur_pos
        )

    def push_eat(self, action: ActEat):
        """
        Push eat action
        """
        self.event_queue.push_after_next_road(
            action) and self.event_queue.push_after_next_edu(action)
        
    def push_coffee_after_edu(self, acttion: ActCoffee):
        """
        Push coffee after education
        """
        self.event_queue.push_after_next_edu(acttion)

    def process_education(self, action: ActEdu) -> ActEduRes:
        """
        Process education action
        """
        fail_probability = 1

        if not self.cur_rest:
            fail_probability *= 0.7

        if not self.cur_eat:
            fail_probability *= 0.8

        if self.cur_pos == Place.HOME:
            fail_probability *= 0.95
        elif self.cur_pos == Place.SOMEWHERE:
            fail_probability *= 0.4

        return ActEduRes(
            successful=random.uniform(0, 1) < fail_probability,
            location=self.cur_pos,
            proficiency=action.duration**0.0001 + 0.5,
        )
 
