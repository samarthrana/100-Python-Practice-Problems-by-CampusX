# Write a program that will determine weather when the value of temperature and humidity is provided by the user.
# TEMPERATURE(C)      HUMIDITY(%)      WEATHER

#       >= 30                             >=90                Hot and Humid
#       >= 30                             < 90                 Hot
#       <30                                >= 90               Cool and Humid
#       <30                                 <90                 Cool

def how_weather(temp, humid):

    weather = ""
    if temp >= 30 and humid >= 90:
        return "Hot and Humid"
    if temp <= 30 and humid < 90:
        return "Hot"
    if temp < 30 and humid >= 90:
        return "Cool and Humid"
    if temp < 30 and humid < 90:
        return "Cool"

print(how_weather(40, 100))




