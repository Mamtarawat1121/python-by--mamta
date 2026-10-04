from abc import ABC,abstractmethod
class BankApp:
    def database(self):
        print('connected to database')
    @abstractmethod
    def security(self):
        pass  
    
class MobileApp(BankApp):
    def mobile_login(self):
        print('login into mobile') 
    def security(self):
        print('mobile security')     
mob = MobileApp()    
mob.security()        