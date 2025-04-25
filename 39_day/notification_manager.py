

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        pass

    def send_message(self, flight_data):
        message = f"Low price allert! Only {flight_data['price']}{flight_data['currency']} to flight from {flight_data['from']} to {flight_data['to']}, on {flight_data['departure_time']}"
        print(message)