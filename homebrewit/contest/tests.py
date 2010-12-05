from django.test import TestCase

class HomebrewitContestViewsTest(TestCase):
	def test_register(self):
		response = self.client.get('/contest/register')
		self.assert_(response.context['form'])

#	def test_register__post(self):
#		response = self.client.post('/contest/register', {'
