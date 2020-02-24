from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

#Testing functions
print("\nMaking new matrix.")
print("\nm1 =")
m1 = new_matrix(4,4)
print_matrix(m1)
print("\nm2 =")
m2 = [[5,4,3,1],[1,3,4,1],[9,3,2,1],[1,1,1,1]]
print_matrix(m2)

print("\nTesting identity matrix. m1 = ")
ident(m1)
print_matrix(m1)

print("\nTesting matrix_mult(). m1 * m2 = ")
matrix_mult(m1, m2)
print_matrix(m2)

print("\nTesting add_edge(). Adding (1,2,3), (4,5,6), (7,8,9), (10,11,12) m3 = ")
m3 = []
add_edge(m3, 1, 2, 3, 4, 5, 6)
add_edge(m3, 7, 8, 9, 10, 11, 12)
print_matrix(m3)

print("\nTesting matrix_mult(). m2 * m3 = ")
matrix_mult(m2, m3)
print_matrix(m3)

#Making drawing
screen = new_screen()
matrix = []
matrix2 = []

add_edge(matrix, 175, 100, 0, 275, 100, 0)
add_edge(matrix, 150, 150, 0, 300, 150, 0)
add_edge(matrix, 150, 50, 0, 300, 50, 0)

add_edge(matrix, 150, 50, 0, 175, 100, 0)
add_edge(matrix, 175, 100, 0, 150, 150, 0)
add_edge(matrix, 300, 50, 0, 275, 100, 0)
add_edge(matrix, 275, 100, 0, 300, 150, 0)

add_edge(matrix, 175, 150, 0, 275, 150, 0)
add_edge(matrix, 150, 200, 0, 300, 200, 0)

add_edge(matrix, 175, 150, 0, 150, 200, 0)
add_edge(matrix, 275, 150, 0, 300, 200, 0)

add_edge(matrix, 175, 200, 0, 275, 200, 0)
add_edge(matrix, 150, 250, 0, 300, 250, 0)

add_edge(matrix, 175, 200, 0, 150, 250, 0)
add_edge(matrix, 275, 200, 0, 300, 250, 0)

add_edge(matrix, 175, 250, 0, 275, 250, 0)
add_edge(matrix, 150, 300, 0, 300, 300, 0)

add_edge(matrix, 175, 250, 0, 150, 300, 0)
add_edge(matrix, 275, 250, 0, 300, 300, 0)

add_edge(matrix, 175, 300, 0, 275, 300, 0)
add_edge(matrix, 150, 350, 0, 300, 350, 0)

add_edge(matrix, 175, 300, 0, 150, 350, 0)
add_edge(matrix, 275, 300, 0, 300, 350, 0)

add_edge(matrix, 215, 350, 0, 215, 400, 0)
add_edge(matrix, 235, 350, 0, 235, 400, 0)

add_edge(matrix, 215, 400, 0, 225, 410, 0)
add_edge(matrix, 235, 400, 0, 225, 410, 0)

draw_lines(matrix, screen, [0, 155, 255])

display(screen)
save_ppm(screen, 'binary.ppm')
save_ppm_ascii(screen, 'ascii.ppm')
save_extension(screen, 'img.png')
