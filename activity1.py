#Creating the class
class Circle:
  #Putting a variable 'radius' in the class
  def __init__(self, radius):
    self.radius = radius
  #Making a function to calculate area
  def area(self):
    return 3.14 * self.radius * self.radius
  #making a function to calculate circumference
  def circumference(self):
    return 2 * 3.14 * self.radius
#Taking input from user for the value of the value of the radius
radius = int(input("Enter the radius of the circle (INTEGERS ONLY!!) : "))
#Asking user if they wanna find area or circumference
choice = input("Do you want to find the area or circumference of the circle? (Type 'area' or 'circumference' P.S. Pi is taken as 3.14 only) : ")
#Making an object for the class 
circle = Circle(radius)
#Using if and else to print the final statement
if choice == "area":
   print("The area of the circle is", circle.area())
elif choice == "circumference":
   print("The circumference of the circle is", circle.circumference())
   #If the user types something else other than area or circumference
else:
   print("Invalid choice. Please enter 'area' or 'circumference' , or check your spelling, or use lower case, not upper.")
