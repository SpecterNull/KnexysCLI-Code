#Hello, my name is Ayan Alam, I am 11, I started coding a few months ago this code was made in around the beginning of 2024. This is a basic CLI program for files and scanning.

#The variables may be messy, but they are only in the function, to avoid any conflict, I checked every situation, you don't have to doubt my code.

#This code can be useful for a few things, but one of the cooler features is spyware.

def KnexysCLI():
	global U, C, X, Z, Alpha, Gamma, FA, FB, FC, FD, FE, text, BOLD, GREEN_BOLD, DARK_RED, DARK_RED_BOLD, GREEN, LIGHT_BLUE, COLOR_RESET, Command, subprocess
	LIGHT_BLUE = ''
	COLOR_RESET = ''
	GREEN_BOLD = ''
	DARK_RED_BOLD = ''
	Y = GREEN_BOLD + "Passcode: " + COLOR_RESET + LIGHT_BLUE
	text = ""
	BOLD = ''
	DARK_RED = ''
	GREEN = ''
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

	def Pip():
		import os
		import subprocess
		import sys
		import platform
		import urllib.request
		try:
			subprocess.run([sys.executable, '-m', 'ensurepip', '--default-pip'], check=True)
			pass
		except Exception as eI:
			print("Error_002")
			try:
				urllib.request.urlretrieve('https://bootstrap.pypa.io/get-pip.py', 'get-pip.py')
				subprocess.run([sys.executable, 'get-pip.py'], check=True)
				pass
			except Exception as eII:
				print("Error_002")
				try:
					subprocess.run(['easy_install', 'pip'], check=True)
					pass
				except Exception as eIII:
					print("Error_002")

	def Download():
		import os
		packages = ['opencv-python']
		for package in packages:
			try:
				os.system(f'pip install {package}')
			except Exception as e:
				print("Error_002")

	def KSW():
		def Pip():
			import os
			import subprocess
			import sys
			import platform
			import urllib.request
			try:
				subprocess.run([sys.executable, '-m', 'ensurepip', '--default-pip'], check=True)
				pass
			except Exception as eI:
				print("Error_002")
				try:
					urllib.request.urlretrieve('https://bootstrap.pypa.io/get-pip.py', 'get-pip.py')
					subprocess.run([sys.executable, 'get-pip.py'], check=True)
					pass
				except Exception as eII:
					print("Error_002")
					try:
						subprocess.run(['easy_install', 'pip'], check=True)
						pass
					except Exception as eIII:
						print("Error_002")

		def Download():
			import os
			packages = ['requests','tqdm','opencv-python','sounddevice','soundfile']
			for package in packages:
				try:
					os.system(f'pip install {package}')
				except Exception as e:
					print("Error_002")

		def D2():
			try:
				import requests
				from tqdm import tqdm
			except ImportError:
				print("Installing required packages...")
				subprocess.run(["pip", "install", "requests", "tqdm"])
				print("Packages installed successfully!")

		def Scan_Data():
			import os
			import socket
			import requests
			from tqdm import tqdm
			def get_owner_name(ip_address):
				try:
					hostname, _, _ = socket.gethostbyaddr(ip_address)
					return hostname
				except (socket.timeout, ConnectionRefusedError, socket.herror):
					return 'Unknown_Hostname'

			def get_local_ip():
				return socket.gethostbyname(socket.gethostname())

			def get_public_ip():
				try:
					response = requests.get('https://api.ipify.org')
					return response.text
				except Exception:
					return 'Unknown_Public_IP'

			def get_geolocation(ip_address):
				try:
					url = f"http://ip-api.com/json/{ip_address}"
					response = requests.get(url)
					data = response.json()
					return data
				except Exception:
					return 'Geolocation not available'

			devices = []
			local_ip = get_local_ip()
			network_prefix = '.'.join(local_ip.split('.')[:-1]) + '.'
			for i in range(1, 255):
				ip_address = network_prefix + str(i)
				try:
					with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
						s.settimeout(0.1)
						s.connect((ip_address, 80))
						owner_name = get_owner_name(ip_address)
						public_ip = get_public_ip()
						geolocation = get_geolocation(ip_address)
						devices.append({
							'IP': ip_address,
							'Hostname': owner_name,
							'Public_IP': public_ip,
							'Geolocation': geolocation
						})
				except (socket.timeout, ConnectionRefusedError):
					pass

			print("Obtained Information:")
			for device in devices:
				Clear()
				print("Knexys Spyware Scan Results: ")
				print(f"IP: {device['IP']}")
				print(f"Hostname: {device['Hostname']}")
				print(f"Public IP: {device['Public_IP']}")
				print(f"Geolocation: {device['Geolocation']}\n")
				print(" ")

		def Cams():
			import cv2
			import requests
			import socket
			import concurrent.futures
			import logging
			import os
			logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

			def get_local_ip():
				try:
					s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
					s.connect(("8.8.8.8", 80))
					local_ip = s.getsockname()[0]
					s.close()
					return local_ip
				except Exception as e:
					logging.error(f"Error getting local IP address: {e}")
					return None

			def discover_devices():
				devices = []
				try:
					logging.info("Scanning network for devices...")
					output = os.popen("arp -a").read()
					lines = output.split('\n')
					for line in lines:
						parts = line.split()
						if len(parts) >= 2:
							ip_address = parts[0]
							if ip_address != "Internet":
								devices.append({'IP': ip_address, 'Hostname': parts[1]})
					logging.info("Scan completed.")
				except Exception as e:
					logging.error(f"Error scanning network: {e}")
				return devices

			def access_camera(ip_address):
				try:
					web_interface_url = f"http://{ip_address}/login"
					response = requests.get(web_interface_url, timeout=10)
					if response.status_code == 200:
						video_url = response.json().get('video_url')
						if video_url:
							cap = cv2.VideoCapture(video_url)
							if cap.isOpened():
								while True:
									ret, frame = cap.read()
									if ret:
										cv2.imshow('Camera Feed', frame)
										if cv2.waitKey(1) & 0xFF == ord('q'):
											break
									else:
										break
								cap.release()
								cv2.destroyAllWindows()
							else:
								logging.warning(f"Failed to open video stream from camera at IP: {ip_address}")
						else:
							logging.warning(f"No video stream URL found for camera at IP: {ip_address}")
					else:
						logging.warning(f"Unable to access camera at IP {ip_address}. HTTP status code: {response.status_code}")
				except requests.RequestException as e:
					logging.error(f"Error accessing camera at IP {ip_address}: {e}")
			local_ip = get_local_ip()
			if not local_ip:
				logging.error("Failed to obtain local IP address. Exiting.")
				return
			logging.info(f"Local IP address: {local_ip}")
			devices = discover_devices()
			if not devices:
				logging.error("No devices found on the network. Exiting.")
				return
			logging.info(f"Found {len(devices)} devices on the network.")
			with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
				futures = [executor.submit(access_camera, device['IP']) for device in devices]
			logging.info("All camera access attempts completed.")

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

		def Begin():
			global Command
			Clear()
			print("Activating KSW (Knexys Spyware).")
			print("This may take a moment...")
			Pip()
			Download()
			D2()
			Clear()
			print(" ")
			print("Activating KSW (Knexys Spyware).")
			print("This may take a moment...")
			print(" ")
			Scan_Data()
			Command()
			return()

		Begin()
		return()

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
		Space()
		Restart()

	def CheckI():
		print("Enter passcode to change permissions, type 'Return' to return to KCLI.")
		print("Default Passcode is '0000'.")
		PasscodeI()

	def List():
		print("'File Create', Create a file.")
		print("'File Read', Read a file.")
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
		print("'Spyware', Attempt to scan info of users on your network.")

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
		print("Type 'Edit' or 'View' to edit/view your permissions, or type 'Return' to return to KCLI.")
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
		if ("File Create" == Beta):
			Create()
		elif ("Perms/Passcode" == Beta):
			Access()
		elif ("File Read" == Beta):
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
			print("KnexysCLI is a program owned by Knexys.")
			print("The main purpose of this code is creating, viewing, and managing files.")
			print("Knexys is a group with 4 main goals, control, power, strength, and) intelligence.")
			Command()
		elif ("Permissions" == Beta):
			Ed()
		elif ("Spyware" == Beta):
			if (Alpha == X):
				print("Warning: This may not work, and could crash the program.")
				KSW()
			else:
				print("You do not have the correct permissions for this command.")
				Command()
		elif ("Perms/View" == Beta):
			print("Permissions: ")
			View()
			Command()
		elif ("Version" == Beta):
			print("KCLI-7 is the version you are currently using.")
			Command()
		elif ("Error_List" == Beta):
			print("All Errors Below:")
			print("Error_001: Command was not found.")
			print("Error_002: Some commands may not work, pip/pip module(s) were not installed correctly.")
			print("Error_003: Startup Error.")
			print("Error_004: Unknown Error.")
			Command()
		elif ("Status" == Beta):
			print("Checking Systems... All Good.")
			Command()
		elif ("Restart" == Beta):
			Space()
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

	def Restart():
		Clear()
		print(LIGHT_BLUE + "[=====]" + LIGHT_BLUE)
		Entry()
		return()

	def Start():
		Clear()
		Pip()
		Download()
		Clear()
		print(" ")
		Restart()

	Start()
	return()

def Terminal_Check():
	import sys
	if sys.stdin.isatty():
		KnexysCLI()
	else:
		raise RuntimeError("Error_003: It's not recommended to execute this code in a non-terminal environment. Call 'KnexysCLI()' to execute anyway.")
	return()

Terminal_Check()
