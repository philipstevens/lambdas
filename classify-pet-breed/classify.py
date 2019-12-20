
try:
  import unzip_requirements
except ImportError:
  pass

import json
import tensorflow as tf
import numpy as np

from io import BytesIO
from PIL import Image
from requests_toolbelt.multipart import decoder

model = tf.keras.models.load_model('resources/oxford_iiit_pet_model')

with open(f'resources/class_dict.json', 'rb') as f:
    class_dict = json.loads(f.read().decode("utf-8"))

def classifyHandler(event, context):

    content_type_header = event['headers']['Content-Type']

    body = event['body'].encode()
    
    rawBytes = decoder.MultipartDecoder(body, content_type_header).parts[0].content

    # # TODO: why do rawBytes look off? why are they unable to be opened as image?

    # rawIO = BytesIO(rawBytes)
    # image = Image.open(rawBytes)

    # # image = np.array(image)
    # # image = tf.image.convert_image_dtype(image, tf.float32)
    # # image = tf.image.resize(image, (224,224))
    # # image = np.expand_dims(image, axis=0)
    # # prediction = model.predict_classes(image)[0]
    # # prediction = class_dict['prediction']

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'sample_bytes' : str(rawBytes)[:10000],
            'request_body' : str(event['body'][:10000])
            })
    }

    return response
