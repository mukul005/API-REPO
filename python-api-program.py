import requests
import sys
def MovieTitle():
     movie_name=sys.argv[1:]
     movie_url=f"http://www.omdbapi.com/?apikey=88deb2b&t={movie_name}"
     return movie_url


def main():
    movie_url=MovieTitle()
    data = requests.get(url = movie_url)
    data_json = data.json()
    try:
        Ratings=data_json["Ratings"]
        try:
            for i in Ratings:
                if 'Rotten Tomatoes' in i['Source']:
                    rotten=i
            Percent=rotten['Value']

            if int(Percent[:len(Percent)-1]) <30:
                print("This doesn't appears to be good movie as it has low rating on Rotten Tomatoes.")
                print("Rotten Tomatoes Rating : ",rotten['Value'])
            else:
                print("It seems to be good movie as it has high rating on Rotten Tomatoes.")
                print("Rotten Tomatoes Rating :  ",rotten['Value'])
        except:
            print("No Rotten Tomatoes rating found")

    except:
        print("There is no such movie, try again")

if __name__== "__main__":
        main()
