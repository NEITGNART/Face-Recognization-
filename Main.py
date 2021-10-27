# Build an application with below functions: Register a new student. When the student check in the library: verify the student’s information: if student registered, they were come in the library else they were denied.
import os
import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

# get the current directory

current_dir = os.getcwd()


class Library:

    def __init__(self):
        self.listStudent = []

    def checkIn(self, idStudent):
        pass

    def registerStudent(self, student):
        self.listStudent.append(student)


class Student:
    def __init__(self, fullName, idStudent, idClass, dateOfBirth, Picture):
        self.fullName = fullName
        self.idStudent = idStudent
        self.idClass = idClass
        self.dateOfBirth = dateOfBirth
        self.Picture = Picture


class StudentList:
    def __init__(self):
        self.listStudent = []

    def addStudent(self, student):
        self.listStudent.append(student)

    def getListStudent(self):
        return self.listStudent

    def countNumberOfStudent(self):
        return len(self.listStudent)

    def printListStudent(self):
        for student in self.listStudent:
            print(student.idStudent)


def readDirectory(directory):
    face_addr = []
    for filename in os.listdir(directory + '/' + "ImageStudent"):
        face_addr.append(directory + "/" + "ImageStudent/" + filename)
    return face_addr


def labelImage(directory):
    images = []
    labels = []

    linkFile = readDirectory(directory)

    for (i, imagePath) in enumerate(linkFile):
        image = cv2.imread(imagePath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        images.append(image)
        labels.append(i)

    return images, labels


linkTest = current_dir + '/' + "Test1.png"

def PCA(linkTest):


    images, labels = labelImage(current_dir)
    image_data = []

    for image in images:
        data = image.flatten()
        image_data.append(data)

    image_data = np.array(image_data).reshape((-1, len(image_data[0])))
    print (image_data.shape)

    # mean image
    mean_image = np.mean(image_data, axis=0)
    print (mean_image.shape)

    # sub tract mean image from image data
    image_data = image_data - mean_image

    # use SVD to get eigen vectors and eigen values

    U, S, V = np.linalg.svd(image_data)

    # Find the eigenfaces and set the threshold
    if (len (S) >= 2):
        eigen_faces = []
        for i in range(len(S)):
            if (S[i] > 0.1):
                eigen_faces.append(V[i])

    # Convert eigen_faces to numpy array
    eigen_faces = np.array(eigen_faces)
    print (eigen_faces.shape)
    # eigen_faces = eigen_faces.reshape((-1, len(eigen_faces[0])))

    def findNearestImage(eigen_faces):

        # Read the image
        image = np.array(Image.open(linkTest))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (100, 100))
        # Reshape the image
        gray = gray.reshape((1, 100 * 100))
        # Subtract mean image from image
        gray = gray - mean_image
        # Using euclid distance to find the nearest image
        distance = np.linalg.norm(eigen_faces - gray, axis=1)
        min_index = np.argmin(distance)
        # print min distance
        print("Distance from dataset: " + str(distance[min_index]))
        return distance[min_index]


    return findNearestImage(eigen_faces)



    # Test the nearest image
    # test_image = cv2.imread(current_dir + "/" + "ImageStudent/1.jpg")
    # test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)











class MainWindow(tk.Frame):


    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text="Quit", command=self.quit)
        self.quitButton.pack(side="bottom")

    def UI(self):
        ImageDirectory = os.getcwd() + "/ImageTkinter"
        ImageStudent = os.getcwd() + "/ImageStudent"

        # Write a programing using Tkiner to create a GUI application for the library management system.
        # The application should have the following features:
        # 1. Register a new student.
        # 2. When the student check in the library: verify the student’s information: if student registered, they were come in the library else they were denied.

        # create a GUI application using Tkiner
        root = tk.Tk()
        root.title("Library Management System")
        root.geometry("500x500")
        root.resizable(0, 0)

        # set up the background image
        imageBackground = tk.PhotoImage(file=ImageDirectory + "/background.png")
        # set background image using imageBackground
        labelBackground = tk.Label(root, image=imageBackground)
        labelBackground.place(x=0, y=0, relwidth=1, relheight=1)

        root.wm_attributes("-topmost", 1)
        root.focus_force()
        root.bind("<Escape>", lambda e: root.destroy())

        # create a button to register a new student
        root.register = tk.Button(root, text="Register", bg='#50c4ee', fg='#5ae3ce', font=('Arial', 12, 'bold'))
        root.register.place(x=100, y=100, width=100, height=50)
        # create a button to check in a student
        root.checkIn = tk.Button(root, text="Check In", bg='#50c4ee', fg='#5ae3ce', font=('Arial', 12, 'bold'))
        root.checkIn.place(x=300, y=100, width=100, height=50)

        # create a label to show the message
        root.message = tk.Label(root, text="Welcome to Library", bg='#50c4ee', fg='#ffffff', font=('Arial', 12, 'bold'))
        root.message.place(x=100, y=200, width=300, height=50)


        # create another page to register a new student when the register button is clicked

        def createRegisterWindow(nameTitle):

            window = tk.Toplevel(root)
            window.title(nameTitle)
            window.geometry("600x600")

            # set window to the top of all windows
            window.wm_attributes("-topmost", 1)
            window.resizable(0, 0)
            window.focus_force()
            # get background
            window.imageBackground = tk.PhotoImage(file=ImageDirectory + "/background.png")
            window.labelBackground = tk.Label(window, image=window.imageBackground)
            window.labelBackground.place(x=0, y=0, relwidth=1, relheight=1)

            # set up the background image

            # Take a input name of the student

            window.name = tk.Label(window, text="Name:", bg='#50c4ee', fg='#ffffff', font=('Arial', 12, 'bold'))
            window.name.place(x=100, y=100, width=100, height=50)
            window.nameEntry = tk.Entry(window, bg='#ffffff', fg='#000000', font=('Arial', 12, 'bold'))
            window.nameEntry.place(x=200, y=100, width=200, height=50)
            window.nameEntry.focus_force()

            # get value name of the student


            # self.idStudent = idStudent
            # self.idClass = idClass
            # self.dateOfBirth = dateOfBirth
            # self.Picture = Picture

            # take a input idStudent of the student

            window.idStudent = tk.Label(window, text="ID Student:", bg='#50c4ee', fg='#ffffff',
                                        font=('Arial', 12, 'bold'))
            window.idStudent.place(x=100, y=200, width=100, height=50)
            window.idStudentEntry = tk.Entry(window, bg='#ffffff', fg='#000000', font=('Arial', 12, 'bold'))
            window.idStudentEntry.place(x=200, y=200, width=200, height=50)
            window.idStudentEntry.focus_force()

            # Take a input idClass of the student

            window.idClass = tk.Label(window, text="ID Class:", bg='#50c4ee', fg='#ffffff', font=('Arial', 12, 'bold'))
            window.idClass.place(x=100, y=300, width=100, height=50)
            window.idClassEntry = tk.Entry(window, bg='#ffffff', fg='#000000', font=('Arial', 12, 'bold'))
            window.idClassEntry.place(x=200, y=300, width=200, height=50)
            window.idClassEntry.focus_force()

            # take a input dateOfBirth of the student

            window.dateOfBirth = tk.Label(window, text="Date of Birth:", bg='#50c4ee', fg='#ffffff',
                                          font=('Arial', 12, 'bold'))
            window.dateOfBirth.place(x=100, y=400, width=100, height=50)
            window.dateOfBirthEntry = tk.Entry(window, bg='#ffffff', fg='#000000', font=('Arial', 12, 'bold'))
            window.dateOfBirthEntry.place(x=200, y=400, width=200, height=50)
            window.dateOfBirthEntry.focus_force()

            # add a button to take a picture of the student

            window.takePicture = tk.Button(window, text="Take Picture", bg='#50c4ee', fg='#5ae3ce',
                                           font=('Arial', 12, 'bold'))
            window.takePicture.place(x=100, y=500, width=100, height=50)



            #When click a button take a picture of the student then open a file dialog to choose a picture
            #and save it to the directory of the project

            def takePicture(window):
                nameFile = filedialog.askopenfilename(initialdir = ImageDirectory, title = "Select file", filetypes = (("png files","*.png"),("all files","*.*")))
                window.imageStudent = nameFile

            window.takePicture.bind("<Button-1>", lambda event: takePicture(window))

            # save information from the window to the file of the student

            window.save = tk.Button(window, text="Save", bg='#50c4ee', fg='#5ae3ce', font=('Arial', 12, 'bold'))
            window.save.place(x=300, y=500, width=100, height=50)

            # Take a button for quit the window

            window.quit = tk.Button(window, text="Quit", bg='#50c4ee', fg='#5ae3ce', font=('Arial', 12, 'bold'))
            window.quit.place(x=500, y=500, width=100, height=50)
            window.quit.bind("<Button-1>", lambda event: window.destroy())


            # after click a button save information and return information to the main window

            def save(window):
                name = window.nameEntry.get()
                idStudent = window.idStudentEntry.get()
                idClass = window.idClassEntry.get()
                dateOfBirth = window.dateOfBirthEntry.get()

                fileName = window.imageStudent

                # take a picture from fileName

                image = np.array(Image.open(fileName))
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                gray = cv2.resize(gray, (100, 100))

                # save picture to the directory of the project
                cv2.imwrite(ImageStudent + "/" + idStudent + ".png", gray)
                # student = Student(name, idStudent, idClass, dateOfBirth, Picture)
                # studentList.addStudent(student)
                window.destroy()


            window.save.bind("<Button-1>", lambda event: save(window))

        # create a checkIn window
        def createCheckInWindow(root):
            # create a window for checkIn
            window = tk.Toplevel(root)
            window.title("CheckIn")
            window.geometry("500x500")
            window.configure(bg='#50c4ee')
            window.resizable(0, 0)
            # set background image for window
            window.image = Image.open(ImageDirectory + "/background.png")
            window.image = window.image.resize((500, 500), Image.ANTIALIAS)
            window.background_image = ImageTk.PhotoImage(window.image)
            window.background_label = tk.Label(window, image=window.background_image)
            window.background_label.place(x=0, y=0, relwidth=1, relheight=1)
            window.background_label.image = window.background_image
            window.background_label.pack()
            # Take the window on the center of the screen
            window.update_idletasks()
            window.wm_attributes("-topmost", 1)
            window.focus_force()


            # Create a button with content "Click to open camera"

            window.openCamera = tk.Button(window, text="Click to open camera", bg='#50c4ee', fg='#5ae3ce', font=('Arial', 12, 'bold'))
            window.openCamera.place(x=100, y=100, width=300, height=50)

            # Create a button to quit the window

            # Create a label for notice with content "Please click a button to open camera and Press S to take a picture"

            window.notice = tk.Label(window, text="Please click a button to open camera and Press S to take a picture", bg='#fdfc2d', fg='#5ae3ce', font=('Arial', 15, 'bold'))
            window.notice.place(x = 0, y=200, width=500, height=50)



            # Create a button to quit the window
            window.quit = tk.Button(window, text="Quit", bg='#50c4ee', fg='#5ae3ce', font=('Arial', 12, 'bold'))
            window.quit.place(x=100, y=400, width=300, height=50)
            window.quit.bind("<Button-1>", lambda event: window.destroy())



            # open camera using opencv
            def openCamera(window):
                cap = cv2.VideoCapture(0)


                while True:
                    # Move frame opencv to the right of window
                    ret, frame = cap.read()

                    ret, frame = cap.read()
                    cv2.imshow('frame', frame)
                    # Take a picture when click a button
                    # save the picture to the directory of the project
                    # if the user press 'q' then break the frame loop
                    if cv2.waitKey(2) & 0xFF == ord('s'):
                        cv2.imwrite(current_dir + "/" + "test.png", frame)
                        break
                cap.release()
                cv2.destroyAllWindows()

                distance  = PCA(current_dir + "/" + "test.png")
                if distance < 6300:

                    # Create a label for notice with content "You can go to the library"
                    window.notice = tk.Label(window, text="Check-in successfully", bg='#fdfc2d', fg='#5ae3ce', font=('Arial', 15, 'bold'))
                    window.notice.place(x = 0, y=200, width=500, height=50)
                else:
                    # Create a label for notice with content "You can not go to the library"

                    window.notice = tk.Label(window, text="Check-in failed", bg='#fdfc2d', fg='#5ae3ce', font=('Arial', 15, 'bold'))
                    window.notice.place(x = 0, y=200, width=500, height=50)




            window.openCamera.bind("<Button-1>", lambda event: openCamera(window))

        root.register.bind("<Button-1>", lambda event: createRegisterWindow(root))
        root.checkIn.bind("<Button-1>", lambda event: createCheckInWindow(root))
        # create another page for CheckIn

        root.mainloop()


class Demo:
    Library = Library()
    studentList = StudentList()
    def main(self):
        MainWindow.UI(self)


Demo.main(self=Demo())