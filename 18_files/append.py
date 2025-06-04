# Append to and existing file called john doe.txt 
# write to a file called john doe.txt
# it should contain data about john doe

f = open("john doe.txt","a")

string = '''
John doe intially live in america , hes s
'''

f.write(string)
f.close()