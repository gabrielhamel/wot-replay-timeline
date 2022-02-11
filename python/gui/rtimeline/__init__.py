
__author__ = "Gabouchet"
__copyright__ = "Copyright 2022, Gabouchet"
__credits__ = ["Gabouchet"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Gabouchet"
__email__ = "gabriel.hamel.pro@gmail.com"
__status__ = "Production"

import logging
_logger = logging.getLogger(__name__)

__all__ = ('init', 'fini')

def init():
    _logger.log("ISSOU GANG init()")

def fini():
	_logger.log("ISSOU GANG fini()")
