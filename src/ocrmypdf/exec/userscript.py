# © 2020 Heinrich Ulbricht: github.com/heinrich-ulbricht
#
# This file is part of OCRmyPDF.
#
# OCRmyPDF is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OCRmyPDF is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with OCRmyPDF.  If not, see <http://www.gnu.org/licenses/>.

"""Interface to user-provided shell script execution"""

from functools import lru_cache
from subprocess import run, call
from shutil import which

@lru_cache(maxsize=1)
def version():
    return "1"


def available():
    return True

def runscript(input_file, output_file, userscriptpath, log):
    if which(userscriptpath) is not None:
        args = [
            userscriptpath,
            input_file,
            output_file,
        ]
        log.debug("Calling script " + userscriptpath)
        call(args)
        log.debug("Done: Calling script " + userscriptpath)
    else:
        log.info("User script could not be found, skipping execution: " + userscriptpath)
