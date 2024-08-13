import webbrowser

def abrir():
    webbrowser.open("https://www.youtube.com/watch?v=mCdA4bJAGGk")


def suma(a,b):
    abrir()
    return a + b


print("hola mundo")

V1 = int(input("Valor 1: "))
V2 = int(input("Valor 2: "))

print("Suma: " + str(suma(V1,V2)))

