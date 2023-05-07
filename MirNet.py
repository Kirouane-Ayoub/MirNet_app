import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
import tensorflow as tf 
import numpy as np 
from PIL import Image
model = tf.keras.models.load_model("MirNet.h5")
def Mirnet(path , save=False) : 
    low_light_img = Image.open(path).convert('RGB')
    low_light_img = low_light_img.resize((256,256),Image.NEAREST)
    image = tf.keras.preprocessing.image.img_to_array(low_light_img)
    image = image.astype('float32') / 255.0
    image = np.expand_dims(image, axis = 0)
    output = model.predict(image)
    output_image = output[0] * 255.0
    output_image = output_image.clip(0,255)
    output_image = output_image.reshape((np.shape(output_image)[0],np.shape(output_image)[1],3))
    output_image = np.uint32(output_image)
    output_image=Image.fromarray(output_image.astype('uint8'),'RGB')
    if save : 
        name = path.split(".")[0]+ "_result.jpg"
        output_image.save(f"results/{name}")
    return output_image , low_light_img



