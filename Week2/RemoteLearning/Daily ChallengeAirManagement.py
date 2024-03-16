import datetime
import random
from faker import Faker

fake = Faker()


class Airline:
    def __init__(self, airline_id, name):
        self.airline_id = airline_id
        self.name = name
        self.planes = []


class Airplane:
    def __init__(self, airplane_id, company):
        self.airplane_id = airplane_id
        self.current_location = None
        self.company = company
        self.next_flights = []

    def __str__(self):
        return f"Airplane {self.airplane_id}"

    def fly(self, destination):
        if self.available_on_date(destination.date, self.current_location):
            print(f"Flight {destination.id} scheduled for airplane {self.airplane_id}")
            destination.schedule_flight(self, destination.date)
            self.current_location = destination
        else:
            print(f"Airplane {self.airplane_id} cannot fly to {destination.city} on {destination.date}")

    def location_on_date(self, date):
        for flight in self.next_flights:
            if flight.date == date:
                return flight.destination.city
        return self.current_location.city if self.current_location else None

    def available_on_date(self, date, location):
        return self.location_on_date(date) == location.city and not self.next_flights


class Flight:
    def __init__(self, flight_id, date, origin, destination, plane):
        self.flight_id = flight_id
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane

    def __str__(self):
        return f"Flight: {self.flight_id}, Date: {self.date}, Origin: {self.origin}, Destination: {self.destination}"

    def take_off(self):
        print(f"Flight {self.flight_id} takes off")

    def land(self):
        print(f"Flight {self.flight_id} lands at {self.destination.city}")
        self.plane.current_location = self.destination


class Airport:
    def __init__(self, city):
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []

    def schedule_flight(self, destination, datetime):
        if self.planes:
            plane = self.planes.pop(0)
            flight_id = f"{destination.city}_{plane.company.airline_id}_{datetime.strftime('%Y%m%d')}"
            flight = Flight(flight_id, datetime, self, destination, plane)
            plane.next_flights.append(flight)
            self.scheduled_departures.append(flight)
            destination.scheduled_arrivals.append(flight)
            print(f"Flight {flight_id} scheduled from {self.city} to {destination.city} on {datetime.strftime("%Y-%m-%d %I:%M %p")}")
        else:
            print(f"No available airplanes at {self.city}")

    def info(self, start_date, end_date):
        print(f"Scheduled flights from {self.city} between {start_date.strftime("%Y-%m-%d %I:%M %p")} and {end_date.strftime("%Y-%m-%d %I:%M %p")}:")
        for flight in self.scheduled_departures:
            if start_date <= flight.date <= end_date:
                print(f" - Flight {flight.flight_id} to {flight.destination.city} on {flight.date.strftime("%Y-%m-%d %I:%M %p")}")


# Test code
el_al_airline = Airline("EA", "El-Al Airline")
red_wings = Airline("RW", "Red Wings")
ben_gurion = Airport("Tel-Aviv")
pulkovo = Airport("Saint-Petersburg")
first_plane = Airplane(123, el_al_airline)
second_plane = Airplane(456, el_al_airline)
third_plane = Airplane(789, red_wings)
el_al_airline.planes.append(first_plane)
el_al_airline.planes.append(second_plane)
red_wings.planes.append(third_plane)
ben_gurion.planes.append(first_plane)

now = datetime.datetime.now()
tomorrow = now.replace(hour=0, minute=0, second=0) + datetime.timedelta(days=1)




ben_gurion.schedule_flight(pulkovo, tomorrow)
print("-------")
ben_gurion.info(now, tomorrow)
