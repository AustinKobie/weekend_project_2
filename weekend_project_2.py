class Parking_Garage:
    def __init__(self):
        self.take_ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.parking_Spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.paid_ticket = {'paid': False, 'ticket': None}
    
# Ask user if they would like to enter the garage in no then end program if yes then
#give a ticket to user unless we are out of tickets/spaces.
    def take_ticket(self):
        enter_garage = input("Would you like to enter the garage? (y/n):").lower()
        if True == "y":
            if self.take_ticket:
                ticket = self.take_ticket.pop()
                self.paid_ticket['ticket'] = ticket
                print("Your ticket number is {ticket}.")
            else:
                print("No more tickets available at this time.")
        else:
            print("Are you sure you would like to find a space elsewhere?")
            
#as the user for payment, they will need to input the ammount
# If the payment variable is not empty then (meaning the ticket has been paid) -> 
# display a message to the user that their ticket has been paid and they have 15mins to leave        
#  This should update the "currentTicket" dictionary key "paid" to True     
    def pay_for_parking_ticket(self):
        take_payment = input("Please enter a payment amount.")
        if take_payment:
            print("Your payment has been received. Please leave in the next 15 minutes.")
            
 # take payment from user for ticket and ask them to leave garage
 #if ticket has not neen paid prompt user for payment
 # once ticket is paid display a message thanking user   
    def leave_garage(self):
        if self.paid_ticket['paid'] = True
            print("Thank you, have a nice day!")
            self.paid_ticket['paid'] = False
        else:
            print("Payment is now due"):
            payment_due= input("Please pay 5.00")
            if take_payment:
            print("Your payment has been received. Please leave in the next 15 minutes.")

            self.parking_Spaces.append(self.paid_ticket['ticket'])
            self.parking_Spaces.append(self.parking_Spaces)

