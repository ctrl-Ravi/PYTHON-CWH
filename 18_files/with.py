# f=open("ravi.txt","r")
# content = f.read()
# print(content)
# f.close()

with open("ravi.txt","r") as f: # context manager
    content= f.read()
    print(content)
    # No need to write f.close(because file is already closed by defult when using with syntax)