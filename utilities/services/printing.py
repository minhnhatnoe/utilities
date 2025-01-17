from gevent import monkey
monkey.patch_all()

import subprocess

from utilities.config import ServiceCoord

from .base import Service
from .rpc import rpc_method


class PrintingService(Service):
    @rpc_method
    def print(self, source):
        print("Printing")
        subprocess.Popen(f'lpr -o media=A4 -o prettyprint -o page-border=single -o fit-to-page {source}')
