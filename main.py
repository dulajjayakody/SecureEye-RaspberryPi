import pygame

def play_alarm(duration):
    pygame.mixer.init()
    
    alarm_sound = pygame.mixer.Sound("media/audio.wav")
    
    alarm_sound.play()
    
    time.sleep(duration)
    
    alarm_sound.stop()


while True:
    cap = cv2.VideoCapture(0)    
    ret, frame = cap.read()
    cap.release()
    cv2.destroyAllWindows()
    
cap.release()
cv2.destroyAllWindows()
