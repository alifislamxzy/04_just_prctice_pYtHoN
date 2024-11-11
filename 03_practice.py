with open('this.txt', 'r') as f: 
    content = f.read()
with open('this_cpy.txt', 'w') as f:
    f.write(content)
    f.close()