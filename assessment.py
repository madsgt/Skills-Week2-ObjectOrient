"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

Ans: 1) Encapsulation- Keeping data and its functionality close together
2) Abstraction- Hiding details we dont need, eg details internal to a method
3)	Polymorphism- Interchangeability of components without conditionals


2. What is a class?

Ans: Class is like a smarter dictionary, it is an essential part of object 
oriented programming
It stores data,is structured and has own smarts. CLass is a construct in python,
its a way to take data and grouping of its functions and place them in a box, we
can access them with the .(dot) operator


3. What is an instance attribute?
Ans: AN instance attribute is created within the method (eg self.name). We can
set attributes to the instance

4. What is a method?
A method is the functionality defined on its class.Methods always pass one 
paramter -self. The self parameter is an instance itself. we can all on methods
object.methods(arguments). THey can also refer to attributes. It has a list of
parameters. When we call method we pass instance as self

5. What is an instance in object orientation?
Ans: Instance is created on a class(a string or file)
Each instance of a class is different and has its own data. instances support 
atrribute references and instantiation
When we make an instance it is created by Python and then initialised
 (perhaps by our code)
WE can have more than one instance of a class. To make an instance 
we would call the class
eg: >>>fido = Animal() FIdo is the instance of the class Animal
We also tend to call the term- instance and object interchangeably

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

Ans: The class attribute is built on the class itself, when asked for it in an 
instance if refers to the class to find it . An instance attribute is set on the
instance/object.WE can replace class attributes with Instance attributes.

During factoring we may realise setting class attributes in some cases is more
useful by setting default/constant values in the class rather than keep passing
in many sub -classes if there is multiple inheritances. 

eg- class Circle(object): # If we are to find area of a circle 
	pi = 3.1416 # setting the class attribute pi helps in subsequent set up

		def__init__(self, radius):
			self.radius = radius # this is an instance attribute

		def area(self):
			return pi * (self.radius**2)

"""


# Parts 2 through 5:
# Create your classes and class methods
class Student(object):

	def __init__(self,first_name,last_name,address):
		self.first_name = first_name
		self.last_name = last_name
		self.address = address
	
		
	def student_display_info(self):
		print " Student {} {} lives at {}".format(self.first_name, 
												self.last_name,
												self.address)

	# The __init__method initialises and stores and the 
	#display method displays the data (applicable for part 2 too)


class Question(object):

	def __init__(self, question, answer):
		self.question = question
		self.answer = answer

	def display_question_answer(self):
		print " Question: {}, correct_answer : {} ".format(self.question, 
			                                               self.answer)
		

class Exam(Question):

	def __init__(self, name, questions):
		super(Exam, self).__init__(question, answer)
		self.questions = []
		self.name = Examname

	def Add_questions(self):
		for question, answer in object: #code incomplete