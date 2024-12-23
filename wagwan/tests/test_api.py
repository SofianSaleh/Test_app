import frappe
import unittest
import requests_mock


class TestApi(unittest.TestCase):

    def setUp(self):
        # This method will run before each test.
        # Set up necessary preconditions here.
        pass

    def tearDown(self):
        # This method will run after each test.
        # Clean up resources or reset states here.
        pass

    @requests_mock.Mocker()
    def test_get_products(self, mock):
        # Mock the WooCommerce API response
        mock.get(
            "https://your-woocommerce-site.com/wp-json/wc/v3/products",
            json=[
                {"id": 1, "name": "Product 1", "price": "10.00"},
                {"id": 2, "name": "Product 2", "price": "20.00"},
            ],
        )

        # Call the method you want to test
        response = [
            {"id": 1, "name": "Product 1", "price": "10.00"},
            {"id": 2, "name": "Product 2", "price": "20.00"},
        ]

        # Assert that the response is as expected
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0]["name"], "Product 1")
