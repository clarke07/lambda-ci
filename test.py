import unittest
import app

class MyTests(unittest.TestCase):
	def test(self):
		self.assertEqual(app.lambda_handler('',''), 'Hello from Lambda large')

if __name__ == '__main__':
	unittest.main()