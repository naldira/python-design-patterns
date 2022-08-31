"""
receive updates from publishers and relay them to
subscribers.
"""

from abc import (ABCMeta,
                 abstractmethod)
from typing import Any, List

from services.subscriber import Subscriber
from services.email import EMail


class Observer(metaclass=ABCMeta):
    """
    interface for Observer classes.
    """
    @classmethod
    @abstractmethod
    def update(cls, info: Any) -> None:
        """
        updates state of observer.

        Parameters
        ----------
        info:
            the new given state, raises NotImplementedError if not overwritten.
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def add_subscriber(cls, subscriber: Subscriber) -> None:
        """
        adds a subscriber to the observer

        Parameters
        ----------
        subscriber:
            subscriber to be added to the observer,
            raises NotImplementedError if not overwritten.
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def remove_subscriber(cls, subscriber: Subscriber) -> None:
        """
        removes a subscriber from the observer

        Parameters
        ----------
        subscriber:
            subscriber to be removed from the observer,
            raises NotImplementedError if not overwritten.
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def notify_subscriber(cls) -> None:
        """
        notifies the subscriber of the new events.
        raises NotImplementedError if not overwritten.
        """
        raise NotImplementedError


class DiscountObserver(Observer):
    """
    concrete implementation of Observer interface, monitoring discounts.
    """
    _subscriber_list = []

    @classmethod
    def update(cls, new_discounts: List[str]) -> None:
        """
        updates state of observer.

        Parameters
        ----------
        new_discounts: List: str:
            a list strings matching newly discounted items.
        """
        for subscriber in cls._subscriber_list:
            for item in new_discounts:
                if item in subscriber.wishlist_new_discounted:
                    subscriber.remove_from_wishlist_new_discounted(item)
            for item in new_discounts:
                if item in subscriber.wishlist:
                    subscriber.add_to_wishlist_new_discounted(item)

    @classmethod
    def add_subscriber(cls, subscriber: Subscriber) -> None:
        """
        adds a subscriber to the observer.

        Parameters
        ----------
        subscriber: Subscriber:
            DiscountSubscriber to be added to the observer.
        """
        cls._subscriber_list.append(subscriber)

    @classmethod
    def remove_subscriber(cls, subscriber: Subscriber) -> None:
        """
        removes a subscriber from the observer.

        Parameters
        ----------
        subscriber: Subscriber:
            DiscountSubscriber to be removed from the observer.
        """
        cls._subscriber_list.remove(subscriber)

    @classmethod
    def notify_subscriber(cls) -> None:
        """
        notifies the subscribers in the list, of the new events.
        """
        for subscriber in cls._subscriber_list:
            message = f"dear {subscriber.name},\n" \
                      f"the following items from your wishlist " \
                      f"have recently gone on sale:\n" \
                      f"{' and '.join(subscriber.wishlist_new_discounted)}"
            EMail.send_email(subscriber.email, message)


class ArticleObserver(Observer):
    """
    concrete implementation of Observer interface, monitoring articles.
    """
    pass


class SecurityObserver(Observer):
    """
    concrete implementation of Observer interface, monitoring security.
    """
    pass
