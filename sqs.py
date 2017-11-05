from liblo import *

#import liblo
import sys
import time


class MuseServer(ServerThread):
    #listen for messages on port 5000
    def __init__(self):
        ServerThread.__init__(self, 5000)

    #receive accelrometer data
    @make_method(None, 'fff')
    def acc_callback(self, path, args):
        acc_x, acc_y, acc_z = args
        print("acc\n")
        #print "%s %f %f %f" % (path, acc_x, acc_y, acc_z)

    #receive EEG data
    @make_method(None, 'ffff')
    def eeg_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        file = open("data.txt", "w")
        #average for now
        data = (l_ear + l_forehead + r_forehead + r_ear)/4
        file.write(data)
        print ("here\n")

    #handle unexpected messages
    @make_method(None, None)
    def fallback(self, path, args, types, src):
        print('fallback\n')
        #print ("Unknown message \
        #\n\t Source: '%s' \
        #\n\t Address: '%s' \
        #\n\t Types: '%s ' \
        #\n\t Payload: '%s'" \
        #% (src.url, path, types, args))

try:
    server = MuseServer()
except ServerError(err):
    print (err)
    sys.exit()
print("I am running\n")

server.start()

if __name__ == "__main__":
    while 1:
        time.sleep(1)
