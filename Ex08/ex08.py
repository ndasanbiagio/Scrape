import requests
import json


url = "https://graph.facebook.com/v19.0/324421833964703?fields=id%2Cname%2Cposts&access_token=EAAFzT2ucsXoBOzNfpQzmaLSXEag7390og0taO2DNk75JCyynRf7DdX14tsFbfPsT5ZAXwtS2Tq5BB1f6tevgXCc3hKtLmzJRdoX5lJWMCtyZBtp7OmTWAo98TkAshlrEVFCs8BnQZBautWjPtO6Dx3cBfZAJOQmpKZAetqpdulqatQM1cDceCB1CdsfrqIolLsKEZCo2Q6D2KBm03UiW1ixiLVZAw38JtDL4qkdXRn2y3URxAXZA3ZBTs"

response = requests.get(url)
data = response.text

data = json.loads(data)
image_url = data['images'][0]['source'] 

image_bytes = requests.get(image_url).content

with open('image.jpg', 'wb') as file:
    file.write(image_bytes)