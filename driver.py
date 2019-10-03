from selenium import webdriver
import os
from tempfile import mkstemp
from os import fdopen, remove


os.environ.setdefault("_SETTINGS_MODULE","server.settings")



############################################################################################################################################################
# Construction of projects directories/paths.
#
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
APPLICATION_DIR = os.path.join(BASE_DIR, 'Courses')
PROJECT_DIR = os.path.join(BASE_DIR, 'linuxjobber')
PROJECT_MEDIA_DIR = os.path.join(BASE_DIR, 'media'+ '\\uploads') # Directory that contains projects media
MEDIA_DIR = os.path.join(APPLICATION_DIR, 'media') #Directory that contains media exclucive to DjangoLabs Application

############################################################################################################################################################


#--------------------------------------------------------------------------------------------------------
#FUNCTIONS
#--------------------------------------------------------------------------------------------------------
def replace(file_path, pattern, subst):
	fh, abs_path = mkstemp()
	with fdopen(fh,'w') as new_file:
		with open(file_path) as old_file:
			for line in old_file:
				new_file.write(line.replace(pattern,subst))
	remove(file_path)
	move(abs_path, file_path)


#-------------------------------------------------------------------------------------------------------





# os.chdir(r"C:\Users\Louis\LinuxjobberWorkSpace\work area\staticscrumy\staticscrumy")
# replace(r'C:\Users\Louis\LinuxjobberWorkSpace\work area\staticscrumy\staticscrumy\settings.py', 'INSTALLED_APPS = [', "INSTALLED_APPS = [\n    '"+branch_name+"',")
# replace(r'C:\Users\Louis\LinuxjobberWorkSpace\work area\staticscrumy\staticscrumy\urls.py', 'urlpatterns = [', "urlpatterns = [\n    path('"+branch_name+"', include('"+branch_name+".urls')),")


# driver = webdriver.Chrome("C:\PythonProject\chromedriver.exe")

# driver.get("http://127.0.0.1:8000/riasec/contact")

# html = driver.execute_script("return document.body.innerHTML;")
# if html:
# 	print('Pass' + BASE_DIR + APPLICATION_DIR )
# else:
# 	print('Fail' + BASE_DIR + APPLICATION_DIR)

# print (html)

print (BASE_DIR)
print (APPLICATION_DIR)