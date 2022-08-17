import datetime
import time
from typing import Callable

from pythontextnow import Client
from pythontextnow.util.ConfigReader import ConfigReader


def enforce_cooldown(function: Callable) -> Callable:
    """
    This will enforce a scaling cooldown on the method it wraps.
    """

    def wrapFunction(*args, **kwargs):
        cooldown_seconds = ConfigReader.get("api", "api_call_cooldown_seconds", as_type=float)
        client_config = Client.get_client_config()
        now = datetime.datetime.now()
        difference_seconds = (now - client_config.last_call_time).total_seconds()
        if difference_seconds > cooldown_seconds:
            # enforce cooldown
            time.sleep(difference_seconds)
            Client.update(last_call_time=now)
        return function(*args, **kwargs)

    return wrapFunction
