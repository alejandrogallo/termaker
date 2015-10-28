#! /usr/bin/env python
import sys;
class TerminalApp(object):
	"""docstring for TerminalApp"""
	
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






	def newAppMode(self):
		if self.flagOn(self.newAppFlag):
			filePath = self.getValueOfFlag(self.newAppFlag);
			if len(filePath.split("."))==1:
				filePath += ".py";
			else:
				print("Please write the file without any extension");
				self.quit();
			print("Creating a new model for a terminal app");
			f = open(filePath,"w");
			f.write("import terminalApp\n\n\n");
			f.write("class MyAppTerminalApp(terminalApp.TerminalApp):\n");
			f.write("\tdef __init__(self):\n");
			f.write("\t\tsuper(MyAppTerminalApp, self).__init__();\n");
			f.write("\t\tself.appName = 'myapp';\n");
			f.write("\t\tself.version = '0.0';\n");
			f.write("\t\t## Define your custom flags\n");
			f.write("\t\t#self.myNewFlag=['--hello','-world']\n");
			f.write("\n\n\n\"\"\"\t def myNewFlagMode(self):\n\t\t#define your new flag method \n");
			f.write("\t\t if self.flagOn(self.myNewFlagMode):\n");
			f.write("\t\t\t #do something with the information, for example get the value\n");
			f.write("\t\t\t flagValue = self.getValueOfFlag(self.myNewFlag);\"\"\"\n");
			f.write("\n\n\n");
			f.write("\tdef init(self):\n\t\t#initialise the parent init() method\n");
			f.write("\t\tparent(MyAppTerminalApp,self).init();\n");
			f.write("\t\t#self.myNewFlagMode();\n");
			f.close();
			print("Model created at %s"%filePath);


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
		#checking if we are initializing a new app
		self.newAppMode();



if __name__=="__main__":
	app = TerminalApp();
	app.init();



