def KnexysCLI():
	global U, C, X, Z, Alpha, Gamma, FA, FB, FC, FD, FE, text, BOLD, GREEN_BOLD, DARK_RED, DARK_RED_BOLD, GREEN, LIGHT_BLUE, COLOR_RESET
	LIGHT_BLUE = '\033[94m'
	COLOR_RESET = '\033[0m'
	GREEN_BOLD = '\033[1;92m'
	DARK_RED_BOLD = '\033[1m\033[91m'
	Y = GREEN_BOLD + "Passcode: " + COLOR_RESET + LIGHT_BLUE
	text = ""
	BOLD = '\033[1m'
	DARK_RED = '\033[31m'
	GREEN = '\033[92m'
	Alpha = GREEN_BOLD + "User@Knexys: " + COLOR_RESET + LIGHT_BLUE
	X = DARK_RED_BOLD + "Admin@Knexys: " + COLOR_RESET + LIGHT_BLUE
	Z = GREEN_BOLD + "User@Knexys: " + COLOR_RESET + LIGHT_BLUE
	U = "0000"
	C = "0000"
	FA = "No file exists, to create one, type 'File_Create'."
	FB = "No file exists, to create one, type 'File_Create'."
	FC = "No file exists, to create one, type 'File_Create'."
	FD = "No file exists, to create one, type 'File_Create'."
	FE = "No file exists, to create one, type 'File_Create'."
	Gamma = False

	def Scan():
		import socket
		def get_owner_name(ip_address):
			try:
				hostname, _, _ = socket.gethostbyaddr(ip_address)
				return hostname
			except (socket.timeout, ConnectionRefusedError, socket.herror):
				return 'Unknown_Hostname'

		devices = []
		local_ip = socket.gethostbyname(socket.gethostname())
		network_prefix = '.'.join(local_ip.split('.')[:-1]) + '.'

		for i in range(1, 255):
			ip_address = network_prefix + str(i)
			try:
				with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
					s.settimeout(0.1)
					s.connect((ip_address, 80))
					owner_name = get_owner_name(ip_address)
					devices.append((ip_address, owner_name))
			except (socket.timeout, ConnectionRefusedError):
				devices.append((ip_address, 'Unknown_Hostname'))

		print("Obtained IP Addresses:")
		for ip, owner_name in devices:
			print(f"{ip}, Name: {owner_name}")

	def ChangeText(text):
		import os
		LIGHT_BLUE = '\033[94m'
		COLOR_RESET = '\033[0m'
		if "[=====]" in text:
			changed_text = text.replace("[=====]", LIGHT_BLUE + "[=====]" + LIGHT_BLUE)
			return changed_text
		else:
			return text

	def Clear():
		import os
		import platform
		ms = [
			'cls' if platform.system() == 'Windows' else 'clear',
			'tput clear',
			'reset'
		]
		for m in ms:
			try:
				os.system(m)
				break
			except Exception as e:
				continue
		else:
			pass

	def NewAdmin():
		global AA, BB, C, U
		AA = input("New Passcode: ")
		C = AA
		BB = input("New Permissions Passcode: ")
		U = AA
		print("All done, KnexysCLI has restarted.")
		Restart()

	def CheckI():
		print("Default Passcode is '0000'.")
		PasscodeI()

	def List():
		print("'File_Create', Create a file.")
		print("'File_Read', Read a file.")
		print("'Permissions', Edit permissions.")
		print("'Perms/View', View permissions.")
		print("'Perms/Passcode', Edit permissions passcode.")
		print("'Edit_Passcode', Edit passcode.")
		print("'Error_List', Lists all error types and meanings of errors.")
		print("'Info', Info about Knexys, and KnexysCLI.")
		print("'Help', Some information, and a list of commands.")
		print("'Exit, Exit KnexysCLI.")
		print("'Restart', Restart this program.")
		print("'Status', Tests if the code works.")
		print("'Version', Shows the version of this program.")
		print("'Scan', Attempt to scan all IPs on a wifi network.")

	def FileCreateA():
		global FA
		print("Create a file here. Files are used for documentation, notes, etc.")
		print("Enter the content of the file. (Press Enter three times to finish.")
		clA = []
		celA = 0
		while celA < 3:
			lA = input("File: ")
			if lA:
				clA.append(lA)
				celA = 0
			else:
				celA += 1
		FA = '\n'.join(clA)
		print("The file has been created. To read it, type 'File_Read'.")
		Command()

	def FileCreateB():
		global FB
		print("Create a file here. Files are used for documentation, notes, etc.")
		print("Enter the content of the file. (Press Enter three times to finish.):")
		clB = []
		celB = 0
		while celB < 3:
			lB = input("File: ")
			if lB:
				clB.append(lB)
				celB = 0
			else:
				celB += 1
		FB = '\n'.join(clB)
		print("The file has been created. To read it, type 'File_Read'.")
		Command()

	def FileCreateC():
		global FC
		print("Create a file here. Files are used for documentation, notes, etc.")
		print("Enter the content of the file. (Press Enter three times to finish.):")
		clC = []
		celC = 0
		while celC < 3:
			lC = input("File: ")
			if lC:
				clC.append(lC)
				celC = 0
			else:
				celC += 1
		FC = '\n'.join(clC)
		print("The file has been created. To read it, type 'File_Read'.")
		Command()

	def FileCreateD():
		global FD
		print("Create a file here. Files are used for documentation, notes, etc.")
		print("Enter the content of the file. (Press Enter three times to finish.):")
		clD = []
		celD = 0
		while celD < 3:
			lD = input("File: ")
			if lD:
				clD.append(lD)
				celD = 0
			else:
				celD += 1
		FD = '\n'.join(clD)
		print("The file has been created. To read it, type 'File_Read'.")
		Command()

	def FileCreateE():
		global FE
		print("Create a file here. Files are used for documentation, notes, etc.")
		print("Enter the content of the file. Press Enter three times to finish.")
		clE = []
		celE = 0
		while celE < 3:
			lE = input("File: ")
			if lE:
				clE.append(lE)
				celE = 0
			else:
				celE += 1
		FE = '\n'.join(clE)
		print("The file has been created. To read it, type 'File_Read'.")
		Command()

	def PasscodeEdit():
		global C, K
		K = input("New Passcode: ")
		C = K
		print("Passcode changed.")
		Command()

	def Access():
		if (Alpha == X):
			PasscodeEditI()
		else:
			print("You don't have the correct permissions for this.")
			Command()

	def AccessI():
		if (Alpha == X):
			PasscodeEdit()
		else:
			print("You don't have the correct permissions for this.")
			Command()

	def Level():
		if ("Admin" == Gamma):
			Alpha = X
		elif("User" == Gamma):
			Alpha = Z
		else:
			Alpha = GREEN_BOLD + "User@Knexys: " + COLOR_RESET + LIGHT_BLUE

	def Decide():
		global Alpha, Gamma, X, Z
		print("Note: Do the 'Restart' command after selecting a level.")
		Gamma = input("User or Admin? ")
		if ("Admin" == Gamma):
			Alpha = X
			print("Permission Selected, Set up passcodes.")
			Level()
			NewAdmin()
		elif("User" == Gamma):
			Alpha = Z
			print("Permission Selected, returned to CLI.")
			Level()
			Command()
		elif("Return" == Gamma):
			print("Returned to CLI.")
			Command()
		else:
			print("Not an option, type 'Return' to return to KnexysCLI.")
			Decide()

	def Edit():
		O = input("Editing Permissions: ")
		if ("Edit" == O):
			CheckI()
		elif ("View" == O):
			View()
		elif ("Return" == O):
			Command()
		else:
			print("Error_001")
			Edit()

	def Perms():
		print("Type 'Edit' or 'View' to edit/view your permissions, or type 'Return' to return to KnexysCLI.")
		Edit()

	def PasscodeEditI():
		global U, D
		D = input("New Permissions Passcode: ")
		U = D
		print("Permissions Passcode has been changed.")
		Command()

	def View():
		if (Alpha == X):
			print("You have Admin permissions.")
			Command()
		else:
			print("You have User permissions.")
			Command()

	def Ed():
		print("You can view and edit permissions here")
		Perms()

	def FileView():
		print("Pick a file from '1' to '5' to view, or type 'Return' to return to KnexysCLI.")
		V = input("Choose File: ")
		if ("1" == V):
			print(FA)
		elif ("2" == V):
			print(FB)
		elif ("3" == V):
			print(FC)
		elif ("4" == V):
			print(FD)
		elif ("5" == V):
			print(FE)
		elif ("Return" == V):
			print("Files have been exited.")
			Command()
		else:
			print("Not an option.")
			FileView()

	def Command():
		global Beta, Alpha
		Level()
		Beta = False
		Beta = input(Alpha)
		if ("File_Create" == Beta):
			Create()
		elif ("Perms/Passcode" == Beta):
			Access()
		elif ("File_Read" == Beta):
			FileView()
			Command()
		elif ("Help" == Beta):
			print("If you're typing a command, don't include the quotes, or anything oustide the quotes.")
			print("Only include what's inside of the quotes.")
			print("Type all commands with uppercase beginnings")
			print("Here's a list of commands you can do.")
			List()
			Command()
		elif ("Exit" == Beta):
			print(DARK_RED_BOLD + "KnexysCLI has been exited." + COLOR_RESET + LIGHT_BLUE)
			Clear()
		elif ("Edit_Passcode" == Beta):
			AccessI()
		elif ("Info" == Beta):
			print("KnexysCLI is a program created by Knexys.")
			print("The main purpose of this code is creating, viewing, and managing files.")
			print("Knexys is a group with 4 main goals, control, power, strength, and) intelligence.")
			Command()
		elif ("Permissions" == Beta):
			Ed()
		elif ("Scan" == Beta):
			if (Alpha == X):
				print("Scanning IPs... This could take a moment.")
				Scan()
				Command()
			else:
				print("You do not have the correct permissions for this command.")
				Command()
		elif ("Perms/View" == Beta):
			View()
			Command()
		elif ("Version" == Beta):
			print("KCLI-7 is the version you are currently using.")
			Command()
		elif ("Error_List" == Beta):
			print("All Errors Below:")
			print("Error_001: Command was not found.")
			Command()
		elif ("Status" == Beta):
			print("Checking Systems... All Good.")
			Command()
		elif ("Restart" == Beta):
			Restart()
		else:
			print(DARK_RED_BOLD + "Error_001" + COLOR_RESET + LIGHT_BLUE)
			Command()

	def Create():
		print("Type '1' to '5' to choose 1 of 5 files to create text in, or type 'Return' to exit 'File_Create'.")
		I = input("Choose File: ")
		if ("1" == I):
			FileCreateA()
		elif ("2" == I):
			FileCreateB()
		elif ("3" == I):
			FileCreateC()
		elif ("4" == I):
			FileCreateD()
		elif ("5" == I):
			FileCreateE()
		elif ("Return" == I):
			print("Files have been exited")
			Command()
		else:
			print("Not an option.")
			Create()

	def Terminal():
		print("""Welcome to KnexysCLI, Passcode Correct. KCLI: Knexys Command Line Interface""")
		print("Type the 'Help' command for help, without the quotes.")
		Command()

	def Passcode():
		global C
		Theta = False
		Theta = input(Y)
		if (Theta == C):
			print("Correct, Access Granted.")
			Level()
			Terminal()
		elif ("Exit" == Theta):
			print(DARK_RED_BOLD + "KnexysCLI has been exited." + COLOR_RESET + LIGHT_BLUE)
			Clear()
		else:
			print(DARK_RED_BOLD + "Incorrect." + COLOR_RESET + LIGHT_BLUE)
			Passcode()

	def Space():
		for i in range(500):
			print(" ")

	def PasscodeI():
		global U, ThetaI
		ThetaI = False
		ThetaI = input(Y)
		if (U == ThetaI):
			print("Correct, Access Granted.")
			Decide()
		elif ("Return" == ThetaI):
			print("Returned to KCLI.")
			Command()
		else:
			print(DARK_RED_BOLD + "Incorrect." + COLOR_RESET + LIGHT_BLUE)
			PasscodeI()

	def PasscodeInfo():
		print("Default Passcode: '0000'.")
		print("Enter passcode to gain accsess.")
		Passcode()

	def	Entry():
		print("KnexysCLI")
		PasscodeInfo()

	def Start():
		Clear()
		print(LIGHT_BLUE + "[=====]" + LIGHT_BLUE)
		Entry()

	def Restart():
		Space()
		Clear()
		Start()
		return()

	Start()
	return()

KnexysCLI()
