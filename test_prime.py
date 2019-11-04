from unittest import TestCase

from prime_no import prime


class TestPrime(TestCase):
    def test_prime(self):
        self.assertTrue(prime(6))
