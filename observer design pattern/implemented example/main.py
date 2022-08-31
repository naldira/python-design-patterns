from services.observer import DiscountObserver
from services.publisher import DiscountPublisher
from services.subscriber import DiscountSubscriber
from services.products import Products

if __name__ == '__main__':
    ali = DiscountSubscriber('ali', 'ali@foo.bar')
    ali.add_to_wishlist('ps5')
    DiscountPublisher.add_observer(DiscountObserver)
    DiscountObserver.add_subscriber(ali)
    Products.add_new_discount('ps5')
    DiscountPublisher.notify_observer()
    DiscountObserver.notify_subscriber()
    ali.add_to_wishlist('ps4')
    Products.add_new_discount('ps4')
    DiscountPublisher.notify_observer()
    DiscountObserver.notify_subscriber()
