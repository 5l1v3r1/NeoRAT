import contextlib
import io

from foreign.client_handling.lazagne.config.write_output import StandardOutput
from foreign.client_handling.lazagne.config.constant import constant
from foreign.client_handling.lazagne.config.run import run_lazagne

constant.st = StandardOutput()


def runLaZagne(category_selected='all', subcategories={}, password=None):
	for pwd_dic in run_lazagne(category_selected=category_selected, subcategories=subcategories, password=password):
		yield pwd_dic


def recover():
	with io.StringIO() as stdout, contextlib.redirect_stdout(stdout):
		for r in runLaZagne(): pass
		return {'message': stdout.getvalue().strip()}