import create_serializer as serlib
ser = serlib.create_serializer("yaml")
def g(a, b):
   return a+b
d = ser.dumps(g)
print(d)

