#Jack Zemke
#Assigment 10.1- Your Own Class
#The purpose of this assignment is to practice designing and implimenting our own classes

class Television:
    __brand='Panasonic' #class variable applies to all objects created within the class
    def __init__(self,pwr,chnl,vol): #constructor, takes in constructor args
        if type(pwr)!=bool: #power level. Checks to make sure its a boolean
            raise TypeError("Please select a Boolean Value to set the TV on or off (True=ON, False=OFF)")
        else:
            self.__power=pwr #if input is Boolean, assign variable to input
        if type(chnl)!=int: #channel. makes sure input is an integer
            raise TypeError(f"Please input an Integer value for the Channel. There is no Channel '{chnl}'")
        else:
            self.__channel=chnl #if input is an integer, assign variable to input
        if type(vol)!=int: #volume. makes sure input is an integer
            raise TypeError('please input an Integer for the Volume.')
        else:
            self.__volume=vol #if input is an integer, assign variable to input
    def setchannel(self,c): #straightforward 'set' method
        if self.__power==True: #ensures the TV is on
            if type(c)==int: #ensures input is correct type (int)
                self.__channel=c #if both criteria are met, update variable with input
            else: #otherwise raise corresponding error
                raise TypeError(f"Please input an Integer value for the Channel. There is no Channel '{c}'")
        else:
            raise SyntaxError('Error. Television must be ON to set the channel\n \
            \t-Try using the "setpower" method and setting it to "True" first')    
    def setpower(self,p): #also straightforward
        if type(p)==bool: #check input type
            self.__power=p #if correct input, update power level with input
        else: #otherwise raise error
            raise TypeError('Error. Please select a Boolean Value (True=ON, False=OFF)')
    def setvol(self,v): #exact same method as setchannel but for volume. Only a few changes (as noted)
        if self.__power==True:
            if type(v)==int:
                self.__volume=v #change here, update volume variable with input
            else: #error messages pertain to volume instead of channel
                raise TypeError('please input an Integer for the Volume.')
        else:
            raise SyntaxError('Error. Television must be ON to set the volume \n\t \
            -Try using the "setpower" method and setting it to "True" first')
    def getpower(self): #straightforward 'get' method. 
        if self.__power==True: #display power status (on or off)
            return 'The TV is ON'
        elif self.__power==False:
            return 'The TV is OFF'
    def getvol(self): #also straightforward 'get' method
        if self.__power==True: #check to ensure TV is on
            return f'the current volume is {self.__volume}.' #if criteria are met, return volume
        else: #otherwise raise error
            raise SyntaxError('Error. Television must be ON to set the volume \n\
            \t-Try using the "setpower" method and setting it to "True" first')
    def getchannel(self): #exact same as getvol but with chanel instead. Few changes as noted
        if self.__power==True:
            return f'You are currently on Channel {self.__channel}.' #refer to channel instead of vol
        else: #errors pertain to channel instad of vol
            raise SyntaxError('Error. Television must be ON to get the channel\n\
            \t-Try using the "setpower" method and setting it to "True" first')    
    def volup(self):
        if self.__power==True: #checks the TV is on
            self.__volume+=1 #if criteria is met, add 1 to volume value
        else: #otherwise print error
            raise SyntaxError('Error. Television must be ON to change the volume\n\
            \t-Try using the "setpower" method and setting it to "True" first')
    def voldown(self): #exact same as volup but subtracts 1 from volume instead of adds
        if self.__power==True:
            self.__volume-=1
        else:
            raise SyntaxError('Error. Television must be ON to change the volume\n\
            \t-Try using the "setpower" method and setting it to "True" first')
    def getbrand(self): #return brand of TV. very straightforward
        return f'The TV is manufactured by {self.__brand}.'
    def channelup(self):
        if self.__power==True: #checks the TV is on
            self.__channel+=1 #if criteria is met, add 1 to channel value
        else: #otherwise print error
            raise SyntaxError('Error. Television must be ON to change the channel\n\
            \t-Try using the "setpower" method and setting it to "True" first')
    def channeldown(self): #exact same as channelup but subtracts 1 from volume instead of adds
        if self.__power==True: 
            self.__channel-=1 #only difference from channelup
        else: 
            raise SyntaxError('Error. Television must be ON to change the channel\n\
            \t-Try using the "setpower" method and setting it to "True" first')



def main(): #demo program
    x=Television(True,12,16) #construct the TV. TV is on, channel 12, volume 16

    y=x.getpower() #first method we demonstrate. Getpower
    print(y) #print the result of getpower. The TV should be on and this method should return that.

    x.voldown() #next we lower the volume by 1
    
    z=x.getvol() #and then we showcase getvol and voldown at once. 
    print(z) #should display the new current volume, 15

    x.channelup() #go up one channel
    d=x.getchannel() #get channel
    print(d) #should return channel 13 as we went up one channel from construction

    x.setvol(100) #setvol to 100
    z=x.getvol() #get the volume. should print new volume of 100
    print(z)

    x.setchannel(29) #setchannel to 29
    p=x.getchannel() #should return new channel value of 29
    print(p)

    x.setpower(False) #turn the TV off
    g=x.getpower() #display updated power level 
    print(g)

    v=x.getbrand() #display brand (panasonic)
    print(v)

    x.volup() #The TV is off, so this should raise an error

if __name__=='__main__': #run demo program
    main()