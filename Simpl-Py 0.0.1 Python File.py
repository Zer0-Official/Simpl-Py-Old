#Define Variables
version = '0.0.1'
updated = '7/15/2021'
available = 'GitHub'

#System Info Display
import wmi
c = wmi.WMI()   
my_system = c.Win32_ComputerSystem()[0]
print(f"System Info:  {my_system.Name} - {my_system.Manufacturer} - {my_system. Model} - {my_system.SystemType}")

#Welcome Display
print('Welcome to Simpl-Py ' + version + ' (Last Updated: ' + updated + ')')
print('Type "help", "copyright", or "credits" for more information.')

#Loop to Start
while True:
	code = input('\n>>>')
  
  #Help Info
	while code == ('help'):
		print('---HELP---')
		cHelp = input('Type "docs" or "problem" for more information:  ')
		if cHelp == ('docs'):
			print('You can find the complete documentation at: https://sites.google.com/view/simpl-py/docs')
			break
		if cHelp == ('problem'):
			print('Report any bugs, flaws, or errors at the GitHub project page or send them to: vlethestars10@gmail.com')
			break
		else:
			print('That is not a valid choice. Please try again.')
  			
  #Copyright Info
	if code == ('copyright'):
		print('---COPYRIGHT---')
		print('The Simpl-Py Interpreter is made 100% by Zer0. Do not use this project or code without written permission from Zer0.')
		print('For more info and permissions, email: vlethestars10@gmail.com')
  	
  #Credits Info
	if code == ('credits'):
		print('---CREDITS---')
		print('The Simpl-Py Interpreter is made 100% by Zer0. While we may of used tutorials or advice from others, no one has given code, names, etc.')
  
  #Simpl-Py Input
	if code == ('Simpl-Py'):
		print('Simpl-Py Interpreter')
		print('Version: ' + version)
		print('Last Updated: ' + updated)
		print('Available On: ' + available)
		print('Created: 7/12/2021')
  
  
  #----- Main Code -----
  
	if code == ('print'):
		cPrint = input('Print What?  ')
		print(cPrint)
  	
	if code == ('echo.print'):  #Or echo
		cEcho = input('Echo What?  ')
		cEchoTimes = int(input('Echo Amount?  '))
		cEchoOutput = cEcho * cEchoTimes
		print(cEchoOutput)
		
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
    
  
  #Slash Commands
	while code == ('/get'):
		cGet = input('Get What?  ')
		if cGet == ('system_info'):
			print(f"System Info:  {my_system.Name} - {my_system.Manufacturer} - {my_system. Model} - {my_system.SystemType}")
			break
		if cGet == ('last_updated'):
			print('Simpl-Py last updated: ')
			break
		if cGet == ('version'):
			print('Simpl-Py version: ')
			break
		if cGet == ('available'):
			print('Simpl-Py available on: ')
			break
		if cGet == ('docs'):
			print('You can find the docs at: https://sites.google.com/view/simpl-py/docs')
			break
		if cGet == ('web_link'):
			print('Zer0 Website: https://sites.google.com/view/zer0-official/home')
			print('Simpl-Py Website: https://sites.google.com/view/simpl-py/home')
			break
		else:
			print('/get function not found. Try again.')
			
	while code == ('/find'):
		cFind = input('Find What?  ')
		#if cFind == ('')
		print('/find is not available at the moment. Simpl-Py version 0.1.0 will fix this.')
		break
		
	while code == ('/interact'):
		cInteract = input('Interact What?  ')
		if cInteract == ('change_log'):
			print('You can find the change log at: https://sites.google.com/view/simpl-py/docs/changelog')
			break
		if cInteract == ('beta_version'):
			print('There is no BETA version right now.')
			break
		if cInteract == ('i_care'):
			print('Thank you for caring about Simpl-Py!')
			print('Email vlethestars10@gmail.com the number "001" to show you care.')
			break
		else:
			print('That is not a valid /interact. Try again.')
			
    
#Report Bugs Please
