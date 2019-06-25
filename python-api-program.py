# importing the requests library 
import requests 
def MovieTitle():
	movie_name=str(input("Enter the search string : "))
	
	cmd=str(f"http://www.omdbapi.com/?apikey=88deb2b&t={movie_name}")
	return cmd


def main():
	while True:
		cmd=MovieTitle()
		r = requests.get(url = cmd) 
# extracting data in json format 
		data = r.json()
		if 'Error' in data:
			print("This is not a valid movie name")

			truth_value=input("Do you want to type movie name again?(y/n) : ")
			if truth_value != 'y':
				exit()
			continue
		
			
		else:
			try:
				Ratings=data["Ratings"]
				for i in Ratings:
					if 'Rotten Tomatoes' in i['Source']:
						rotten=i
					
				Percent=rotten['Value']
				if int(Percent[:len(Percent)-1]) <30:
					print("You can watch this movie as rotten tomatoes is only",rotten['Value'])
				else:
					print("Don't watch this movie as it does not seems to be good movie and it has rotten tomatoes value ",rotten['Value'])

			except:
				print("There isn't any rating found for this script")
			exit()


if __name__== "__main__":
	main()
