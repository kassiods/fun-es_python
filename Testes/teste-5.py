#modificador global 
x=1

def modificador_global():
    global x
    x=20

modificador_global()
print(x)