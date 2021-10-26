#Build an application with below functions: Register a new student. When the student check in the library: verify the student’s information: if student registered, they were come in the library else they were denied.
import os
import numpy as np
import cv2
from PIL import Image

# get the current directory
currentDirectory = os.getcwd() + "/Image"


class Student:
    def __init__(self, fullName, idStudent, idClass, dateOfBirth, Picture):
        self.fullName = fullName
        self.idStudent = idStudent
        self.idClass = idClass
        self.dateOfBirth = dateOfBirth
        self.Picture = Picture



# Using PCA to reduce the dimension of the image and store it in the database to recognize the student

class PCA:

    def __init__(self, image):
        self.image = image

    def reduceDimension(self):
        # get the current directory
        currentDirectory = os.getcwd() + "/Image"
        # read the image
        image = cv2.imread(currentDirectory + "/" + self.image)
        # convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # get the image size
        height, width = gray.shape
        # reshape the image to a vector
        imageVector = gray.reshape(height * width, 1)
        # calculate the mean of the image
        mean = np.mean(imageVector, axis=0)
        # calculate the covariance of the image
        covariance = np.cov(imageVector.T)
        # calculate the eigen values and eigen vectors of the covariance matrix
        eigenValues, eigenVectors = np.linalg.eig(covariance)
        # sort the eigen values and eigen vectors in descending order
        idx = eigenValues.argsort()[::-1]
        eigenValues = eigenValues[idx]
        eigenVectors = eigenVectors[:, idx]
        # get the first two eigen vectors
        eigenVectors = eigenVectors[:, :2]
        # calculate the projection of the image
        projection = np.dot(imageVector - mean, eigenVectors)
        # reshape the projection to the image size
        projection = projection.reshape(height, width, 2)
        # return the projection
        return projection


class Library:

    def __init__(self):
        self.listStudent = []

    def checkIn(self, idStudent):
        pass




    def registerStudent(self, student):
        self.listStudent.append(student)

class Demo:

   def main(self):

       while (True):
           print("1. Register a new student")
           print("2. CheckIn")
           print("3. Exit")

           choice = int(input("Enter your choice [1-2-3]: "))

           if choice == 1:
               #input information of student through console
               fullName = input("Enter full name: ")
               dateOfBirth = input("Enter date of birth: ")
               idClass = input("Enter id class: ")
               idStudent = input("Enter id student: ")

               # take a picture of the student using pillow

               picture = Image.open(currentDirectory + "/" + "student.jpg")
               picture.show()

           if choice == 2:
               pass
           if choice == 3:
                break



Demo.main(self=Demo())







