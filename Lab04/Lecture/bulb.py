
class bulb():
    'here is a test of defining bulb'
    def __init__(self, bulb_status=False,bulb_name='PUTA2021 bulb'):
        self.switch=bulb_status
        self.bulb_name=bulb_name

    def print_onoff(self):
#         print (__name__)

        if self.switch==True:
            print ('this is %s. I am on'%self.bulb_name)
        else:
            print ('this is %s. I am off'%self.bulb_name)

    def bulb_switch_on(self):

        if self.switch==True:
            pass
        if self.switch==False:
            self.switch=True

    def bulb_switch_off(self):

        if self.switch==False:
            pass
        if self.switch==True:
            self.switch=False
