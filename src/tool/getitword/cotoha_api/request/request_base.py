from abc import ABCMeta, abstractmethod


class RequestBase(object, metaclass=ABCMeta):
    @abstractmethod
    def validate(self):
        raise NotImplementedError("must be overrided.")

    @abstractmethod
    def to_dict(self):
        raise NotImplementedError("must be overrided.")
