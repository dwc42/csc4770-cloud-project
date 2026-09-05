from backend.libraries.api import jsApiClass, set_interval
from time import time


# probaly be its own file
class _Api_:
    @staticmethod
    def setTicker(displayValue: str):  # Avoid using 'str' as a variable name
        pass


Api = jsApiClass(_Api_)


@set_interval(interval=1)
def updateTicker():
    Api.setTicker(f"{time()}")
