# Observer implemented example

---
## modules in services package:
1. email.py: a (fake) email sending service, simply prints onto terminal.
2. products: plays the role of products in database.
3. publisher: publisher classes will notify observers that are in their update
list, of changes in states they're monitoring
4. observer: observer classes receive the state change from publishers, and will
notify subscribers that are in their list of this change.
5. subscriber: subscriber classes will receive the updates they've registered
to receive.


<mark>important note </mark>: each publisher (one) to observers (many) has a one-way,
one-to-many relationship with observers in its list.

<mark>important note </mark>: each observer (one) to subscribers (many) has a one-way,
one-to-many relationship with subscribers in its list.



---
**main.py** uses the modules in services package to create a subscriber.
add to the subscribers wishlist. after that it puts that same item in products
discount list, if the application is working correctly in next steps the
publisher should notify the observer, and observer should notify the user via
a (fake) E-mail. a second product is added to the wishlist next and also added
to the product discounts to make sure the first item doesn't get printed twice.