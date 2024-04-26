
def hello():
    print("hello")


hello()

def hi(name, age):
    return f"hi {name} you are {str(age)} years old"

print(hi("mope",30))

def helloSeq(first,second):
    print(f"Hello {first} {second}")

helloSeq(second="baby", first="mope")

def calc(first,second):
    return first + second

print(calc(2,3))