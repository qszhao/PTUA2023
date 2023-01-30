class bulb():
    'here is a test of defining bulb'
    def __init__(self, bulb_status=False,bulb_name='PTUA2023_bulb'):
        self.status=bulb_status
        self.bulb_name=bulb_name
    
    def print_onoff(self):
#         print (__name__)

        if self.status==True:
            print ('this is %s. I am on'%self.bulb_name)
        else:
            print ('this is %s. I am off'%self.bulb_name)

    def bulb_switch_on(self):

        if self.status==True:
            pass
        if self.status==False:
            self.status=True
            
    def bulb_switch_off(self):

        if self.status==False:
            pass
        if self.status==True:
            self.status=False