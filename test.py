import unittest
import app

class MyTests(unittest.TestCase):
	def test(self):
		self.assertEqual(app.lambda_handler('',''), 'Hello from Lambda 12345666666')

if __name__ == '__main__':
	unittest.main()