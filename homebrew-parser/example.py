#!/usr/bin/python

from extractomatic import extractomatic

result_data = extractomatic('http://www.reddit.com/r/Homebrewing/comments/gihwe/my_dad_has_a_small_beer_brewery_and_were_aiming/')

print result_data
print '\n >>> That url has ' + str(len(result_data)) + ' comments'
