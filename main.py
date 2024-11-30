import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from cube import Rubik3D
from hand_control import detect_gesture
import cv2
import mediapipe as mp

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
pygame.display.set_caption("3D Rubik Controlled by Hand Gestures")
gluPerspective(45, (WIDTH / HEIGHT), 0.1, 50.0)
glTranslatef(0.0, 0.0, -8)
rubik = Rubik3D()
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access the webcam")
    exit()
# Mediapipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
clock = pygame.time.Clock()
running = True
rubik_rotation = [0, 0, 0]
def draw_camera_texture(frame):
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    frame_data = cv2.flip(frame, 0)
    frame_data = cv2.cvtColor(frame_data, cv2.COLOR_BGR2RGB)
    frame_data = frame_data.astype('uint8')
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, frame.shape[1], frame.shape[0], 0, GL_RGB, GL_UNSIGNED_BYTE, frame_data)
    glDeleteTextures(1, int(texture_id))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                rubik.rotate_face('U')
            elif event.key == pygame.K_d:
                rubik.rotate_face('D')
            elif event.key == pygame.K_r:
                rubik.rotate_face('R')
            elif event.key == pygame.K_l:
                rubik.rotate_face('L')
            elif event.key == pygame.K_f:
                rubik.rotate_face('F')
            elif event.key == pygame.K_b:
                rubik.rotate_face('B')

    # Xóa màn hình và vẽ lại
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    rubik.draw()
    pygame.display.flip()
    clock.tick(30)
cap.release()
pygame.quit()
