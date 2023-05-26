class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def configure(self):
        print(f"Hp omen have core {self.cpu}, and {self.ram} ram" )


Hp_omen=computer("i7","16gb")
Hp_omen.configure()
print(id(Hp_omen))