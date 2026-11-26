#import re
#import subprocess
import requests

url = "http://212.2.244.181/entries"
url = "https://quiquak.de/entries"
headers = {"Host": "quiquak.de"}


#def get_cpu_temp():
   # try:
   #     output = subprocess.check_output(["osx-cpu-temp"], text=True, timeout=5).strip()
   #     match = re.search(r"([0-9]+(?:\.[0-9]+)?)", output)
   #     if match:
   #         return float(match.group(1))
  #  except (FileNotFoundError, subprocess.SubprocessError, ValueError):
   #     return None
 #   return None


#temp = get_cpu_temp()

#if temp is None:
#    print("Keine CPU-Temperatur gefunden (ist osx-cpu-temp installiert?).")
#else:
payload = {
        "name": "Mac-Sensor",
       # "message": f"CPU-Temperatur: {temp:.1f} °C",
       "message": f"CPU-Temperatur: 45 °C",
    }
response = requests.post(url, json=payload, headers=headers, timeout=10)
print("Status Code:", response.status_code)
print("Antwort:", response.text)