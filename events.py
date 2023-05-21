"""
Events for a person
"""

from state import (ACTION, ActCoffee, ActRest, ActEat, ActEdu, ActRoad)
class Event:
    """
    Class for Event to make a Queue
    """
    def __init__(self):
        """
        Initialization
        """
        self.queue_event: list[ACTION] = []

    def __len__(self):
        """
        Return len of queue
        """
        return len(self.queue_event)
    
    def top_peek(self):
        """
        Return first element of quque
        """
        return self.queue_event[0] if self.queue_event else None

    def back_peek(self):
        """
        Return last element of queue
        """
        return self.queue_event[-1] if self.queue_event else None
    
    def top_pop(self):
        """
        Pop first element of queue
        """
        return self.queue_event.pop(0) if self.queue_event else None
    
    def back_pop(self):
        """
        Pop last element of queue
        """
        return self.queue_event.pop(-1) if self.queue_event else None
    
    def top_push(self, act: ACTION):
        """
        Add action to the first place
        """
        return [act] + self.queue_event
    
    def back_push(self, act: ACTION):
        """
        Add action to the last place
        """
        return self.queue_event.append(act)
    
    def remove(self, action):
        """
        Remove action from queue
        """
        if action in self.queue_event:
            self.queue_event.remove(action)

    def push_after_next_coffe(self, act:ACTION):
        """
        Add new action after coffe action
        """
        for idx, action in enumerate(self.queue_event):
            if isinstance(action, ActCoffee):
                self.queue_event.insert(idx + 1, act)
                break
        else:
            self.queue_event.append(act)

    def push_after_next_rest(self, act:ACTION):
        """
        Add new action after rest action
        """
        for idx, action in enumerate(self.queue_event):
            if isinstance(action, ActRest):
                self.queue_event.insert(idx + 1, act)
                break
        else:
            self.queue_event.append(act)

    def push_after_next_eat(self, act:ACTION):
        """
        Add new action after eat action
        """
        for idx, action in enumerate(self.queue_event):
            if isinstance(action, ActEat):
                self.queue_event.insert(idx + 1, act)
                break
        else:
            self.queue_event.append(act)

    def push_after_next_edu(self, act:ACTION):
        """
        Add new action after edu action
        """
        for idx, action in enumerate(self.queue_event):
            if isinstance(action, ActEdu):
                self.queue_event.insert(idx + 1, act)
                break
        else:
            self.queue_event.append(act)

    def push_after_next_road(self, act:ACTION):
        """
        Add new action after road action
        """
        for idx, action in enumerate(self.queue_event):
            if isinstance(action, ActRoad):
                self.queue_event.insert(idx + 1, act)
                break
        else:
            self.queue_event.append(act)

    def peek_after_next_rest(self):
        """
        Peek next element after rest
        """
        for idx, action in enumerate(self.queue_event):
            if isinstance(action, ActRest):
                return self.queue_event[idx+1]
        else:
            return None
        
    def peek_after_next_road(self):
        """
        Peek next element after road
        """
        for idx, action in enumerate(self.queue_event):
            if isinstance(action, ActRoad):
                return self.queue_event[idx+1]
        else:
            return None
    
    def peek_after_next_eat(self):
        """
        Peek next element after eat
        """
        for idx, action in enumerate(self.queue_event):
            if isinstance(action, ActEat):
                return self.queue_event[idx+1]
        else:
            return None
        
    def peek_after_next_edu(self):
        """
        Peek next element after edu
        """
        for idx, action in enumerate(self.queue_event):
            if isinstance(action, ActEdu):
                return self.queue_event[idx+1]
        else:
            return None
        
    def peek_after_next_coffee(self):
        """
        Peek next element after road
        """
        for idx, action in enumerate(self.queue_event):
            if isinstance(action, ActCoffee):
                return self.queue_event[idx+1]
        else:
            return None

    def contains(self, action: type):
        """
        Checks containing of action
        """
        return any(isinstance(act, action) for act in self.queue_event)
    
    def filter_nonpermanent(self):
        """
        Remove all permanent actions
        """
        self.queue_event = list(filter(lambda x: isinstance(x, ActEat) 
        or isinstance(x, ActRoad)), self.queue_event)
