import unittest
from employee import Employee

class TestCalc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('class set up\n')

    @classmethod
    def tearDownClass(cls):
        print('class tear down')

    def setUp(self):
        print('test set up')
        self.employee_1 = Employee('Thara','Supasiti',100000)
        self.employee_2 = Employee('Joe','Doe',50000)

    def tearDown(self):
        print('test tear down\n')

    def test_email(self):
        print('test email')
        self.assertEqual(self.employee_1.email, 'Thara.Supasiti@email.com')
        self.assertEqual(self.employee_2.email, 'Joe.Doe@email.com')
    
    def test_fullname(self):
        print('test fullname')
        self.assertEqual(self.employee_1.fullname, 'Thara Supasiti')
        self.assertEqual(self.employee_2.fullname, 'Joe Doe')

    def test_apply_raise(self):
        print('test apply raise')
        self.employee_1.apply_raise()
        self.employee_2.apply_raise()

        self.assertEqual(self.employee_1.pay, 105000)
        self.assertEqual(self.employee_2.pay, 52500)

if __name__ == "__main__":
    unittest.main()