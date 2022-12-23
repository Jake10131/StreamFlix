import requests
import webbrowser

def main():
  print("""
   _____ _                            ______ _ _      
  / ____| |                          |  ____| (_)     
 | (___ | |_ _ __ ___  __ _ _ __ ___ | |__  | |___  __
  \___ \| __| '__/ _ \/ _` | '_ ` _ \|  __| | | \ \/ /
  ____) | |_| | |  __/ (_| | | | | | | |    | | |>  < 
 |_____/ \__|_|  \___|\__,_|_| |_| |_|_|    |_|_/_/\_\

  """)
  name = input("Enter the movie name: ")
  print(f"Searching for {name}")
  sitelink = f"https://seapi.link/?type=search&query={name}"
  url_results = requests.get(sitelink).json()
  results = url_results["results"]
  status = url_results["status"]
  movieurl = []
  index = 1
  if (status == 200):
    for result in results:
      if (result["size"] > 0):
        print(f'({index}){result["title"]} --> {result["quality"]}\n')
        index += 1
        movieurl.append(result["url"])
  if movieurl:
    choice = int(input("Enter the index of the moive: "))
    try:
      stream = movieurl[choice -1]
      webbrowser.open(stream)
    except IndexError:
      print("Incorrect Index entered")
  else:
    print(f"No results found for {name}")
if __name__ == "__main__":
  main()
