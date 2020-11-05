from user import authentication
from transactions import journal
import banking
import sys
import requests

if __name__ == '__main__':

    for i in sys.argv[1:]:
        print(i)
    
    authentication.authenticate_user()
    journal.receive_income(100.00)
    journal.pay_expense(100.00)
    banking.do_reconciliation()
    # help("modules")