"""
emulates data from database, only to example's demonstration.
"""
from typing import List


class Products:
    """
    stand-in for data retrieved from database.
    """
    _products = ['ps1', 'ps2', 'ps3', 'ps4', 'ps5']
    _old_discounts = []
    _new_discounts = []

    @classmethod
    def add_old_discount(cls, product: str) -> None:
        """
        adds a product to list of old discounts. raises Value error
        if no such product is found.

        Parameters
        ----------
        product:
            product to be added to old discounts list.
        """
        if product in cls._products:
            cls._old_discounts.append(product)
        else:
            raise ValueError(f'No product named {product}')

    @classmethod
    def remove_old_discount(cls, product: str) -> None:
        """
        removes a product from list of old discounts. raises Value error
        if no such product is found.

        Parameters
        ----------
        product:
            product to be removed from old discounts list.
        """
        if product in cls._products:
            cls._old_discounts.remove(product)
        else:
            raise ValueError(f'No product named {product}')

    @classmethod
    def add_new_discount(cls, product: str) -> None:
        """
        adds a product to list of new discounts. raises Value error
        if no such product is found.

        Parameters
        ----------
        product:
            product to be added to new discounts list.
        """
        if product in cls._products:
            cls._new_discounts.append(product)
        else:
            raise ValueError(f'No product named {product}')

    @classmethod
    def remove_new_discount(cls, product: str) -> None:
        """
        removes a product from list of new discounts. raises Value error
        if no such product is found.

        Parameters
        ----------
        product:
            product to be removed from old discounts list.
        """
        if product in cls._products:
            cls._new_discounts.remove(product)
        raise ValueError(f'No product named {product}')

    @classmethod
    def get_products(cls) -> List[str]:
        """
        returns private attribute, products list.
        """
        return cls._products

    @classmethod
    def get_new_discounts(cls) -> List[str]:
        """
        returns private attribute, new discounts list.
        """
        return cls._new_discounts

    @classmethod
    def get_old_discounts(cls) -> List[str]:
        """
        returns private attribute, old discounts list.
        """
        return cls._old_discounts
