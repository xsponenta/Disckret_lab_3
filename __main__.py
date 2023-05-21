"""
The main script
"""

from events import Event
from state import State, Place
from me import MyState

person = MyState(Event(), State.REST, Place.HOME)
for mounth in range(12):
    print(f'Started mounth {mounth + 1}')  
    for day in range(30):
        print(f"Started day {day + 1}")
        for hour in range(24):
            print(f"Mounth{mounth+1}, Day {day + 1}, Hour {hour}:")
            _ = person.next_state(hour)