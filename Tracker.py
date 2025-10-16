from skyfield.api import *

errors = 0
ts = load.timescale()
url = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle'

satellites = load.tle_file(url)

print (f"It has been found and loaded {len(satellites)} active satellites.")

by_name = {sat.name: sat for sat in satellites}

while True:
    
    satellite = input("Which satellite would you like to track? (Type 'exit' to exit the program)")
    satellite = satellite.strip()

    if satellite == 'exit':
        break 


    try: 
        tracking = by_name[satellite]
        print(f"Now tracking {tracking.name}")

        t = ts.now()

        geocentric = tracking.at(t)
        subpoint = geocentric.subpoint()

        longitude = subpoint.longitude.degrees
        latitude = subpoint.latitude.degrees

        print(f"Current position ({t.utc_strftime('%Y-%m-%d %H:%M:%S UTC')}):")
        print(f"  Latitude:  {latitude:.4f}°")
        print(f"  Longitude: {longitude:.4f}°")
        print("-" * 40)

        errors = 0

    except:
        
        errors += 1
        print("Invalid satellite code, please try again!")
        print("-" * 40)

        if errors > 3:
            print("It looks like you're having some trouble.")
            print("Please, head to: https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle")
            print("For more information")
            print("-" * 40)

