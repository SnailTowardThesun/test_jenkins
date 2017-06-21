import unittest, test_demo

if __name__ == "__main__":
    suite = unittest.TestSuite()
    # demo, samples.
    suite.addTest(unittest.makeSuite(test_demo.TestDemo))

    # start suite.
    unittest.TextTestRunner().run(suite)