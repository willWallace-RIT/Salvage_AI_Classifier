import numpy as np from vision.classifier import VisionPipeline

pipeline = VisionPipeline()

def infer(image_array): result = pipeline.run(image_array) return result

if name == "main": fake_image = np.random.randint(0, 255, (64, 64)) print(infer(fake_image))
