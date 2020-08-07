from injector import Injector, inject, BoundKey, InstanceProvider, Module
import abc


class AbsClass(object, metaclass=abc.ABCMeta):
    def __init__(self):
        print("parent")


class AbsSubClass(AbsClass):
    def __init__(self):
        print("child")


class AbsSubClass2(AbsClass):
    def __init__(self):
        print("child2")


class MyClass(object):
    @inject
    def __init__(self, abs_class: AbsClass):
        self.abs_class = abs_class


class DIModule(Module):
    def configure(self, binder):
        binder.bind(AbsClass, to=AbsSubClass)


class DIModule2(Module):
    def configure(self, binder):
        binder.bind(AbsClass, to=AbsSubClass2)


injector = Injector([DIModule])
value = injector.get(MyClass)
print(value.abs_class)
