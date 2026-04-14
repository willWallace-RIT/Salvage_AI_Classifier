from model.infer import infer import numpy as np

if name == "main": print("Running Salvage AI Demo")

fake_image = np.random.randint(0, 255, (64, 64))

result = infer(fake_image)
print("Prediction:", result)
