def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('apiwrapper/tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

test()
