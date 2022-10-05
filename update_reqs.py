# this file reads the file csv_tools.py and updates the requirements.txt file with the packages used in the file using the pipreqs module
import os

os.system("python -m pipreqs.pipreqs " + (os.getcwd()) + " --force")


#!information concerning THIS file:

##?This file is taken from https://gist.github.com/SpotlightForBugs/fbdc39a62417eaf09d528e3ba4d62093
##?Feel free to use it in your projects and modify it as you wish, because of the simplicity of the code (there are more comments than code),
##?there is no need to credit me, but it would be nice if you did.


###?license: Do What The Fuck You Want To Public License (WTFPL)
