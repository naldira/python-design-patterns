"""
inform observers of events inside the server applications.
"""

from abc import (ABCMeta,
                 abstractmethod)
from services.products import Products
from services.observer import Observer


class Publisher(metaclass=ABCMeta):
    """
    Interface for Publisher class.
    """

    @classmethod
    @abstractmethod
    def add_observer(cls, observer: Observer) -> None:
        """
        adds an Observer to the observer list.

        Parameters
        ----------
        observer:
            Observer to be added to the observer list,
            raises NotImplementedError if not overwritten.
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def remove_observer(cls, observer: Observer) -> None:
        """
        removes an Observer from the observer list.

        Parameters
        ----------
        observer:
            Observer to be removed from the observer list,
            raises NotImplementedError if not overwritten.
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def notify_observer(cls) -> None:
        """
        notifies the Observer of the new events.
        raises NotImplementedError if not overwritten.
        """
        raise NotImplementedError


class DiscountPublisher(Publisher):
    """
    concrete implementation of Publisher interface, monitoring discounts.
    """
    _observer_list = []

    @classmethod
    def add_observer(cls, observer: Observer) -> None:
        """
        adds an Observer to the _observer_list.

        Parameters
        ----------
        observer: Observer:
            Observer to be added to the _observer_list.
        """
        cls._observer_list.append(observer)

    @classmethod
    def remove_observer(cls, observer: Observer) -> None:
        """
        removes an Observer from the _observer_list.

        Parameters
        ----------
        observer: Observer:
            Observer to be removed from the _observer_list.
        """
        cls._observer_list.remove(observer)

    @classmethod
    def notify_observer(cls):
        """
        notifies the Observers in the list, of the new events.
        """
        new_discounts = [item for item in Products.get_new_discounts()
                         if item not in Products.get_old_discounts()]
        for observer in cls._observer_list:
            observer.update(new_discounts)


class ArticlePublisher(Publisher):
    """
    concrete implementation of Publisher interface, monitoring articles.
    """
    NotImplemented


class SecurityPublisher(Publisher):
    """
    concrete implementation of Publisher interface, monitoring security.
    """
    NotImplemented
