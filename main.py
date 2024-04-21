import cv2
import time
import pygame
from skimage.transform import resize
from skimage import io, color
import joblib

def play_alarm(duration):
    pygame.mixer.init()
    
    alarm_sound = pygame.mixer.Sound("media/audio.wav")
    
    alarm_sound.play()
    
    time.sleep(duration)
    
    alarm_sound.stop()
    
def preprocess_test_image(image, target_size=(100, 100)):
    # Resize the image to the target size
    resized_image = resize(image, target_size, anti_aliasing=True)
    # Convert the resized image to grayscale
    image_gray = color.rgb2gray(resized_image)
    return image_gray

def make_prediction(clf, image):
    # Load and preprocess the test image
    preprocessed_image = preprocess_test_image(image)
    # Flatten the preprocessed image
    features = preprocessed_image.reshape(1, -1)
    # Make prediction using the trained classifier
    prediction = clf.predict(features)
    return prediction[0]

model_file = "model/trained_model.pkl"
clf = joblib.load(model_file)

while True:
    
    cap = cv2.VideoCapture(0)    
    ret, frame = cap.read()
    prediction = make_prediction(clf, frame)
    if prediction == 0:
        print("NonViolence")
        continue
    else:
        print("Violence")
        play_alarm(100)
        break
    
    cap.release()
    cv2.destroyAllWindows()
    
cap.release()
cv2.destroyAllWindows()
    
