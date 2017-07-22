def addnums(x,y):
    return x + y
# change to push
print addnums(2,3)
print addnums(0x1f,3.3)
# "0x" is a hexadecimal number
# 9 09, 10 0a, 11 0b, ... 15 0f, 16 10, 31 1f ...
print addnums("a","b")

def addnums(x,y):
    if isinstance(x,(float,int)) and isinstance(y,(float,int)):
        return x + y
    print("I cannot add these types (" + str(type(x)) + ", " + str(type(y)) + ")")
    return

# We can return whatever we want from a function (dictionary, tuple, lists, strings, etc.).

print addnums(2,3.0)
print addnums("cat",23232)

# 5
# 34.3
# ab
# I cannot add these types (<type 'str'>, <type 'int'>)
# None