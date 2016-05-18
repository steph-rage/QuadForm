print("To determine the complex solutions to an equation of the form ax^2 + bx + c = 0, enter the values for a, b and c")
a = float(raw_input("a: "))
b = float(raw_input("b: "))
c = float(raw_input("c: "))
det = b**2 - 4*a*c
if det >= 0:
	Ans1 = (-b + det**0.5)/(2*a)
	Ans2 = (-b - det**0.5)/(2*a)
	print("The solutions for x are: %f and %f" %(Ans1, Ans2))
else:
	Ans_Real = -b/(2*a)  
	Ans_Imag = (-det)**0.5/(2*a)
	print("The solutions for x are %f + %fi and %f - %fi" %(Ans_Real, Ans_Imag, Ans_Real, Ans_Imag))

