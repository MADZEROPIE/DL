import tensorflow as tf
import numpy as np

from tf_explain.core.grad_cam import GradCAM
from PIL import Image

from keras.preprocessing.image import load_img, img_to_array
from keras.applications.imagenet_utils import preprocess_input

# Load pretrained model or your own
model = tf.keras.applications.vgg16.VGG16(weights="imagenet", include_top=True)

examples = {281 : 'cat', 232 : 'dog', 7 : 'cock'} # https://gist.github.com/yrevar/942d3a0ac09ec9e5eb3a

for key, name in examples.items():
    
    # Load image
    img = load_img("images/input_nn/" + name + ".jpg", target_size=(224, 224))
    img = img_to_array(img)
    
    # check if predicted correctly
    image_batch = np.expand_dims(img, axis=0)
    
    predicted = model.predict(preprocess_input(image_batch.copy())).argmax()
    assert predicted == key, name + f" predicted incorrectly. Predicted: {predicted}. Expected: {key}"
    
    # Start explainer
    data = ([img], None)
    
    explainer = GradCAM()
    actual = explainer.explain(data, model, class_index=key)

    explainer.save(actual, '.', "src/" + name + ".png")

    expected = np.asarray(Image.open("images/output_nn/" + name + ".png"))

    assert np.array_equal(actual, expected), name + " is wrong"
    
    print(name + " is correct") 

print("Tests are passed!")
