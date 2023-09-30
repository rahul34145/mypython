#include<GL/glut.h> 
#include<stdio.h> 
int x1, y1, x2, y2; 
void draw_pixel(int x, int y) 
{ 
glColor3f(1.0,0.0,0.0); 
glBegin(GL_POINTS); 
glVertex2i(x, y); 
glEnd(); 
} 