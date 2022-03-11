#Define Variables
version = '0.2.0'
updated = '3/10/2022'
available = 'GitHub, Simpl-Py Website'
var1 = 0
var2 = 0
var3 = 0

#System Info Display
import wmi
c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]
print(f"System Info:  {my_system.Name} - {my_system.Manufacturer} - {my_system. Model} - {my_system.SystemType}")

#Welcome Display
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Welcome to Simpl-Py ' + version + ' (Last Updated: ' + updated + ')')
print('Type "help", "copyright", or "credits" for more information.')

#Loop to Start
while True:
	code = input('\n>>> ')

  #Help Info
	if code == ('help'):
		print('---HELP---')
		print()
		print('Report any bugs, flaws, or errors at the GitHub project page: https://github.com/Zer0-Official/Simpl-Py/issues')

  #Copyright Info
	elif code == ('copyright'):
		print('---COPYRIGHT---')
		print()
		with open("Extras/copyright.txt", "r") as file:
			for CopyrightContents in file:
				print(CopyrightContents)

  #Credits Info
	elif code == ('credits'):
		print('---CREDITS---')
		print()
		with open("Extras/credits.txt", "r") as file:
			for CreditsContents in file:
				print(CreditsContents)


# - - - - - Main Code - - - - -

	#Print Functions
	elif code == ('print'):
		cPrint = input('Print What?  ')
		print(cPrint)

	elif code == ('echo.print'):  #Or echo
		cEcho = input('Echo What?  ')
		cEchoTimes = int(input('Echo Amount?  '))
		cEchoOutput = cEcho * cEchoTimes
		print(cEchoOutput)

	while code == ('print_var'):
		cPrintVar = input('What Variable?  ')
		if cPrintVar == ('var1'):
			print(var1)
			break
		if cPrintVar == ('var2'):
			print(var2)
			break
		if cPrintVar == ('var3'):
			print(var3)
			break
		else:
			print('Variable not found. Try again.')

	while code == ('print_math'):  #Or calc
		cMathInt1 = int(input('First Integer:  '))
		cMathOp = input('Operator? (+, -, *, /)  ')
		cMathInt2 = int(input('Second Integer:  '))
		if cMathOp == '+':
			print('{} + {} = '.format(cMathInt1, cMathInt2))
			print(cMathInt1 + cMathInt2)
			break
		elif cMathOp == '-':
			print('{} - {} = '.format(cMathInt1, cMathInt2))
			print(cMathInt1 - cMathInt2)
			break
		elif cMathOp == '*':
			print('{} * {} = '.format(cMathInt1, cMathInt2))
			print(cMathInt1 * cMathInt2)
			break
		elif cMathOp == '/':
			print('{} / {} = '.format(cMathInt1, cMathInt2))
			print(cMathInt1 / cMathInt2)
			break
		else:
			print('Invalid Operator. Try again.')

	if code == ('correct.print'):
		cCorrect = input('Correct What?  ')
		print(cCorrect.capitalize())

	elif code == ('lower.print'):
		cLower = input('Lowercase What?  ')
		print(cLower.lower())

	elif code == ('upper.print'):
		cUpper = input('Uppercase What?  ')
		print(cUpper.upper())

	elif code == ('backwards.print'):
		cBackwards = input('Backwards What?  ')
		print(cBackwards [::-1])

	#Variables
	if code == ('var1'):
		cVar1Value = input('New Variable Value:  ')
		var1 = cVar1Value
		print('var1 set to: ' + var1)
	if code == ('var2'):
		cVar2Value = input('New Variable Value:  ')
		var2 = cVar2Value
		print('var2 set to: ' + var2)
	if code == ('var3'):
		cVar3Value = input('New Variable Value:  ')
		var3 = cVar3Value
		print('var3 set to: ' + var3)

	#Txt File Control
	while code == ('txt.open'):
		cOpenName = input('Name?  ')
		cOpenWrite = input('Write? (y/n)  ')
		if cOpenWrite == 'n':
			cOpenRead = input('Read? (y/n)  ')
			if cOpenRead == 'n':
				break
			if cOpenRead == 'y':
				cFile = open('Extras/MyDocuments/' + cOpenName, "r")
				print(cFile.readlines())
				break
			else:
				print('Not understood. Try again.')
		if cOpenWrite == 'y':
			cWrite = input('Write What?  ')
			cFile = open("Extras/MyDocuments/" + cOpenName, "a")#append mode
			cFile.write(cWrite)
			break
		else:
			print('Not understood. Try again.')

	if code == ('txt.new'):
		cNewName = input('New File Name?  ')
		cFile = open("Extras/MyDocuments/" + cNewName, "w+")

	#Slash Commands
	while code == ('/get'):
		cGet = input('Get What?  ')
		if cGet == ('system_info'):
			print(f"System Info:  {my_system.Name} - {my_system.Manufacturer} - {my_system. Model} - {my_system.SystemType}")
			break
		else:
			print('/get function not found. Try again.')

	while code == ('/find'):
		cFind = input('Find What?  ')
		if cFind == ('help'):
			print('Use `help` to report a problem.')
			break
		if cFind == ('copyright'):
			print('Use `copyright` to see Copyright info.')
			break
		if cFind == ('credits'):
			print('Use `credits` to see Credits info.')
			break
		if cFind == ('print'):
			print('''Typing ‘print’ is the basic print function. You will be asked, ‘Print
What?’ Now, you can type anything you want to be printed. After
entering, the computer will print out your text.''')
			break
		if cFind == ('echo.print'):
			print('''This is a different type of printing that will cause your text to be
printed multiple times. Typing the function will ask you, ‘Echo What?’
You can now type anything you want to print. Next, you will be asked,
‘Echo Amount?’ Type an integer that states how many times you want
to print the text. The computer will now echo your text.''')
			break
		if cFind == ('print_math'):
			print('''This will print math equations. You will be asked for the first integer,
operator, and second integer. The computer will print out the math
equation and the answer.''')
			break
		if cFind == ('print_var'):
			print('''This will print the value of a variable. You will be asked, ‘What
Variable?’ Type back the desired variable name and the computer will
print out the value of that variable.''')
			break
		if cFind == ('/get'):
			print('''This command can retrieve info. Just type /get and enter one of these names:
	● system_info : shows your system info''')
			break
		if cFind == ('/find'):
			print('You are using /find right now!')
			print('''This command will ask you, ‘Find What?’ Just type in any command
or function and it will give you doc info on it.''')
			break
		if cFind == ('/Simpl-Py'):
			print('''This command will ask you, ‘Simpl-Py Command?’ You can then type any of the following:
	● last_updated : shows Simpl-Py last update date
	● version : shows the current Simpl-Py version
	● available : shows where Simpl-Py is available
	● docs : gives a website link to the documentation
	● web_link : gives website links to Simpl-Py and Zer0
	● change_log : brings you to the change log
	● beta_version : unlocks beta version (if available)
	● i_care : type this if you deeply care about Simpl-Py
	● create_date : type this to get the Simpl-Py creation date''')
			break
		if cFind == ('variables'):
			print('''There is only one variable that you can make for now, but we will add
more eventually. The variable is named ‘var1’ and the name cannot
be changed (for now). It is set to 0 each time you run the project. To
change the value, type ‘var1’ and you will be asked for a new variable
value. Type any text or number amount. See the print section above
to learn how to print the value.''')
			break
		if cFind == ('commenting'):
			print('''To comment, just type a non-command string. The computer will
ignore it. This also means that any wrong code will not register.''')
			break
		else:
			print('/find function not found. Try again.')

	while code == ('/Simpl-Py'):
		cSimplPy = input('Simpl-Py Command?  ')
		if cSimplPy == ('last_updated'):
			print('Simpl-Py last updated: ' + updated)
			break
		if cSimplPy == ('version'):
			print('Simpl-Py version: ' + version)
			break
		if cSimplPy == ('available'):
			print('Simpl-Py available on: ' + available)
			break
		if cSimplPy == ('docs'):
			print('You can find the docs at: https://sites.google.com/view/simpl-py/docs')
			break
		if cSimplPy == ('web_link'):
			print('Zer0 Website: https://sites.google.com/view/zer0-official/home')
			print('Simpl-Py Website: https://sites.google.com/view/simpl-py/home')
			break
		if cSimplPy == ('change_log'):
			print('You can find the change log at: https://sites.google.com/view/simpl-py/docs/changelog')
			break
		if cSimplPy == ('beta_version'):
			print('There is no BETA version right now.')
			break
		if cSimplPy == ('i_care'):
			print('Thank you for caring about Simpl-Py!')
			break
		if cSimplPy == ('create_date'):
			print('Simpl-Py was created: 7/12/2021')
			break
		else:
			print('/Simpl-Py function not found. Try again')

	if code == '/stop':
		exit()


#Please report any bugs
