from django.test.simple import run_tests as default_run_tests 
from django.conf import settings 


def run_tests(test_labels, *args, **kwargs): 
	if not test_labels:
		test_labels = settings.OUR_APPS
	
	return default_run_tests(test_labels, *args, **kwargs) 

