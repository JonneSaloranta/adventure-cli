import unittest

from src.util.vector2D import Vector2D

class TestVector2D(unittest.TestCase):
    
    def setUp(self):
        self.v1 = Vector2D(1, 2)
        self.v2 = Vector2D(3, 4)

    def tearDown(self):
        # print("tearDown")
        pass


    def test_add(self):
        self.assertEqual(self.v1 + self.v2, Vector2D(4, 6))
        self.assertEqual(self.v1, Vector2D(1, 2))

    def test_sub(self):
        self.assertEqual(self.v1 - self.v2, Vector2D(-2, -2))
        self.assertEqual(self.v1, Vector2D(1, 2))

    def test_mul(self):
        self.assertEqual(self.v1 * 3, Vector2D(3, 6))
        self.assertEqual(self.v1, Vector2D(1, 2))

    def test_normalize(self):
        self.assertEqual(self.v1, Vector2D(1, 2))
        self.assertEqual(self.v1.normalize(), Vector2D(0.4472135954999579, 0.8944271909999159))

    def test_distance(self):
        self.assertEqual(self.v1.distance(self.v2), 2.8284271247461903)
        self.assertEqual(self.v1, Vector2D(1, 2))

    def test_dot(self):
        self.assertEqual(self.v1.dot(self.v2), 11)
        self.assertEqual(self.v1, Vector2D(1, 2))

    def test_angle(self):
        self.assertEqual(self.v1.angle(self.v2), 0.17985349979247847)
        self.assertEqual(self.v1, Vector2D(1, 2))

    def test_str(self):
        self.assertEqual(str(self.v1), "(1, 2)")
        self.assertEqual(self.v1, Vector2D(1, 2))

    def test_repr(self):
        self.assertEqual(repr(self.v1), "Vector2D(1, 2)")
        self.assertEqual(self.v1, Vector2D(1, 2))

    def test_iter(self):
        self.assertEqual(list(self.v1), [1, 2])
        self.assertEqual(self.v1, Vector2D(1, 2))

    def test_getitem(self):
        self.assertEqual(self.v1[0], 1)
        self.assertEqual(self.v1[1], 2)
        self.assertEqual(self.v1, Vector2D(1, 2))
        self.assertRaises(IndexError, lambda: self.v1[2])
        self.assertRaises(IndexError, lambda: self.v1[-1])

    def test_len(self):
        self.assertEqual(len(self.v1), 2)
        self.assertEqual(self.v1, Vector2D(1, 2))

    def test_eq(self):
        self.assertEqual(self.v1, Vector2D(1, 2))
        self.assertEqual(self.v1, Vector2D(1, 2))

    def test_ne(self):
        self.assertEqual(self.v1, Vector2D(1, 2))

    def test_magnitude(self):
        self.assertEqual(self.v1, Vector2D(1, 2))
        self.assertEqual(self.v1.magnitude(), 2.23606797749979)

    def test_truediv(self):
        self.assertEqual(self.v1 / 2, Vector2D(0.5, 1))
        self.assertEqual(self.v1, Vector2D(1, 2))



if __name__ == "__main__":
    unittest.main(verbosity=2)