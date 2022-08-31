"""
receive information from observers instead of
querying the server applications directly.
"""

from abc import (ABCMeta,
                 abstractmethod)
from typing import List

from services.products import Products


class Subscriber(metaclass=ABCMeta):
    """
    Interface for Subscriber classes.
    """

    @property
    @abstractmethod
    def name(self) -> None:
        """
        subscriber's name.
        raises NotImplementedError if not overwritten.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def email(self) -> None:
        """
        subscriber's name.
        raises NotImplementedError if not overwritten.
        """
        raise NotImplementedError


class DiscountSubscriber(Subscriber):
    """
    concrete implementation of Subscriber interface, monitoring discounts.
    """
    def __init__(self, name: str, email: str, wishlist: List = []) -> None:
        self.name = name
        self.email = email
        self.wishlist = wishlist
        self.wishlist_new_discounted = []
        self.wishlist_all_discounted = []

    @property
    def name(self) -> str:
        """
        getter for name attribute.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        sets a new value for name.
        raises value error if not a string.

        Parameters
        ----------
        new_name: str:
            new value for name.
        """
        if not isinstance(new_name, str):
            raise ValueError('names can only be strings.')
        self._name = new_name

    @property
    def email(self) -> str:
        """
        getter for email attribute.
        """
        return self._email

    @email.setter
    def email(self, new_email: str) -> None:
        """
        sets a new value for email.
        raises value error if not a string.

        Parameters
        ----------
        new_email: str:
            new value for email.
        """
        if not isinstance(new_email, str):
            raise ValueError('email has to be a string.')
        self._email = new_email

    def add_to_wishlist(self, product: str) -> None:
        """
        adds a product to wishlist.

        Parameters
        ----------
        product: str:
            product to be added to wishlist.
        """
        if product in Products.get_products():
            self.wishlist.append(product)
        else:
            print(f'{product} is not in products, no action')

    def remove_from_wishlist(self, product: str) -> None:
        """
        removes a product from wishlist.

        Parameters
        ----------
        product: str:
            product to be removed from wishlist.
        """
        if product in self.wishlist:
            self.wishlist.remove(product)
        else:
            print(f'{product} did not exist in wishlist, not removed.')

    def add_to_wishlist_new_discounted(self, product: str) -> None:
        """
        adds a product to newly discounted items in wishlist.

        Parameters
        ----------
        product: str:
            product to be added to newly discounted items in wishlist.
        """
        if product in Products.get_products():
            self.wishlist_new_discounted.append(product)
        else:
            print(f'{product} is not in products, no action')

    def remove_from_wishlist_new_discounted(self, product: str) -> None:
        """
        removes a product from newly discounted items in wishlist.

        Parameters
        ----------
        product: str:
            product to be removed from newly discounted items in wishlist.
        """
        if product in self.wishlist:
            self.wishlist_new_discounted.remove(product)
        else:
            print(f'{product} did not exist in wishlist, not removed.')

    def add_to_wishlist_all_discounted(self, product: str) -> None:
        """
        adds a product to all discounted items in wishlist.

        Parameters
        ----------
        product: str:
            product to be added to all discounted items in wishlist.
        """
        if product in Products.get_products():
            self.wishlist_all_discounted.append(product)
        else:
            print(f'{product} is not in products, no action')

    def remove_from_wishlist_all_discounted(self, product: str) -> None:
        """
        removes a product from all discounted items in wishlist.

        Parameters
        ----------
        product: str:
            product to be removed from all discounted items in wishlist.
        """
        if product in self.wishlist:
            self.wishlist_all_discounted.remove(product)
        else:
            print(f'{product} did not exist in wishlist, not removed.')

    def clean_up_wishlist(self) -> None:
        """
        removes items that aren't discounted in products from
        all discounted wishlist items list.
        """
        for item in self.wishlist_all_discounted:
            if item not in [Products.get_old_discounts() +
                            Products.get_new_discounts()]:
                self.wishlist_all_discounted.remove(item)


class ArticleSubscriber(Subscriber):
    """
    concrete implementation of Subscriber interface, monitoring articles.
    """
    pass


class SecuritySubscriber(Subscriber):
    """
    concrete implementation of Subscriber interface, monitoring security.
    """
    pass
