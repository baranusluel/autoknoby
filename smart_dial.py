import string
import cognitive_face as CF



KEY = '96ac51d9ccf74f258ecfc1ae8ece5e44'
CF.Key.set(KEY)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)

img_urls = [
    'https://img.thedailybeast.com/image/upload/c_crop,d_placeholder_euli9k,h_1440,w_2560,x_0,y_0/dpr_2.0/c_limit,w_740/fl_lossy,q_auto/v1527786393/180531-Tani-_CNN_Blasts_Morgan_Freeman-hero_dyfqf1',
    'https://timedotcom.files.wordpress.com/2017/12/barack-obama.jpeg']

faces = [CF.face.detect(img_url) for img_url in img_urls]

# Assume that each URL has at least one face, and that you're comparing the first face in each URL
# If not, adjust the indices accordingly.
similarity = CF.face.verify(faces[0][0]['faceId'], faces[1][0]['faceId'])
print (similarity)


