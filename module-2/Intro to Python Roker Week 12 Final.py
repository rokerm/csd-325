import requests, json

welcomePage = input("Welcome the free weather map! Press enter to continue... \n")
#city main function
def city():
  city = input("Enter a city: ")
  url = 'https://api.openweathermap.org/data/2.5/weather?q={},US&units=imperial&APPID=4eb7f9134266ab96779f64e411481398'.format(city)
  response = requests.get(url)
  weatherData = response.json()
  show_data(weatherData)
  tryAgain = input("Would you like to search another location? \n")
  if tryAgain == 'Yes' or tryAgain == 'yes':
    main()
  if tryAgain == 'No' or tryAgain == 'no':
    print("Thanks for choosing our service! Hope to see you again!")
    exit()
#zipcode main function
def zip():
  zip = input("Enter a zip code: ")
  url = 'https://api.openweathermap.org/data/2.5/weather?zip={},US&units=imperial&APPID=4eb7f9134266ab96779f64e411481398'.format(zip)
  response = requests.get(url)
  weatherData = response.json()
  show_data(weatherData)
  tryAgain = input("Would you like to search another location? \n")
  if tryAgain == 'Yes' or tryAgain == 'yes':
    main()
  if tryAgain == 'No' or tryAgain == 'no':
    print("Thanks for choosing our service! Hope to see you again!")
    exit()
  
  
def quit():
  print("Thanks for choosing our service! Hope to see you again!")
  exit()
#displays json to a readable format
def show_data(weatherData):
  temp = weatherData['main']['temp']
  hightemp = weatherData['main']['temp_max']
  lowtemp = weatherData['main']['temp_min']
  wind_speed = weatherData['wind']['speed']
  press = weatherData['main']['pressure']
  latitude = weatherData['coord']['lat']
  longitude = weatherData['coord']['lon']
  humid = weatherData['main']['humidity']
  description = weatherData['weather'][0]['description']
  print('Your connection was successful')
  print('Current Temperature : {} degrees fahrenheit'.format(temp))
  print('High Temperature : {} degrees fahrenheit'.format(hightemp))
  print('Low Temperature : {} degrees fahrenheit'.format(lowtemp))
  print('Wind Speed : {} m/s'.format(wind_speed))
  print('Pressure : {} hPa'.format(press))
  print('Latitude : {}'.format(latitude))
  print('Longitude : {}'.format(longitude))
  print('Humidity : {} %'.format(humid))
  print('Description : {}'.format(description))
#menu main function for user input
def main():
  while True:
    menu = input("Our menu options allows you to search by city or zip code to see weather details in a specific area. \n 1. Enter 'C' to search a city. \n 2. Enter 'Z' to search zip code. \n 3. Enter 'Q' to quit. \n")
    if menu == 'C' or menu == 'c':
      try:
        city()
      except Exception:
        print("Your entry did not work. Please Try again.")
        city()
    if menu == 'Z' or menu == 'z':
      try:
        zip()
      except Exception:
        print("Your entry did not work. Please Try again.")
        zip()
    if menu == 'Q' or menu == 'q':
      try:
        quit()
      except Exception:
        print("Your entry did not work. Please Try again.")
        quit()
    else:
      print("We don't support that. Try again.")
main()

    
      
  

