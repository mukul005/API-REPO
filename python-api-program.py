import requests
import sys
import urllib.request
from goto import with_goto

# Check if URL is responding or not

def CHECK_URL(URL):
    return urllib.request.urlopen(URL).getcode()

@with_goto
def main():

# Taking details

    movie_name=sys.argv[1:]
    URL = 'http://www.omdbapi.com'
    api_key='88deb2b'
    PARAMS = {'t':movie_name, 'r': 'json', 'apikey': api_key}

# Checking if URL is up or not
    try:
        if CHECK_URL(URL) == 200:
           print("URL is working fine")

    except:
        print("URL is not working")
        goto .END

# Working on extracting information

    data_json = requests.get(url = URL, params=PARAMS).json()


    if 'Invalid API key!' in data_json.values():
        print("Invalid API key has been provided, please use correct key")
        goto .END


    try:

        Ratings=data_json["Ratings"]

        try:

            for i in Ratings:
                if 'Rotten Tomatoes' in i['Source']:
                    rotten=i
            Percent=rotten['Value']


            if int(Percent[:len(Percent)-1]) <30:
                print("This movie has rating below 30% on Rotten tomatoes, can be ignored")
                print("Rotten Tomatoes Rating : ",rotten['Value'])
            else:
                print("This movie has rating above 30% on Rotten tomatoes and could be watched atleast once.")
                print("Rotten Tomatoes Rating :  ",rotten['Value'])

        except:
            print("No Rotten Tomatoes rating found")

    except:
        print("There is no such movie, try again")

    label .END

if __name__== "__main__":
        main()
