from django.test import TestCase

from restaurant.models import Menu, Booking

class MenuTest(TestCase):
    def test_get_item(self):
        # create a new menu object
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)

        self.assertEqual(item, "IceCream : 80")

        # check that the name, price, and description fields are set correctly
        self.assertEqual(item.title, 'IceCream')
        self.assertEqual(item.price, 80)
        self.assertEqual(item.inventory, 100)