import numpy as np

def extract_features(image_array):
""" Fake feature extractor placeholder. Replace with CNN / ViT embeddings. """
return [ np.mean(image_array), np.std(image_array), np.max(image_array) / 255.0 ]
