import warnings
from functools import wraps

from fairlearn.exceptions import ImplicitUsageOfAsFrameWarning


def use_as_frame_explicitly(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "as_frame" not in kwargs:
            msg = (
                "You have not specified the value for as_frame, which currently "
                "defaults to True. Starting with version 0.10.0, the default is "
                "changing to False. Specify the value of as_frame to suppress "
                "the warning."
            )
            warnings.warn(ImplicitUsageOfAsFrameWarning(msg))
        return func(*args, **kwargs)

    return wrapper
