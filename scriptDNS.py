from requests import get
import requests
import os


ip = get("https://api.ipify.org").text

archivo_ip = open("ippublic.txt","r").readline(30)

if ip == archivo_ip:
    print("la ip no ha cambiado")
else:
    os.system("curl -X GET https://ipv4.api.hosting.ionos.com/dns/v1/dyndns?q=OWMyZDM0ODRmYjI5NDRiNzgxNWU3YTg0MmQyNGU4YTYueWU4NmRSWjlnSE5nVVJldEZSWjlGN2lzYjllZEwyQzMxTjdaRXJWSlJyc2xHRl9mcUZ2aUd2eWM4dk9taUtiSE1xN3M4SXFSNjZJMFU0ZmNIYmRRNmc")
    open("ippublic.txt","w").write(str(ip))
