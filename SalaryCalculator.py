"""
Program: SalaryCalculator.py

"""

from breezypythongui import EasyFrame
from tkinter.font import Font

# Other imports go here.

# Class header (class name will change from project to project.)
class SalaryCalculator(EasyFrame):
	#Definition of our classes' constructor method
	def __init__(self):
		# Call to the EasyFrame class constructor.
		EasyFrame.__init__(self, title = "Salary Calculator", background =  "lightgreen", width = 400, height = 500)
		# Create a variable from the Font class.
		myFont = Font(family = "Verdana", size = 12, slant = "italic")
		myFont1 = Font(family = "Verdana", size = 20, slant = "italic")
		self.addLabel(text = "Salary Calculator", row = 0, column = 0, font = myFont1, sticky = "NSEW", columnspan = 2, background = "lightgreen")
		self.addLabel(text = "Hourly Wage:", row = 1, column = 0, font = myFont, background = "skyblue")
		self.addLabel(text = "No. of Hours Worked:", row = 2, column = 0, font = myFont, background = "skyblue")
		self.addLabel(text = "The Employee's salary is:", row = 3, column = 0, font = myFont, background = "skyblue")

		self.hourlyWage = self.addFloatField(value = 0.0, row = 1, column = 1)
		self.noHoursWorked = self.addIntegerField(value = 0, row = 2, column = 1, width = 20)
		self.compute = self.addButton(text = "Compute", row = 2, column = 0, columnspan = 2, command = self.compute)
#		self.outputArea = self.addFloatField(text = "", row = 3, column = 1, state = "readonly", columnspan = 2, precision = 2)
		self.outputArea = self.addTextField(text = "", row = 3, column = 1, state = "readonly", columnspan = 2)
		self.noHoursWorked.bind("<Return>", lambda event: self.compute())
		self.compute["background"] = "palegoldenrod"
		self.compute["width"] = 15
	# Definition of the compute function, which is the event handler.
	def compute(self):
			""" Computes the investment schedule based on the inputs and outputs to the text area widget in tabular format."""
			# Obtain and validate the inputs.
			wage = self.hourlyWage.getNumber()
			hours = self.noHoursWorked.getNumber()
			pay = wage * hours

			if wage == 0 or hours == 0:
				return

			# Output the results

			self.outputArea.setText(pay)

# Global definition of the main() method.
def main():
	# Instantiate an object from the class into mainLoop()
	SalaryCalculator().mainloop()

# Global call to main() for program entry.
if __name__ == '__main__':
	main()



