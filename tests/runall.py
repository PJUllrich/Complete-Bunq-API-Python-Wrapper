def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests', top_level_dir='tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

test()
