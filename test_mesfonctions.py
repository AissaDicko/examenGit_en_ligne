import unittest

from mesfonctions import ajouter, diviser, est_pair, palindrome_texte, moyenne


class TestMesFonctions(unittest.TestCase):
    def test_ajouter(self):
        self.assertEqual(ajouter(2, 3), 5)
        self.assertEqual(ajouter(-1, 1), 0)
        self.assertEqual(ajouter(0, 0), 0)

    def test_diviser(self):
        self.assertEqual(diviser(10, 2), 5)
        self.assertEqual(diviser(5, 2), 2.5)
        self.assertIsNone(diviser(5, 0))

    def test_est_pair(self):
        self.assertTrue(est_pair(4))
        self.assertFalse(est_pair(5))
        self.assertTrue(est_pair(0))

    def test_palindrome_texte(self):
        self.assertTrue(palindrome_texte('Radar'))
        self.assertTrue(palindrome_texte('A man a plan a canal Panama'))
        self.assertFalse(palindrome_texte('Bonjour'))

    def test_moyenne(self):
        self.assertEqual(moyenne([1, 2, 3, 4]), 2.5)
        self.assertEqual(moyenne([5]), 5)
        self.assertIsNone(moyenne([]))


if __name__ == '__main__':
    unittest.main()
