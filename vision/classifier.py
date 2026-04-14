from model.model import SalvageClassifier from vision.feature_extractor import extract_features

class VisionPipeline: def init(self): self.model = SalvageClassifier()

def run(self, image):
    features = extract_features(image)
    return self.model.predict(features)
