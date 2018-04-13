def stars_decorator(f):
  def foo():
    print("*" * 50)
    f()
    print("*" * 50)

  return foo


def timestamp(f):
  def bar():
    print("timestamp activated")
    f()

  return bar


# greet = timestamp(greet)
@staticmethod
def greet():
  print("Howdy World!")




greet()