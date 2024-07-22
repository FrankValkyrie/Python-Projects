from tkinter import *
class DebtCalculator:

	def __init__(self):

		window = Tk()
		window.title("Debt Calculator")
		window.configure(background='black')
		''' input labels '''
		Label(window, text = "Loan Amount", background="black", fg="white").grid(row = 3, column = 1, sticky = W)
		Label(window, text = "Number of Years", background="black", fg="white").grid(row = 2, column = 1, sticky = W)
		Label(window, text = "Annual Interest Rate", background="black", fg="white").grid(row = 1, column = 1, sticky = W)
		Label(window, text = "Monthly Payment", background="black", fg="white").grid(row = 4, column = 1, sticky = W)
		Label(window, text = "Total Payment", background="black", fg="white").grid(row = 5, column = 1, sticky = W)
		''' input logic'''
		self.annualInterestRate = StringVar()
		Entry(window, textvariable = self.annualInterestRate, justify = RIGHT).grid(row = 1, column = 2)
		self.numberOfYears = StringVar()

		Entry(window, textvariable = self.numberOfYears, justify = RIGHT).grid(row = 2, column = 2)
		self.loanAmountVar = StringVar()

		Entry(window, textvariable = self.loanAmountVar, justify = RIGHT).grid(row = 3, column = 2)
		self.monthlyPayment = StringVar()
		lblMonthlyPayment = Label(window, textvariable = self.monthlyPayment, background="white", borderwidth=1, relief="solid", width = 17).grid(row = 4, column = 2, sticky = E)

		self.totalPayment = StringVar()
		lblTotalPayment = Label(window, textvariable = self.totalPayment, background="white", fg="black", width = 17, borderwidth=1, relief="solid").grid(row = 5, column = 2, sticky = E)
		
		''' buttons'''
		btcalculate = Button(window, text = "Calculate", command = self.calculate, background="green", fg="white").grid(row = 6, column = 2, sticky = E) 
		window.mainloop()

	def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears): 
		monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
		return monthlyPayment;

	def calculate(self):	
		monthlyPayment = self.getMonthlyPayment(
		float(self.loanAmountVar.get()),
		float(self.annualInterestRate.get()) / 1200,
		int(self.numberOfYears.get()))

		self.monthlyPayment.set(format(monthlyPayment, '10.2f'))
		totalPayment = float(self.monthlyPayment.get()) * 12 \
								* int(self.numberOfYears.get())

		self.totalPayment.set(format(totalPayment, '10.2f'))


DebtCalculator()
