import sys
import os
import unittest
from io import StringIO
sys.path.append(os.path.abspath('../modules'))
import getemails
import pagereader

soup = pagereader.readPage('http://www.whatsmyip.net/')

class getMailsTestCase(unittest.TestCase):
	
	def setUp(self):
		self.held, sys.stdout = sys.stdout, StringIO()
	
	def test_return_emails_list(self):
		data = "\nMails Found - 1\n-------------------------------\nadvertise@provaz.eu\n"
		getemails.getMails(soup)
		self.assertEqual(sys.stdout.getvalue(),data)

	def tearDown(self):
                sys.stdout.flush()

if __name__ == '__main__':
	unittest.main()
