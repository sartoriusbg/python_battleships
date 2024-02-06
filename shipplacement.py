def print_t(text="pranked"):
    print(text)

def print_hello():
    print("hello")


def execute(func, par):
    func(*par)

execute(print_hello, [])
    
