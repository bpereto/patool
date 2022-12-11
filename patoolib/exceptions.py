class PatoolError(Exception):
    """Raised when errors occur."""


class PatoolUnknownArchiveError(PatoolError):
    """Raised when encountering an unknown archive type."""


class PatoolUnsupported(PatoolError):
    """Raised when encountering an unsupported action."""


class PatoolExeNotFound(PatoolError):
    """Raised when the executable for extractions is missing."""


class PatoolCmdError(PatoolError):
    """Raised when running a command return errors."""


class PatoolOperationError(PatoolError):
    """Raised when running an operation return errors."""


class PatoolPasswordError(PatoolError):
    """Raised when there is an error regarding passwords."""
