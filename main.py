import uuid #This can create uniq strings for files
import requests #This helps to connect internet to send requests
import os # This accessing to syscall  lib
import hashlib # This is for Hash algorithm



ImageDir="images"  # Define a directory to save images


if not os.path.exists(ImageDir): # if directory not exist, create a directory that define above
    os.makedirs(ImageDir)

def download_file(url, file_name=None): # This is  original download function
	r = requests.get(url, allow_redirects=True)
	file = file_name if file_name else str(uuid.uuid4())
	open(os.path.join(ImageDir,file), 'wb').write(r.content) # Creatin images in /Images directory


def checkSumTest(): # This is hash function to create file and check if it's uniq or not
	uniqHash=[]  # This is  list where we can store uniq ones to compare others
	for file in os.listdir(ImageDir): # Iterating files in ImageDirectory that define above
		if hashlib.md5(open(os.path.join(ImageDir,file),'rb').read()).hexdigest() not in uniqHash: #First step check if hash value is stored before or not
			uniqHash.append(hashlib.md5(open(os.path.join(ImageDir,file),'rb').read()).hexdigest()) # This step add uniq hash value into list
		else:
			print("This file is duplicate in hash output >> "+file) # Printing Error for duplicate ones
	print("\n This files are uniq >>\n")
	print(uniqHash) #Printing uniq files's hash values

urls =[ # Our url list is here
"http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
"https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024pxHawai%27i.jpg",
"http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024pxHawai%27i.jpg"
]

def getFiles(): # Trigger function for download files
	for url in urls:
		download_file(url)

def createChildProcess(): # This is  where we create a system call 'fork' to make a child process 
   n = os.fork()
   if n > 0: # First child process always numbered as 0
	print("Parent process PID is : ", os.getpid())
	os.wait() # Preventing/Avoidind orphan process
   else:
	print("Child proces PID is: ", os.getpid()) # This step where the child process is begin, so we are calling our functions here to use "Child Process"
	getFiles() #Download Files
	checkSumTest() # Check the uniq files
	print("Child process end") # To show where the child process is end.




createChildProcess() # And this is the main function  to trigger everytthing
