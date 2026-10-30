travelers = int(input("Travelers:"))
nights = int(input("Nights:"))
hotel = float(input("the cost of the hotel per night:"))
transport_group = float(input("transportation costs per group"))
food_per_person = float(input("food per person per day"))

days = nights + 1
total_hotel = nights * hotel
total_food = travelers * days * food_per_person
total_trip = total_hotel + transport_group + total_food
cost_per_person = total_trip / travelers

print("Total hotel:", total_hotel)
print("Total food:", total_food)
print("Total trip:", total_trip)
print("Total cost:", cost_per_person)