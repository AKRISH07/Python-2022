import logging;
logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.DEBUG,filename='sqrt.log') - All the o/p will be displayed in this file
#DEBUG, INFO, WARN, ERROR (Last Priority - Only error will be displayed)
#If WARN is given WARN, ERROR will be displayed

num1 = 10;
num2 = 20;
res=num1/num2;
if(res<0):
    print("Result less than 0")
    logging.warn("Less than 0 ***")
else:
    print(res)
    logging.info("Result is displayed**")