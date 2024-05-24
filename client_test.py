import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
    # Unit Test 1: Test if getDataPoint returns the correct tuple of stock name, bid_price, ask_price, and price
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        expected_output = ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2)
        self.assertEqual(getDataPoint(quotes[0]), expected_output)

    # Unit Test 2: Test if getDataPoint calculates price correctly when bid price is greater than ask price
    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        expected_output = ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2)
        self.assertEqual(getDataPoint(quotes[0]), expected_output)

    """ ------------ Add more unit tests ------------ """

if __name__ == '__main__':
    unittest.main()
