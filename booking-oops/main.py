import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_security = pd.read_csv("card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = 'no'
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """check Availability Of Hotels"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class SpaHotel(Hotel):
    def book_spa_package(self):
        pass


class Reservation:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thankyou for your Reservation!
        Here are the your Booking date:
        Name: {self.customer_name}
        Hotel Name: {self.hotel.name}
        """

        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validation(self, expiration, holder, cvv):
        card_data = {"number": self.number, "expiration": expiration, "cvc": cvv, "holder": holder}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_security.loc[df_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


class SpaTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your SPA reservation!
        Here are you SPA booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content


print(df)
hotel_id = input("Enter Hotel Id: ")
hotel = SpaHotel(hotel_id)
if hotel.available():
    credit_card = SecureCreditCard(number="1234567891023456")
    if credit_card.validation(expiration="12/26", holder="JOHN SMITH", cvv="123"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name = input("Please Enter the Customer Name: ")
            reservation = Reservation(customer_name=name, hotel_object=hotel)
            print(reservation.generate())
            spa = input("Do you want to book a spa package? ")
            if spa == "yes":
                hotel.book_spa_package()
                spa_ticket = SpaTicket(customer_name=name, hotel_object=hotel)
                print(spa_ticket.generate())
        else:
            print("Credit Card Authentication Failed!")
    else:
        print("There is an issue with yours credit card")
else:
    print("All Hotels are Filled")
