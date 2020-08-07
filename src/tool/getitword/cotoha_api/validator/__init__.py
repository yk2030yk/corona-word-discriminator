class CheckError(Exception):
    pass


class ValidationError(Exception):
    pass


class Checker(object):
    @staticmethod
    def str_maxlen(value, max_length):
        if len(value) > max_length:
            raise CheckError(
                f"This string length must be less than or equal to {max_length}."
            )

    @staticmethod
    def str_minlen(value, min_length):
        if len(value) < min_length:
            raise CheckError(f"This string length must be not less than {min_length}.")

    @staticmethod
    def num_maxlen(value, max_length):
        if value > max_length:
            raise CheckError(f"This number must be less than or equal to {max_length}.")

    @staticmethod
    def num_minlen(value, min_length):
        if value < min_length:
            raise CheckError(f"This number must be not less than {min_length}.")

    @staticmethod
    def required(value):
        if value is None:
            raise CheckError("This value is reqired.")

    @staticmethod
    def is_allowed(value, allowed_values):
        if value not in allowed_values:
            allowed = allowed_values.join(",")
            raise CheckError(f"This value must be any one of these ({allowed})")

    @staticmethod
    def is_list(value):
        if isinstance(value, list):
            raise CheckError(f"This value must be list")

    @staticmethod
    def is_allowed_list(list_value, allowed_values):
        not_allowed_values = [
            value for value in list_value if value not in allowed_values
        ]

        if len(not_allowed_values) > 0:
            raise CheckError(f"This value must be any one of these ({allowed})")


class Validator(object):
    def __init__(self):
        self.errors = []

    def check(self, method, value, *arg, **kwargs):
        try:
            method(value, *arg, **kwargs)
        except CheckError as e:
            self.errors.append(ValidationError(e))

    def validate_str_maxlen(self, value, max_length):
        self.check(Checker.str_maxlen, value, max_length)

    def validate_str_minlen(self, value, min_length):
        self.check(Checker.str_minlen, value, min_length)

    def validate_num_maxlen(self, value, max_length):
        self.check(Checker.num_maxlen, value, max_length)

    def validate_num_minlen(self, value, min_length):
        self.check(Checker.num_minlen, value, min_length)

    def validate_allowed(self, value, allowed_values):
        self.check(Checker.is_allowed, value, allowed_values)

    def validate_list(self, value):
        self.check(Checker.is_list, value)

    def validate_allowed_list(self, value, allowed_values):
        self.check(Checker.is_allowed_list, value, allowed_values)

    def validate_required(self, value):
        self.check(Checker.required, value)
