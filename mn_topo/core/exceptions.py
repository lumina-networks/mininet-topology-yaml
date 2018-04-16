class InvalidPropertyException(Exception):
    def __init__(self, message="Invalid properties set: {}", invalid_props=[]):
        # Call the base class constructor with the parameters it needs
        message = message.format(', '.join(invalid_props))
        super(InvalidPropertyException, self).__init__(message)


class InvalidIDException(Exception):
    def __init__(self, message="Invalid IDs in: {}", invalid_ids=[]):
        # Call the base class constructor with the parameters it needs
        message = message.format(', '.join(invalid_ids))
        super(InvalidIDException, self).__init__(message)


class MandatoryPropertyException(Exception):
    def __init__(self, message="Mandatory properties not set: {}", mandatory_props=[]):
        # Call the base class constructor with the parameters it needs
        message = message.format(', '.join(mandatory_props))
        super(MandatoryPropertyException, self).__init__(message)
