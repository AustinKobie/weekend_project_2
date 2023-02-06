class Parking_Garage:
    def __init__(self):
        self.ticket_supply = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.parking_spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.paid_ticket = {'paid': False,
                            'ticket': None
                            }


    def issue_ticket(self):
        enter_garage = input(
            "Would you like to enter the garage? (y/n):").lower()
        if enter_garage == "y":
            if self.ticket_supply:
                ticket = self.ticket_supply.pop()
                self.paid_ticket['ticket'] = ticket
                print(f"Your ticket number is {ticket}. Please pay $5.00")
            else:
                print("No more tickets available at this time.")
        else:
            print("If you still need a spot, we'll be here.")
            return
        
        
    def pay_for_parking_ticket(self):
        take_payment = input("Please enter payment amount.")
        payment = float(take_payment)
        if payment >= 5.0:
            change = payment - 5.0
            print(f"Your payment has been received. Please leave in the next 15 minutes. Thank you for the ${change} tip!!")
            self.paid_ticket['paid'] = True


    def leave_garage(self):
        if self.paid_ticket['paid'] == True:
            print("Thank you, have a nice day!")
            self.paid_ticket['paid'] = False
            self.parking_spaces.append(self.paid_ticket['ticket'])
            self.paid_ticket['ticket'] = None
        else:
            print("Payment is now due")
            payment_due = input("Please pay $5.00")
            payment = float(payment_due)
            if payment:
                print(
                    "Your payment has been received. Please leave in the next 15 minutes.")
                self.parking_spaces.append(self.paid_ticket['ticket'])
                self.paid_ticket['paid'] = False
                self.paid_ticket['ticket'] = None


parking_garage = Parking_Garage()
parking_garage.issue_ticket()
if parking_garage.paid_ticket['ticket']:
    parking_garage.pay_for_parking_ticket()
    parking_garage.leave_garage()
