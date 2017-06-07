'''Bike assignment at Coding Dojo.
by: Troy Center, troycenter1@gmail.com, Coding Dojo Python fundamentals, June 2017
'''
#pylint: disable=C0103
class Bike(object):
    ''' Bike Class
    '''
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        '''Display the bike info
        '''
        print "Bike info: Price: %s Max Speed: %s Miles: %s" %(
            self.price, self.max_speed, self.miles)
        return self

    def ride(self):
        '''display "riding" on the screen and increase the total miles ridden by 10
        '''
        print "Riding... "
        self.miles += 10
        return self

    def reverse(self):
        '''display "Reversing" and descrease the total miles by 5, not less than 0
        '''
        print "Reversing... "
        self.miles -= 5
        if self.miles < 5:
            self.miles = 0
        return self

bike1 = Bike(200, "25mph")
bike2 = Bike(220, "30mph")
bike3 = Bike(1200, "55mph")


bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()

