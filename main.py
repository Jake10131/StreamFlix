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
  def streamflix():
    name = input("Enter the movie name: ").strip()
    print(f"Searching for {name}")
    sitelink = f"https://seapi.link/?type=search&query={name}"
    url_results = requests.get(sitelink).json()
    results = url_results["results"]
    status = url_results["status"]
    movieurl = []
    moviename=[]
    index = 1
    if (status == 200):
      for result in results:
        if (result["size"] > 0):
          print(f'({index}){result["title"]} --> {result["quality"]}\n')
          index += 1
          movieurl.append(result["url"])
          moviename.append(result["title"])
    def stream(url,name):
      choice = int(input("Enter the index of the moive: ").strip())
      try:
        print(f'Playing: {name[choice -1]}')
        webbrowser.open(url[choice -1])
      except IndexError:
        print("Incorrect Index entered")
        stream(url,name)
    if movieurl:
      stream(movieurl,moviename)
    else:
      print(f"No results found for {name}")
      streamflix()
    repeat=int(input(r'Do you want to play another movie? (type 1 for "Yes" or 2 for "No": ').strip())
    if repeat==1:
      streamflix()
    else:
      exit()
  streamflix()
  
if __name__ == "__main__":
  main()
