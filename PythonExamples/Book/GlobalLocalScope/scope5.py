# The global Statement
def spam():
  global eggs
  eggs = 'spam'

eggs = 'global'
print(eggs)
spam()
print(eggs)