from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import pandas as pd 
import os 
from pathlib  import Path



path = Path(os.path.dirname(__file__))
red_wine = pd.read_csv( str(path / Path ( "data/winequality-red.csv" )))
print(red_wine.head())


model = keras.Sequential([
    layers.Dense(units = 1,input_shape =(len(red_wine.columns)-1,))    
])


print(model.weights)

# print("Weights\n{}\n\nBias\n{}".format(w, b)))


