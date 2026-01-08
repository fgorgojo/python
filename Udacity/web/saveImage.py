import requests
import random

image_url = 'https://images.ctfassets.net/2y9b3o528xhq/4swf2qhcelEUWzKHaKne6C/d890de3220ea332fb42e9b8e5f7848fd/real-world-projects.png'

r = requests.get(image_url)
tmp = f'./tmp/{random.randint(0,100000000)}.png'

with open(tmp, 'wb') as img:
    img.write(r.content)

# This approach will also work:
# img = open(tmp, 'wb')
# img.write(r.content)
# img.close()

print(tmp)