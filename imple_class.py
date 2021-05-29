from tensorflow.keras.models import model_from_json
import numpy as np

class AnimalRecogonizer(object):

    ANIMAL_LIST = ['Elephant','Wild_boar']
    def __init__(self,model_json_file,model_weights_file):
        with open(model_json_file,"r") as json_file:
            loaded_json_model = json_file.read()
            self.loaded_model = model_from_json(loaded_json_model)

            self.loaded_model.load_weights(model_weights_file)
            self.loaded_model.make_predict_function()

    def predict(self,img):
        self.pre = self.loaded_model.predict(img)
        return AnimalRecogonizer.ANIMAL_LIST[np.argmax(self.pre)]