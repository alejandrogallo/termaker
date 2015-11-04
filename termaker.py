import sys



class Flag(object):
	def __init__(self, flagNames, order=False, kwarg = False):
		self.flagNames = self.initFlagNames(flagNames)
		self.order = order
	def initFlagNames(self, flagNames):
		if not type(flagNames) is list:
			return [flagNames]
		else:
			return flagNames
	def setOrder(self, order):
		self.order = order


class FlagHandler(object):
	"""docstring for FlagHandler"""
	def __init__(self, flags, function, docstring="", strictMode = False):
		super(FlagHandler, self).__init__()
		self.flags = flags
		self.function = function 
		self.docstring = docstring
		self.arguments = []
		self.flagsGotten = 0

	def searchInFlagNames(self, name):
		for flag in self.flags:
			if name in flag.flagNames:
				return flag
		return False

	def parse(self, argv):
		for i in range(len(argv)):
			flag = self.searchInFlagNames(argv[i])
			if flag:
				self.flagsGotten+=1
				if argv[i+1]:
					if not self.searchInFlagNames(argv[i+1]):
						pass


	def run(self):
		
		


class TerminalApp(object):
	"""Instantiate this"""
	def __init__(self):
		super(TerminalApp, self).__init__();
		self.argv = self.getArgv();
		self.appName = "TerminalApp";
		self.version = "0.1";
		#SOME DEFAULT FLAGS AND DEFINITIONS
		self.fileInFlag = ["-f","--file","--in"];
		self.fileOutFlag = ["--out"];
		self.helpFlag = ["--help","-h","?"];
		self.verbatim = False;
		self.verbatimFlag="-v";
		#to create a model for future applications
		self.newAppFlag = "new";


	
	def printFlags(self):
		for field in vars(self):
			if "flag" in field.lower():
				print(getattr(self, field));
	def printUsage(self):
		usageText = self.appName+":Usage: "+self.appName+" ";
		print(usageText);
		self.printFlags();
	def printHelp(self):
		self.printUsage();
		helpText="";
		print(helpText);


	def getArgv(self):
		#here we put all --foo=bar in separate form --foo , bar, so that we can treat everything together
		argv = sys.argv;
		transformedArgv = []; 
		for arg in argv:

			split = arg.replace(" ","").split("=");
			transformedArgv+=split;
		return transformedArgv;



	def argvIsEmpty(self):
		if len(self.argv)==1:
			self.printUsage();
			return True;
		else:
			return False;
	def checkIfArgvIsEmpty(self):
		#like argvIsEmpTy but exits if it's the case (for applications that need arguments)
		if self.argvIsEmpty(self):
			self.quit();
	def quit(self):
		print("Exiting "+self.appName);
		sys.exit(0);
	
	



	def flagOn(self,flags):
		"""This just checks if a flag is on, to use for flags that do not need a value 
		e.g. -h for help and not for input files etc.."""
		"""The input (flags) can be either a list of flags or a string"""
		if not type(flags) is list:
			flags = [flags];
		for flag in flags:
			if flag in self.argv:
				return True;
		return False;
	def getValueOfFlag(self,flags):
		"""To use for flags that need a value e.g. --file=foo/bar.jpg or -f foo/bar.jpg """
		"""If there is no value to be read, it exists the program. """
		if not type(flags) is list:
			flags = [flags];
		for flag in flags:
			if flag in self.argv:
				index  = int(self.argv.index(flag));
				if len(self.argv)>(index+1):
					flagValue = self.argv[index+1];
					if self.verbatim:
						print("Value of %s is %s"%(flag,flagValue));
					return flagValue;
				else:
					print("Error in flag %s"%flag);
					self.printUsage();
					self.quit();


 	def helpMode(self):
 		""" in help mode one quits after presenting the information """
 		if self.flagOn(self.helpFlag):
 			self.printHelp();
 			self.quit();
	def verbatimMode(self):
		if self.flagOn(self.verbatimFlag):
			self.verbatim=True;
			print("Entering verbatim mode.");
			return True;
		else:
			self.verbatim=False;
			return False;

	def init(self):
		print(self.appName+": version "+self.version+"\nEntering in terminal mode:\n");
		#checking for verbatim mode
		self.verbatimMode();
		#checking for help mode
		self.helpMode();
	
	
	def addFlag(flagNames, flagFunction, argument=False, docstring=""):
		pass
	def addCommand(commandName, commandFunction, argument=False, docstring = ""):
		pass
