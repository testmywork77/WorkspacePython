# Global Variables Can Be Read from a Local Scope
def spam():
    print(eggs)
    
eggs = 42
spam()
print(eggs)