import platform
import sys
import os
from typing import Optional, Tuple


class Utils:
	@staticmethod
	def open_text_file(filename):
		""" Open file in read mode """
		f = open(filename, 'r', encoding='utf-8')
		res = f.read()
		f.close()
		return res


	@staticmethod
	def open_variable_file(filename):
		""" Open file in read mode, store rows in a list """
		f = open(filename, 'r', encoding='utf-8')
		res = f.readlines()
		f.close()
		return res


	@staticmethod
	def save_variable_file(filename, list_var):
		""" Save the data: bible, book and chapter in the text file """
		f = open(filename, 'w', encoding='utf-8')
		for i in list_var:
			f.writelines(str(i) + '\n') 
		f.close()


	def platform_system_desc(self):
		""" Get operating system description """
		if platform.system() == "Linux":
			try:
				system_desc = os.name
			except ImportError:
				system_desc = "Linux"
			if "32" not in system_desc and "64" not in system_desc:
				system_desc += " " + self.get_os_architecture_number()
		else:
			system_desc = (platform.system() + " " + platform.release() + " " + self.get_os_architecture_number())
		return system_desc


	@staticmethod
	def get_os_architecture_number():
		""" Get operating system architecture number """
		if "32" in platform.machine() and "64" not in platform.machine():
			return "(32-bit)"
		elif "64" in platform.machine() and "32" not in platform.machine():
			return "(64-bit)"
		else:
			return ""


	@staticmethod
	def get_python_version_string(version_info: Optional[Tuple] = None) -> str:
		""" Get Python version """
		if version_info is None:
			version_info = sys.version_info
		result = ".".join(map(str, version_info[:3]))
		if version_info[3] != "final":
			result += "-" + version_info[3]
		result += " (" + ("64" if sys.maxsize > 2 ** 32 else "32") + "-bit)"
		return result