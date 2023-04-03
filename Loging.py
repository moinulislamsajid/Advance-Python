import logging
logging.debug('this is a debug message')
logging.info('this is info message')
logging.warning('this is warning message')
logging.error("this is a error message")
logging.critical("this is a critical message")  # this is message print only 3 item who is warning or erroe and critical

try:
    list = [1,2,3,4]
    lok = list[7]
except IndexError as e:
    logging.error(e)  # error out of range 


try:
    r = 19/0
    print(r)

except ZeroDivisionError as e:
    logging.error("Divison By Zero not possible")


