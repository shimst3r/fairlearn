# Copyright (c) Microsoft Corporation and Fairlearn contributors.
# Licensed under the MIT License.


class DataFairnessWarning(UserWarning):
    """Custom warning meant to be raised when loading datasets with fairness issues."""

    pass


class ImplicitUsageOfAsFrameWarning(FutureWarning):
    """
    Custom warning meant to be raised when loading datasets without explicitly
    passing `as_frame`.
    """
