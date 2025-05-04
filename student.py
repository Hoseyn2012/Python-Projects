class telebe:
    def __init__(self,ad,yas,bal):      
        self.ad = ad
        self.yas = yas
        self.bal = bal
    def qiymet(self):
        if self.bal>90:
            return "Ela"
        elif 89>=self.bal>=70:
            return "Yaxsi"
        elif 69>=self.bal>=50:
            return "Kafi"
        else:
            return "zəif"
    def melumat(self):
        print('ad:',self.ad)
        print('yas:',self.yas)
        print('bal:',self.bal)
        print("qiymet",self.qiymet())
        print("-----------------")
t1=telebe("Negr",89,100)
t2=telebe("Nigga",71,3)
t3=telebe("bombardinocapucino",19,87)
t1.melumat()
t2.melumat()
t3.melumat()