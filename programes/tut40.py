# 1st way of string formatting

me = "Kartikey"
a = "this is %s" % me
print(a)

# 2nd way of string formatting
a1 = 3
b = "This is %s %s " % (me, a1)
print(b)

# 3rd way of string formatting
c = "This is {} {}"
d = c.format(me, a1)
print(d)
c = "This is {1} {0}"
d = c.format(me, a1)
print(d)


#F-strings

let = f"This is {me} {a1} {3*5}"
print(let)
