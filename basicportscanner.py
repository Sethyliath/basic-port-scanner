#import necessities
from socket import *
import time
#set start time
startTime = time.time()

if __name__ == '__main__':
    #create an input prompt
    target = input('Enter the host to be scanned: ')
    t_IP = gethostbyname(target)
    #print the response
    print('Starting scan on host: ', t_IP)
#set the port range
    for i in range(1, 1000):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if (conn == 0):
            #print which ports are open
            print('Port %d: OPEN' % (i,))
        s.close()
        #print the time taken to complete the scan
print('Time taken:', time.time() - startTime)