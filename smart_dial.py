import string
import cognitive_face as CF



KEY = '96ac51d9ccf74f258ecfc1ae8ece5e44'
CF.Key.set(KEY)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)

img_urls = [
    'https://www.biography.com/.image/t_share/MTE4MDAzNDEwNzg5ODI4MTEw/barack-obama-12782369-1-402.jpg',
    'https://timedotcom.files.wordpress.com/2017/12/barack-obama.jpeg']

faces = [CF.face.detect(img_url) for img_url in img_urls]

# Assume that each URL has at least one face, and that you're comparing the first face in each URL
# If not, adjust the indices accordingly.
similarity = CF.face.verify(faces[0][0]['faceId'], faces[1][0]['faceId'])
print similarity


