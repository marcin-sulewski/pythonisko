class CustomObject:
    pass

obj = CustomObject()

obj.a = 1
obj.b = 2
obj.c = 3

obj_dict = vars(obj)

print( obj_dict)
