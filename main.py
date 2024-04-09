# Get the base of a URL in Python 

from urllib.parse import urlparse

my_url = 'https://bobbyhadz.com/images/wallpaper.jpg'

parsed = urlparse(my_url)
# 👇️ ParseResult(scheme='https', netloc='bobbyhadz.com', path='/images/wallpaper.jpg', params='', query='', fragment='')
print(parsed)

base = parsed.netloc
print(base)  # 👉️ bobbyhadz.com

path = parsed.path
print(path)  # 👉️ /images/wallpaper.jpg

with_path = base + '/'.join(path.split('/')[:-1])
print(with_path)  # 👉️ bobbyhadz.com/images

print(path.split('/'))  # 👉️ ['', 'images', 'wallpaper.jpg']