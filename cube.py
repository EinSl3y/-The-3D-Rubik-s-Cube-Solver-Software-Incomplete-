from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Rubik3D:
    def __init__(self):
        self.cube_colors = [
            (1, 1, 1),  # Màu trắng
            (1, 1, 0),  # Màu vàng
            (1, 0, 0),  # Màu đỏ
            (0, 1, 0),  # Màu xanh lá cây
            (0, 0, 1),  # Màu xanh dương
            (1, 0.5, 0)  # Màu cam
        ]

    def draw_cube(self, x, y, z, colors):
        # Mô tả các mặt của hình lập phương
        cube_faces = [
            [(0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)],  # Mặt trên
            [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)],  # Mặt dưới
            [(0, 1, 0), (1, 1, 0), (1, 1, 1), (0, 1, 1)],  # Mặt trước
            [(0, 0, 0), (1, 0, 0), (1, 0, 1), (0, 0, 1)],  # Mặt sau
            [(1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 0, 1)],  # Mặt phải
            [(0, 0, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1)]   # Mặt trái
        ]

        # Vẽ các mặt chính của ô với màu sắc
        glBegin(GL_QUADS)
        for i, color in enumerate(colors):
            glColor3f(*color)  # Thiết lập màu
            for vertex in cube_faces[i]:
                glVertex3f(vertex[0] + x, vertex[1] + y, vertex[2] + z)
        glEnd()

        # Vẽ viền trắng cho mỗi mặt
        glColor3f(1, 1, 1)  # Màu trắng
        glLineWidth(2)      # Độ dày của viền
        glBegin(GL_LINES)
        for face in cube_faces:
            for i in range(len(face)):
                start = face[i]
                end = face[(i + 1) % len(face)]  # Điểm tiếp theo
                glVertex3f(start[0] + x, start[1] + y, start[2] + z)
                glVertex3f(end[0] + x, end[1] + y, end[2] + z)
        glEnd()

    def draw(self):
        glEnable(GL_CULL_FACE)  # Bật culling để ẩn mặt không nhìn thấy
        glCullFace(GL_BACK)    # Loại bỏ mặt sau
        glEnable(GL_DEPTH_TEST)  # Kiểm tra chiều sâu

        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    self.draw_cube(x, y, z, self.cube_colors)
