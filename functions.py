# Imports subprocess
import subprocess

# Imports GingerIt
from gingerit.gingerit import GingerIt

# Function to install GingerIt. To be run once for user
def install_gignerit():

	# Updates pip and instals gingerit
	subprocess.run('python -m pip install --upgrade pip')
	p = subprocess.run('pip install gingerit')


# Function to check spelling of the output
# Takes in generated output, corrects and returns corrected text
def check_spelling(generated_text):
    
    parser = GingerIt()
    changed_text = parser.parse(generated_text)
    
    changed_text = changed_text["result"]
    return changed_text
 


#CHECKS
install_gignerit()

generated_text = input("Sentences to check: \n")
print(check_spelling(generated_text))


