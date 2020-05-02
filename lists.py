bicycles = ['trek', 'cannondle', 'huffy', 'shwinn']
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])
message = f"My first bicyle was a {bicycles[0].title()}."
print(message)
shrooms = ['psylocybin', 'azurnces', 'mexicana', 'boys from brazil']
message = f"I especially love {shrooms[2].title()} mushrooms"
print(message)
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[1] = 'ktm'
print(motorcycles)
motorcycles.append('yamaha')
print(motorcycles)
devices =[]
devices.append('android')
print(devices)
devices.append('apple')
print(devices)
# good job Robert
del motorcycles[1]
print(motorcycles)
# pop and poppped
metals = ['iron', 'aluminum', 'stainless']
popped_metals = metals.pop()
print(metals)
print(popped_metals)
last_scrapped = metals.pop()
print(f"the last metal i scrapped was {last_scrapped.title()}.")
too_expensive = 'iron'
metals.remove(too_expensive)
print(metals)
print(f"nA{too_expensive.title()} is too expensive for me.")
guests = ['george boole', 'albert einstein', 'bill gates']
print(f"i would like to invite {guests} to dinner")
del(guests[1])
print(guests)
guests.append('einstein')
print(guests)
print(f"i would like to invite {guests} to dinner")
print(f"a larger venue has become available {guests}")
# sort
cars = ['bmw', 'vw', 'honda']
cars.sort()
print(cars)
cars.reverse()
print(cars)
cars=["bmw", "audi", "toyota", "subaru"]
len(cars)
