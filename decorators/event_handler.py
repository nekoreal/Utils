from typing import Callable
import inspect

class Handler:
    def __init__(self,
                 func:Callable,
                 priority:int=0
                 ):
        self.priority:int = priority
        self.func:Callable = func

class Event:
    def __init__(self,
                 event_name:str
                 ):
        self.event_name:str = event_name
        self.handlers: list[Handler] = []

    def add_handler(self,
                    handler:Handler
                    )->bool:
        try:
            self.handlers.append(handler)
            return True
        except:
            return False

    def remove_handler(self,
                       handler:Handler
                       )-> bool:
        try:
            self.handlers.remove(handler)
            return True
        except:
            return False

    def remove_handler_by_func(self,
                      func:Callable
                      )-> bool:
        for handler in self.handlers:
            if handler.func == func:
                self.handlers.remove(handler)
                return True
        return False

    def clear_handlers(self):
        self.handlers: list[Handler] = []

    def handle(self, *args, **kwargs):
        for handler in sorted(self.handlers, key=lambda h: h.priority, reverse=True):
            func = handler.func
            sig = inspect.signature(func)
            try:
                bound = sig.bind_partial(*args, **kwargs)
                bound.apply_defaults()
                func(*bound.args, **bound.kwargs)
            except TypeError as e:
                print(f"Handler {func.__name__} argument mismatch: {e}")


class EventHandler:

    def __init__(self,):
        self.events: list[Event] = []

    def add_event(self,
                  event_name:str
                  ):
        for event in self.events:
            if event.event_name == event_name:
                raise RuntimeError(f"Event {event.event_name} already registered")
        self.events.append(Event(event_name))

    def add_event_handler(self,
                  event_name:str,
                  priority:int=0
                  )->Callable:
        def wrapper(func:Callable):
            current_event = self.find_event(event_name)
            if current_event: current_event.add_handler(Handler(func,priority))
            else: raise RuntimeError(f'Event {event_name} not found')
            return func
        return wrapper

    def find_event(self,
                  event_name:str
                  )-> Event|None:
        for event in self.events:
            if event.event_name == event_name:
                return event
        return None

    def trigger_event(self,
                      event_name:str,
                      *args,
                      **kwargs
                      ):
        current_event = self.find_event(event_name)
        if current_event:
            current_event.handle(*args, **kwargs)
        else:
            raise RuntimeError(f'Event {event_name} not found')

    def create_trigger_event_decorator(self,
                                priority:int=0
                                ):
        def wrapper(func:Callable):
            event_name=f"on_{func.__name__}"
            if not self.find_event(event_name):
                self.add_event(event_name=event_name)
            def inner(*args, **kwargs):
                self.trigger_event(event_name, *args, **kwargs)
                return func(*args, **kwargs)
            return inner
        return wrapper

    def remove_event_handler(self,
                             event_name:str,
                             func:Callable
                             )-> bool:
        current_event = self.find_event(event_name)
        if current_event:
            try:
                return current_event.remove_handler_by_func(func)
            except:
                return False
        else:
            raise RuntimeError(f'Event {event_name} not found')


