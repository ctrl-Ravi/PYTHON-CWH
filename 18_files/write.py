# write to a file called john doe.txt
# it should contain data about john doe

f = open("john doe.txt","w")

string = '''
John doe is a nice guy, he lives in nyc and he works with python his favorite packag e is pandaaaa
'''

f.write(string)
f.close()