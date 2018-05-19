import cognitive_face as CF
from global_variables import personGroupId

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

Key = 'e72e6fd9e8964cdab9b1ba2cc1b14c7b'
CF.Key.set(Key)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

res = CF.person_group.train(personGroupId)
print (res)
