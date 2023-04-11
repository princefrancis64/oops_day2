class bank:
    def transaction(self):
        print("total transaction value")
    def account_opening(self):
        print("this will show you your account open status")
    def deposit(self):
        print("this will show you deposited amount")

    def test(self):
        print("this is a test method from bank class")

class HDFC_bank:
    def hdfc_to_icici(self):
        print("this will show you all the transactions to icici through hdfc")

    def test(self):
        print("this is a test method from hdfc bank")

class ineuron_bank:
    def account_status_icici(self):
        print("print account status in icici")

class icici(HDFC_bank,bank,ineuron_bank):
    pass

i = icici()
i.deposit()
i.hdfc_to_icici()
i.transaction()
i.account_opening()
i.test()
i.account_status_icici()