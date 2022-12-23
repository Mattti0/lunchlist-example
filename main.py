import sys
import tomllib
from restaurants import restaurants

restaurantsconfig = None
with open("restaurants/config.toml", "rb") as tomlconfig:
    restaurantsconfig = tomllib.load(tomlconfig)

if restaurantsconfig is None:
    sys.exit(-1)

restaurants.importRestaurantPlugins(restaurantsconfig.get("restaurants"))

for restaurant in restaurants.getAllRestaurants():
    print(f"{restaurants.getNameForRestaurant(restaurant)}")
    for item in restaurants.getListForRestaurant(restaurant):
        try:
            print(f"{  item}")
        except KeyError:
            pass