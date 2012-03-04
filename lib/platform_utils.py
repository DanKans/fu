""" 
		Platform Interface utility
			
"""

import subprocess
import commands
import platform

class system:

		def __init__(self):
				
				info = set( [ ss.lower() for ss in platform.uname() ])
				
				# determine the type of platform
				if 'darwin' in info:
						self.name = 'mac'
						self.copy_command = 'pbcopy';
#						self.exec_command = '';
				elif 'cygwin' in info.lower():
						self.name = 'windows'
						self.copy_command = 'clip';
				else :
						self.name = 'linux'
						self.copy_command = 'xclip -selction clipboard';

		"""Copy given string into system clipboard."""
		def copy(self,string):

				# Assuming it works, we try and execute the function
				worked = True
				try:
						subprocess.Popen([self.copy_command], stdin=subprocess.PIPE).communicate(str(unicode(string)))
				except Exception, why:

						# If it doesn't work return flase
						worked = False
#						print "%s: %s. The %s command failed" % ( color.cyan('cfu'), color.red('ERROR'), self.copy_command ) 
				return worked
			 
		def paste(self):
				"""Returns system clipboard contents."""
				try:
						return unicode(commands.getoutput('pbpaste'))
				except Exception, why:
						raise XcodeNotFound
