import inspect
from copy import deepcopy
from typing import get_type_hints
import webview
import json


class __test__:
    def __nop__():
        pass


# Get the default method names to filter them out
defaultFunctionNames = set(
    [name for name, func in inspect.getmembers(__test__, predicate=inspect.isfunction)]
)


def jsApiClass[T](classToFix: T) -> T:
    # 1. Create a deep copy of the class
    coppiedClass = deepcopy(classToFix)

    # 2. Loop through functions using inspect.getmembers
    for name, func in inspect.getmembers(coppiedClass, predicate=inspect.isfunction):

        # Filter out default or magic methods
        if name in defaultFunctionNames or name.startswith("__"):
            continue  # Use 'continue' to skip, not 'return' which kills the whole function

        # 3. Get type hints using the actual function object
        hints = get_type_hints(func)
        if "return" in hints:
            del hints["return"]

        def typeToString(arg: any, arg_type):
            # Combined matching types together and added missing code blocks
            match arg_type:
                case _ if arg_type in (dict, list, set):
                    return json.dumps(arg)
                case _:
                    return str(arg)

        # 4. Correctly unpack the type hints dictionary (key, type)
        # We use an inner factory function to cleanly capture the current 'name' and 'hints'
        def make_js_wrapper(func_name, func_hints):
            def jsFunction(*args):
                # Convert each argument based on its expected type hint
                converted_args = [
                    typeToString(args[i], t)
                    for i, (k, t) in enumerate(func_hints.items())
                ]
                # Format the arguments as a comma-separated string for JavaScript
                js_args_str = ", ".join(converted_args)

                # FIX: Check if the state object and target function exist before running it!
                return (
                    f"if (window.pywebview && window.pywebview.state && typeof window.pywebview.state.{func_name} === 'function') {{ "
                    f"window.pywebview.state.{func_name}({js_args_str}); "
                    f"}}"
                )

            return jsFunction

        js_func_generator = make_js_wrapper(name, hints)

        # 5. Use setattr instead of square brackets to assign the new lambda
        setattr(
            coppiedClass,
            name,
            lambda *args: (
                webview.windows[0].evaluate_js(js_func_generator(*args))
                if len(webview.windows) > 0
                else None
            ),
        )

    return coppiedClass


import threading


def set_interval(interval):
    def decorator(function):
        def wrapper(*args, **kwargs):
            stopped = threading.Event()

            def loop():  # executed in another thread
                while not stopped.wait(interval):  # until stopped
                    function(*args, **kwargs)

            t = threading.Thread(target=loop)
            t.daemon = True  # stop if the program exits
            t.start()
            return stopped

        return wrapper

    return decorator
