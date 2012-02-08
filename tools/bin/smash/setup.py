#!/usr/bin/env python
# setup.py - smash installation script
# Copyright (C) 2008, 2009 Zilogic Systems
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

from distutils.command.sdist import sdist
import shutil

from smashlib.smash import __version__

class rp_sdist(sdist):
    def run(self):
        """Before building the source distribution, we would like to
        have required resource modules generated and the __init__.py
        nuked."""
        
        d = "smashlib/resources/"
        from smashlib.resources import smash_glade
        # Nuke smashlib/resources/__init__.py
        file(d + "__init__.py", "w")
        ret = sdist.run(self)
        shutil.copyfile("rpinit.py", d + "__init__.py")
        return ret

setup(name = "smash",
      version = __version__,
      description = "8051 micro-controller ISP tool",
      author = "Vijay Kumar",
      author_email = "vijaykumar@zilogic.com",
      license = "GPLv3",
      url = "http://www.zilogic.com/smash/",
      packages = ['smashlib', 'smashlib.resources'],
      scripts = ["smash", "smash-gui"],
      long_description = """
Smash is an 8051 microcontroller In-System Programming (ISP) tool, for
Philips and NXP microcontrollers.
""",
      cmdclass = {"sdist": rp_sdist},
      )

