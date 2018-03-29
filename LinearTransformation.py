from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import thread
from copy import copy, deepcopy
from math import *
import re

window = 0
width, height = 500,500

print" ______   __  __     ______     ______     ______ "    
print"/\__  _\ /\ \/\ \   /\  == \   /\  ___\   /\  ___\ "   
print"\/_/\ \/ \ \ \_\ \  \ \  __<   \ \  __\   \ \___  \ " 
print"   \ \_\  \ \_____\  \ \_____\  \ \_____\  \/\_____\ "
print"    \/_/   \/_____/   \/_____/   \/_____/   \/_____/ "
print" ______     __         ______     ______     ______ "   
print"/\  __ \   /\ \       /\  ___\   /\  ___\   /\  __ \ "
print"\ \  __ \  \ \ \____  \ \ \__ \  \ \  __\   \ \ \/\ \ "   
print" \ \_\ \_\  \ \_____\  \ \_____\  \ \_____\  \ \_____\ "   
print"  \/_/\/_/   \/_____/   \/_____/   \/_____/   \/_____/ "   
print"----------------by NOIR DE BLACC team----------------"
print"-------------Rabbi Fijar Mayoza // 13516081----------"
print"---------------Hafizh Budiman // 13516137------------"
print"-----------------------------------------------------"
print"---SELAMAT DATANG DI PROGRAM TRANSLASI LINEAR KAMI---"
# Menerima masukan titik koordinat bidang dari user
sisi = input(">> Input jumlah sisi dari bidang = ")
matrix = []
for i in range (0,sisi):
    k=i+1
    kol = []
    x,y = input(">> titik x,y "+str(k)+" : ")
    kol.append(x/2.0)
    kol.append(y/2.0)
    matrix.append(kol)
vertexDim = 2
nVertices = sisi

matrix_reset = deepcopy(matrix)

#Fungsi-fungsi dan prosedur yang dipakai dalam OpenGL

def refresh2d(width,height):
    glViewport(0,0,width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-250, 250, -250, 250.0, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw_polygon():
    glBegin(GL_POLYGON)
    for i in range(0,sisi):
        glVertex2f(
            matrix[i][0],
            matrix[i][1]
            )
    glEnd()

def draw_axis():
    glLineWidth(2.5)
    glBegin(GL_LINES)
    glVertex2f(-250.0, 0)
    glVertex2f(250.0, 0.0)
    glEnd()
    glLineWidth(2.5)
    glBegin(GL_LINES)
    glVertex2f(0.0, -250.0)
    glVertex2f(0.0, 250.0)
    glEnd()
    glLineWidth(0.001)
    glBegin(GL_LINES)
    for i in range (0,11):
        glVertex2f( -250.0 + i*50, -250 )
        glVertex2f( -250.0 + i*50, 250 )
    glEnd()
    glLineWidth(0.001)
    glBegin(GL_LINES)
    for i in range (0,11):
        glVertex2f( -250, -250.0 + i*50 )
        glVertex2f( 250, -250.0 + i*50 )
    glEnd()

def drawinput():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    refresh2d(width,height)

    glColor3f(1,1,1)
    draw_polygon()
    
    glColor3f(1,1,1)
    draw_axis()

    glutSwapBuffers()

# Menerima jenis pilihan eksekusi terhadap bidang

def menu_input():
    print ">> Menu = "
    print ">> -  translate <dx> <dy>"
    print ">>    Melakukan translasi objek dengan menggeser sejauh dx dan dy"
    print ">> -  dilate <k>"
    print ">>    Melakukan dilatasi objek dengan faktor skala k"
    print ">> -  rotate <deg> <a> <b>"
    print ">>    Melakukan rotasi objek berlawanan arah jarum jam sebesar <deg>"
    print ">>    derajat terhadap titik <a>,<b>"
    print ">> -  reflect <param>"
    print ">>    Melakukan pencerminan objek terhadap <param>, <param> dapat berupa:"
    print ">>    x, y, y=x, y=-x, atau suatu titik (a,b)"
    print ">> -  shear <param> <k>"
    print ">>    Melakukan operasi shear pada objek. Nilai <param> berupa"
    print ">>    sumbu x atau y, dan k adalah faktor shear."
    print ">> -  stretch <param> <k>"
    print ">>    Melakukan operasi stretch pada objek. Nilai <param> berupa"
    print ">>    sumbu x atau y, dan k adalah faktor stretch."
    print ">> -  custom <a> <b> <c> <d>"
    print ">>    Melakukan transformasi linier dengan objek matriks sebagai berikut : "
    print ">>     _    _"
    print ">>    | a  b |"
    print ">>    |_c  d_|"
    print ">> -  multiple <n>"
    print ">>    Melakukan transformasi linier pada objek sebanyak n kali berurutan"
    print ">> -  reset"
    print ">>    Mengembalikan objek pada kondisi awal objek didefinisikan"
    print ">> -  exit"
    print ">>    Keluar dari program"
    print"----------------------------------------------------------------------------"
    while True:
        string = raw_input(">> Pilihan = ")
        menu = []
        menu = string.split(" ")
        if (menu[0] == 'translate'):
            x,y = float(menu[1]),float(menu[2])
            translate(x,y)
        elif (menu[0] == 'dilate'):
            k = float(menu[1])
            dilate(k)
        elif (menu[0] == 'rotate'):
            deg,a,b = float(menu[1]),float(menu[2]),float(menu[3])
            rotate(deg,a,b)
        elif (menu[0] == 'reflect'):
            reflect(menu[1])
        elif (menu[0] == 'shear'):
            sumbu,x = menu[1],float(menu[2])
            shear(sumbu,x)
        elif (menu[0] == 'stretch'):
            sumbu,x = menu[1],float(menu[2])
            stretch(sumbu,x)
        elif (menu[0] == 'custom'):
            a,b,c,d = float(menu[1]),float(menu[2]),float(menu[3]),float(menu[4])
            custom(a,b,c,d)
        elif (menu[0] == 'reset'):
            reset()
        elif (menu[0] == 'multiple'):
            multiple(int(menu[1]))
        elif (menu[0] == 'exit'):
            close()
        else:
            print ">> Masukkan tidak ada dalam menu,"
            print ">> input kembali operasi translasi yang diinginkan"

''' Melakukan translasi objek dengan menggeser nilai x sebesar dx dan menggeser nilai y sebesar dy. '''    
def translate(dx,dy):
    a = dx/20000.0
    b = dy/20000.0
    a1 , b1 = 0.0 , 0.0
    while a1<=abs(dx/2.0) and b1<=abs(dy/2.0):
        for i in range(0, sisi):
            matrix[i][0] += a
            matrix[i][1] += b 
        a1 = abs(a)+a1
        b1 = abs(b)+b1

'''Melakukan dilatasi objek dengan faktor scaling k.'''
def dilate(k):
    target = deepcopy(matrix)
    for i in range(0, sisi):
        target[i][0] = matrix[i][0]*k
        target[i][1] = matrix[i][1]*k

    for i in range(0, sisi):
        c = sisi*20000
        d = sisi*20000
        cc = 0
        dd = 0
        while (cc<=c and dd<=d):
            for i in range(0, sisi):
                matrix[i][0] += (target[i][0]-matrix[i][0])/20000.0
                matrix[i][1] += (target[i][1]-matrix[i][1])/20000.0
            cc += 1
            dd += 1

'''Melakukan operasi shear pada objek. Nilai param dapat berupa x
(terhadap sumbu x) atau y (terhadap sumbu y). Nilai k adalah faktor
shear.'''
def shear(sumbu,x):
    if sumbu == 'x':
        target = deepcopy(matrix)
        for i in range(0, sisi):
            target[i][0] = target[i][0] + (x*target[i][1])
    elif sumbu == 'y':
        target = deepcopy(matrix)
        for i in range(0, sisi):
            target[i][1] = target[i][1] + (x*target[i][0])

    for i in range(0,sisi):
        c = sisi*20000
        d = sisi*20000
        cc = 0
        dd = 0
        while(cc<=c and dd<=d):
            for i in range(0,sisi): 
                matrix[i][0] += (target[i][0]-matrix[i][0])/20000.0
                matrix[i][1] += (target[i][1]-matrix[i][1])/20000.0
            cc += 1
            dd += 1

'''Melakukan operasi stretch pada objek. Nilai param dapat berupa x
(terhadap sumbu x) atau y (terhadap sumbu y). Nilai k adalah faktor
stretch.'''        
def stretch(sumbu,x):
    target = deepcopy(matrix)
    if sumbu == 'x':
        for i in range(0, sisi):
            target[i][0] = target[i][0]*x
    elif sumbu == 'y':
        for i in range(0, sisi):
            target[i][1] = target[i][1]*x
    for i in range(0,sisi):
        c = sisi*20000
        d = sisi*20000
        cc = 0
        dd = 0
        while(cc<=c and dd<=d):
            for i in range(0,sisi): 
                matrix[i][0] += (target[i][0]-matrix[i][0])/20000.0
                matrix[i][1] += (target[i][1]-matrix[i][1])/20000.0
            cc += 1
            dd += 1

'''Melakukan rotasi objek secara berlawanan arah jarum jam sebesar deg
derajat terhadap titik a,b'''
def rotate(deg,a,b):
    degr = radians(deg)
    k = 0
    d = degr/50000.0
    for i in range(0, sisi):
        while abs(degr)>=k :
            for i in range(0,sisi):
                matrix[i][0] = ((matrix[i][0]-a/2)*cos(d)) - ((matrix[i][1]-b/2)*sin(d)) + a/2
                matrix[i][1] = ((matrix[i][0]-a/2)*sin(d)) + ((matrix[i][1]-b/2)*cos(d)) + b/2   
            k += abs(degr)/50000.0

'''Melakukan transformasi linier pada objek dengan matriks transformasi dengan elemen [a b][c d]'''    
def custom(a,b,c,d):
    target = deepcopy(matrix)
    for i in range(0, sisi):
        target[i][0] = matrix[i][0]*a + matrix[i][1]*b
        target[i][1] = matrix[i][0]*c + matrix[i][1]*d

    for i in range(0,sisi):
        c = sisi*20000
        d = sisi*20000
        cc = 0
        dd = 0
        while(cc<=c and dd<=d):
            for i in range(0,sisi): 
                matrix[i][0] += (target[i][0]-matrix[i][0])/20000.0
                matrix[i][1] += (target[i][1]-matrix[i][1])/20000.0
            cc += 1
            dd += 1

'''Mengembalikan objek pada kondisi awal objek didefinisikan.'''
def reset():
    target = deepcopy(matrix_reset)
    for i in range(0, sisi):
        matrix[i][0] = target[i][0]
        matrix[i][1] = target[i][1]
    for i in range(0,sisi):
        c = sisi*20000
        d = sisi*20000
        cc = 0
        dd = 0
        while(cc<=c and dd<=d):
            for i in range(0,sisi): 
                matrix[i][0] += (target[i][0]-matrix[i][0])/20000.0
                matrix[i][1] += (target[i][1]-matrix[i][1])/20000.0
            cc += 1
            dd += 1

'''Melakukan pencerminan objek. Nilai param adalah salah satu dari nilainilai
berikut: x, y, y=x, y=-x, atau (a,b). Nilai (a,b) adalah titik untuk
melakukan pencerminan terhadap.'''
def reflect(x):
    target = deepcopy(matrix)
    param = re.split(r'[,\s()]+', x)
    if param[0] == 'y=x':
        for i in range(0, sisi):
            target[i][0] = matrix[i][1]
            target[i][1] = matrix[i][0]
    elif param[0] == 'y=-x':
        for i in range(0, sisi):
            target[i][0] = matrix[i][1]*(-1.0)
            target[i][1] = matrix[i][0]*(-1.0)
    elif param[0] == 'y':
        for i in range(0, sisi):
            target[i][0] = matrix[i][0]*(-1.0)
    elif param[0]=='x':
        for i in range(0, sisi):
            target[i][1] = matrix[i][1]*(-1.0) 
    else:
        for i in range(0, sisi):
            target[i][0] = -1*target[i][0] + float(param[1])
            target[i][1] = -1*target[i][1] + float(param[2])

    for i in range(0,sisi):
        c = sisi*20000
        d = sisi*20000
        cc = 0
        dd = 0
        while(cc<=c and dd<=d):
            for i in range(0,sisi): 
                matrix[i][0] += (target[i][0]-matrix[i][0])/20000.0
                matrix[i][1] += (target[i][1]-matrix[i][1])/20000.0
            cc += 1
            dd += 1

'''Melakukan transformasi linier pada objek sebanyak n kali berurutan.
Setiap baris input 1..n dapat berupa translate, rotate, shear, dll tetapi
bukan multiple, reset, exit.'''
def multiple(n):
    Operasi = []
    for i in range(n):
        string = raw_input(">> Operasi %d = " %(i+1))
        Operasi.append(string)
    
    for string in Operasi:
        pilih = []
        pilih = string.split(" ") 
        if (pilih[0] == 'translate'):
            x,y = float(pilih[1]),float(pilih[2])
            translate(x,y)
        elif (pilih[0] == 'dilate'):
            k = float(pilih[1])
            dilate(k)
        elif (pilih[0] == 'rotate'):
            deg,a,b = float(pilih[1]),float(pilih[2]),float(pilih[3])
            rotate(deg,a,b)
        elif (pilih[0] == 'reflect'):
            reflect(pilih[1])
        elif (pilih[0] == 'shear'):
            sumbu,x = pilih[1],float(pilih[2])
            shear(sumbu,x)
        elif (pilih[0] == 'stretch'):
            sumbu,x = pilih[1],float(pilih[2])
            stretch(sumbu,x)
        elif (pilih[0] == 'custom'):
            a,b,c,d = float(pilih[1]),float(pilih[2]),float(pilih[3]),float(pilih[4])
            custom(a,b,c,d)
        else:
            print (">> Maaf, operasi ' %s ' ilegal dalam operasi multiple," %(pilih[0]))
            print (">> Operasi ilegal tidak dapat dieksekusi")

'''Keluar dari program'''
def close():
    print ">> Terima kasih telah menggunakan program kami."
    glutDestroyWindow(glutGetWindow())
    exit(0)

# OpenGL Window Program
def main():
    thread.start_new_thread(menu_input,())
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)    
    window = glutCreateWindow("Simulasi Transformasi Linear by NOIR DE BLACC")

    glutDisplayFunc(drawinput)
    glutIdleFunc(drawinput)

    glutMainLoop()

main()
