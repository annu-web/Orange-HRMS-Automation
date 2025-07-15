from login import Login
from admin import Admin
from Title import Title_pge
from dotenv import load_dotenv
import unittest


def suite():
    suite.addTest(Login())
    suite.addTest(Admin())
    suite.addTest(Title_pge())

    return suite

if __name__ == '__main__':
    load_dotenv()
    runner = unittest.TextTestRunner(verbosity=2)
    suite = suite()
    runner.run(suite)
    