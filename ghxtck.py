# Import necessary libraries
import subprocess  # Library for running shell commands
import os  # Library for interacting with the operating system
import webbrowser  # Library for opening web browsers
import time  # Library for time-related functions
import curses  # Library for creating text-based user interfaces
import pyfiglet  # Library for creating ASCII art text
from pyfiglet import Figlet  # Specific import to use the Figlet class

# Create a custom Figlet font object and print ASCII art text
custom_fig = Figlet(font='bubble')  # Creating a Figlet object with the 'bubble' font
print(custom_fig.renderText('GHAX ATTCK'))  # Printing ASCII art text 'GHAX ATTCK' using the custom Figlet font

# Dictionary of repository URLs and their respective directory names
repositories = {
    "dark-fantasy-exploit": "https://github.com/ritvikb99/dark-fantasy-exploit", 
    "tikhack": "https://github.com/Antpap07/tikhack",  
    "x11-repo": "https://github.com/x11-repo/exploit",  
    "DARKARMY": "https://github.com/D4RK-4RMY/DARKARMY",  
    "hackingtool": "https://github.com/Z4nzu/hackingtool", 
    "Memcrashed-DDoS-exploit": "https://github.com/649/Memcrashed-DDoS-exploit",  
    "WhatWeb": "https://github.com/urbanadventurer/WhatWeb",  
    "fsociety": "https://github.com/Manisso/fsociety", 
    "nexmo-cli": "https://github.com/Nexmo/nexmo-cli", 
    "nmap": "https://github.com/nmap/nmap"  
}


# Function to clone repositories
def clone_repository(repo_url):
    subprocess.run(['git', 'clone', repo_url])
    # This function uses 'subprocess.run' to execute the 'git clone' command to clone a repository specified by 'repo_url'
    
# Hacker menu display
print("\033[96mWelcome to the Hacker Menu\033[0m")
# Prints a welcome message in cyan color

# Displaying menu options
print("\033[96m------------------------\033[0m")
print("\033[93m1. Install repositories\033[0m")
print("\033[93m2. Update package list\033[0m")
print("\033[93m3. Install requirements.txt\033[0m")
print("\033[93m4. Install all available languages\033[0m")
print("\033[93m5. Install PhoneInfoga\033[0m")
print("\033[93m6. Download Nexmo-CLI\033[0m")
print("\033[93m7. Download BurpSuite\033[0m")
print("\033[93m8. Choose a repository to clone into\033[0m")
print("\033[93m9. Open Burp Suite\033[0m")
print("\033[93m10. nmap Test\033[0m")
print("\033[93m11. Install Security Tools\033[0m")
# Prints a menu with different options in yellow color

# Asking for user input
user_input = input("\033[96mPlease enter the number of the action you want to perform: \033[0m")
# Asks the user to input a number corresponding to the action they want to perform and stores it in the 'user_input' variable


# Perform the selected action based on user input

if user_input == '1':
    # If the user input is '1':
    
    user_input_repos = input("\033[91mDo you want to install repositories? (y/n): \033[0m").lower()
    # Ask the user whether they want to install repositories and convert their input to lowercase
    
    if user_input_repos == 'y':
        # If the user's input is 'y':
        
        # Call the function to clone repositories
        clone_repositories(repositories)
        # Invoke the function to clone repositories based on the 'repositories' dictionary
        
    else:
        print("Skipping repository installation.")
        # If the user's input is not 'y', print a message indicating that repository installation is skipped

elif user_input == '2':
    # If the user input is '2':
    
    user_input_update = input("\033[91mDo you want to update the package list? (y/n): \033[0m").lower()
    # Ask the user whether they want to update the package list and convert their input to lowercase
    
    if user_input_update == 'y':
        # If the user's input is 'y':
        
        # Update the package list using 'sudo apt update' command
        subprocess.run(['sudo', 'apt', 'update'])
        # Runs the command to update the package list
        
    else:
        print("Skipping package list update.")
        # If the user's input is not 'y', print a message indicating that package list update is skipped

elif user_input == '3':
    # If the user input is '3':
    
    user_input_requirements = input("\033[91mDo you want to install requirements.txt? (y/n): \033[0m").lower()
    # Ask the user whether they want to install requirements.txt and convert their input to lowercase
    
    if user_input_requirements == 'y':
        # If the user's input is 'y':
        
        # Install requirements from requirements.txt using 'pip install -r requirements.txt' command
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
        # Runs the command to install requirements from requirements.txt
        
    else:
        print("Skipping requirements installation.")
        # If the user's input is not 'y', print a message indicating that requirements installation is skipped

elif user_input == '4':
    # If the user input is '4':
    
    user_input_languages = input("\033[91mDo you want to install all available languages? (y/n): \033[0m").lower()
    # Ask the user whether they want to install all available languages and convert their input to lowercase
    
    if user_input_languages == 'y':
        # If the user's input is 'y':
        
        # Install various programming languages and development tools
        subprocess.run(['sudo', 'apt', 'install', 'perl', 'ruby-full', 'haskell-platform', 'nim', 'dart', 'crystal', 'nodejs', 'default-jdk', 'golang-go', 'torsocks', 'libssl-dev', 'libffi-dev', 'libpcap-dev', 'libnet1-dev', 'libnetfilter-queue-dev', 'libnfnetlink-dev', 'libnftnl-dev', 'libmnl-dev', 'libjansson-dev', 'libdumbnet-dev', 'libbsd-dev'])
        # Runs the command to install a list of programming languages and related development tools
        
    else:
        print("Skipping languages installation.")
        # If the user's input is not 'y', print a message indicating that languages installation is skipped

elif user_input == '5':
    # If the user input is '5':
    
    user_input_phoneinfoga = input("\033[91mDo you want to install PhoneInfoga? (y/n): \033[0m").lower()
    # Ask the user whether they want to install PhoneInfoga and convert their input to lowercase
    
    if user_input_phoneinfoga == 'y':
        # If the user's input is 'y':
        
        # Install PhoneInfoga using a bash command retrieved from a GitHub repository
        os.system('bash <( curl -sSL https://raw.githubusercontent.com/sundowndev/phoneinfoga/master/support/scripts/install )')
        # Executes a bash command to install PhoneInfoga
        
    else:
        print("Skipping PhoneInfoga installation.")
        # If the user's input is not 'y', print a message indicating that PhoneInfoga installation is skipped
        
elif user_input == '6':
    # If the user input is '6':
    
    user_input_nexmo = input("\033[91mDo you want to download Nexmo-CLI? (y/n): \033[0m").lower()
    # Ask the user whether they want to download Nexmo-CLI and convert their input to lowercase
    
    if user_input_nexmo == 'y':
        # If the user's input is 'y':
        
        # Download Nexmo-CLI using wget
        os.system('wget https://github.com/Nexmo/nexmo-cli')
        # Executes a command to download Nexmo-CLI using wget
        
    else:
        print("Skipping Nexmo-CLI download.")
        # If the user's input is not 'y', print a message indicating that Nexmo-CLI download is skipped
        
elif user_input == '7':
    # If the user input is '7':

	user_input_burp_install = input("\033[91mDo you want to download and install BurpSuite? (y/n): \033[0m").lower()
    # Ask the user whether they want to download and install BurpSuite and convert their input to lowercase

	if user_input_burp_install == 'y':
        # If the user's input is 'y':

        # Download BurpSuite from its URL
		os.system('wget https://portswigger.net/burp/releases/download?product=community&version=2021.7.1&type=linux')
        # Downloads BurpSuite Community Edition (you might want to update the URL with the latest version)

        # Extract the downloaded file (assuming it's a zip file)
		os.system('unzip download\?product\=community\&version\=2021.7.1\&type\=linux')
        # Replace 'download\?product\=community\&version\=2021.7.1\&type\=linux' with the actual downloaded file name

        # Move BurpSuite to a suitable directory (you might want to adjust the directory)
		os.system('sudo mv burpsuite_community /opt/')
        # Replace 'burpsuite_community' with the actual folder name of the extracted BurpSuite

		print("BurpSuite has been downloaded and installed successfully.")
        # Display a message confirming successful installation

	else:
		print("Skipping BurpSuite download and installation.")
        # If the user's input is not 'y', print a message indicating that BurpSuite download and installation are skipped

if user_input == '8':
    # If the user input is '8':
    
    print("\033[96mAvailable Repositories:\033[0m")
    # Display a header for the available repositories
    
    for repo_name in repositories:
        print(f"\033[91m- {repo_name}\033[0m")
    # Iterate through the repository names and print each one
        
    user_input_repo = input("\033[91mPlease enter the name of the repository you want to navigate into: \033[0m")
    # Ask the user to enter the name of the repository they want to navigate into
    
    if user_input_repo in repositories:
        # If the entered repository name exists in the 'repositories' dictionary:
        
        repo_url = repositories[user_input_repo]
        # Get the URL of the selected repository from the 'repositories' dictionary
        
        clone_repository(repo_url)
        # Clone the selected repository
        
        os.chdir(user_input_repo)  # Change directory to the selected repository
        # Change the current working directory to the selected repository
        
    else:
        print("Repository not found.")
        # If the entered repository name doesn't exist in the 'repositories' dictionary, print a message
        
elif user_input == '9':
    # If the user input is '9':
    
    user_input_burp = input("\033[91mDo you want to open BurpSuite? (y/n): \033[0m").lower()
    # Ask the user whether they want to open BurpSuite and convert their input to lowercase
    
    if user_input_burp == 'y':
        # If the user's input is 'y':
        
        # Open BurpSuite
        subprocess.run(['burpsuite'])
        # Runs the command to open BurpSuite
        
    else:
        print("Skipping BurpSuite.")
        # If the user's input is not 'y', print a message indicating that BurpSuite is skipped
        
elif user_input == '10':
    # If the user input is '10':
    
    user_input_nmap = input("\033[93mPlease enter the website URL or IP address you want to perform the nmap test on: \033[0m")
    # Ask the user to enter a website URL for the nmap test
    
    # Perform the nmap test on the entered website URL
    subprocess.run(['nmap', '-sV', user_input_nmap])
    # Runs the command to perform an nmap test with service version detection on the entered website URL
    
elif user_input == '11':
    # If the user input is '11':
    
    # Display available security tools
    print("\033[96mAvailable Security Tools:\033[0m")
    print("\033[93m1. John the Ripper\033[0m")
    print("\033[93m2. Homebrew (Mac/Linux)\033[0m")
    print("\033[93m3. Lynis\033[0m")
    print("\033[93m4. Metasploit\033[0m")
    print("\033[93m5. SQLMap\033[0m")
    print("\033[93m6. Nikto\033[0m")
    # Prints a list of available security tools for the user to view


# Ask the user to input a number corresponding to the security tool they want to install
user_input_security = input("\033[96mPlease enter the number of the security tool you want to install: \033[0m")

# Check the user's input and execute commands accordingly based on their choice
if user_input_security == '1':
    # If the user input is '1':
    
    # Install 'John the Ripper' tool using 'apt-get'
    subprocess.run(['sudo', 'apt-get', 'install', 'john', '-y'])
    
elif user_input_security == '2':
    # If the user input is '2':
    
    # Install 'Homebrew' using 'apt'
    subprocess.run(['sudo', 'apt', 'install', 'snapd'])
    
elif user_input_security == '3':
    # If the user input is '3':
    
    # Install 'Lynis' using a bash script from GitHub via curl
    subprocess.run(['/bin/bash', '-c', "$(curl -fsSL https://raw.githubusercontent.com/CISOfy/lynis/master/contrib/install.sh)"])
    
elif user_input_security == '4':
    # If the user input is '4':
    
    # Install 'Metasploit' using curl to retrieve the installation script and execute it
    subprocess.run(['curl', 'https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb', '>', 'msfinstall'])
    subprocess.run(['chmod', '755', 'msfinstall'])
    subprocess.run(['./msfinstall'])
    
elif user_input_security == '5':
    # If the user input is '5':
    
    # Clone 'SQLMap' repository from GitHub
    subprocess.run(['git', 'clone', '--depth', '1', 'https://github.com/sqlmapproject/sqlmap.git', 'sqlmap-dev'])
    
elif user_input_security == '6':
    # If the user input is '6':
    
    # Clone 'Nikto' repository from GitHub
    subprocess.run(['git', 'clone', 'https://github.com/sullo/nikto.git'])
   

