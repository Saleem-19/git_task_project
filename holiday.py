#dictionaries containing the cost of flights, hotel and car rental
flights_price = {"london": 1000, "new york": 1400, "paris": 895, "dubai": 995}
hotel_cost_per_night = {"london": 150, "new york": 230, "paris": 160, "dubai": 300}
daily_rental_cost = {"london": 40, "new york": 50, "paris": 45, "dubai": 55}
#the following three lines gathers the users input 
city_flight = input("Which city are you flying to? ").lower()
num_nights = int(input("How many nights will you be staying at the hotel? "))
rental_days = int(input("How many days will you be hiring a car for? "))

# plane cost checks if city_flight is in the flights_price dictionary and returns the cost of the flight if it is, otherwise it returns 0
def plane_cost(): 
    if city_flight in flights_price:    
        print(f"The price of your flight is {flights_price[city_flight]}")
        return flights_price[city_flight]
    else:
        print("Sorry, we don't fly to that destination")
        return 0
     
def hotel_cost():
    if city_flight in hotel_cost_per_night:
        print(f"The cost of your hotel stay is {hotel_cost_per_night[city_flight] * num_nights}")
        return hotel_cost_per_night[city_flight] * num_nights
    else:
        print("Sorry, we don't have a hotel in that destination")
        return 0

def rental_cost():
    if city_flight in daily_rental_cost:
        print(f"The cost of your car rental is {daily_rental_cost[city_flight] * rental_days}")
        return daily_rental_cost[city_flight] * rental_days
    


#create a another function to calculate the total cost of the holiday
def holiday_cost():
    return plane_cost() + hotel_cost() + rental_cost()


print(f"The total cost of your holiday is {holiday_cost()}")