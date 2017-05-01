import unittest
import app

class MyTests(unittest.TestCase):
	def test(self):
		self.assertEqual(app.lambda_handler('',''), 'Hello from Lambda 3')

if __name__ == '__main__':
	unittest.main()