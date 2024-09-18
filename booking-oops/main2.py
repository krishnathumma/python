import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})


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

