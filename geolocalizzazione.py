
import geopy
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my-app")
#indirizzo , cap CITTA MI, Italy
#address = "Piazza del Duomo, 20122 Milano MI, Italy"

address = "Via Novara, Piazza Carlo Amati, 31, 20147 Milano MI, Italy "
location = geolocator.geocode(address)
# Print the latitude and longitude
print("Latitude:", location.latitude)
print("Longitude:", location.longitude)

#loca= "Latitude: 45.463910150000004, Longitude: 9.190642626255652"
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my-app")

loca = geolocator.reverse("45.463910150000004, 9.190642626255652")

#print(loca.address)
#Potsdamer Platz, Mitte, Berlin, 10117, Deutschland, European Union

#print((loca.latitude, location.longitude))
#(52.5094982, 13.3765983)

#print(loca.raw)
#{'place_id': '654513', 'osm_type': 'node', ...