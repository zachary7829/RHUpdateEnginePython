import requests
import re

inputdict = {"Current Version":"3.001"}
oldver = (inputdict.get("Current Version"))
print(oldver)

url = "https://routinehub.co/api/v1/shortcuts/2502/versions/latest"
data = requests.get(url, timeout=5.00)
print(data.json().get("Version"))
newver = (data.json().get("Version"))

if oldver != newver:
  oldver = int(re.search(r'\d+', oldver).group())
  oldver = str(oldver)
  #Removes all but first period from oldver
  if "." in oldver:
   oldver1 = re.sub(r'^.*?{}'.format(re.escape(".")), '', oldver, flags=re.DOTALL).strip()
   oldver2 = [pos for pos, char in enumerate(oldver) if char == "."]
   oldver2 = oldver2[0]
   oldver2 = oldver[0:oldver2]
   oldver = oldver2 + "." + oldver1.replace(".", "")
   print(oldver)

  newver = int(re.search(r'\d+', newver).group())
  newver = str(newver)
  if "." in newver:
   newver1 = re.sub(r'^.*?{}'.format(re.escape(".")), '', newver, flags=re.DOTALL).strip()
   newver2 = [pos for pos, char in enumerate(newver) if char == "."]
   newver2 = newver2[0]
   newver2 = newver[0:newver2]
   newver = newver2 + "." + newver1.replace(".", "")
   print(newver)
  
  oldver = int(oldver)
  newver = int(newver)
  if oldver > newver:
    print("Rollback")
  else:
    print("Update Detected")
else:
  print("No Update Found")