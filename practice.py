content = [ "a","b","c"]

filename = ["aaa.txt","bcc.txt","cdd.txt"]

for contents , filenaems in zip(content,filename):

    file = open(f"file/{filename}", 'w')

    file.write(contents)
    file.close()

