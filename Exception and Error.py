# Error and Exception
from logging import exception


try:
   a = 5/1
   b = a + '10'
except ZeroDivisionError as e:
    print("Division by 0 not possible")
except TypeError as e:
    print(e)
finally:
    print("this is not possible")