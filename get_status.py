import cognitive_face as CF
from global_variables import personGroupId

Key = 'dc1527b9a0114e3fad617f95d71656c1'
CF.Key.set(Key)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

res = CF.person_group.get_status(personGroupId)
print (res)
