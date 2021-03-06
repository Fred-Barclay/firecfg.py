# Copyright © 2020 rusty-snake
#
# This file is part of firecfg.py
#
# firecfg.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# firecfg.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from os import listdir, unlink
from os.path import realpath

class CleanSymlinks:
    FIREJAIL_EXEC = "/usr/bin/firejail"
    BINDIR = "/usr/local/bin/"

    def clean(self):
        for file in listdir(CleanSymlinks.BINDIR):
            symlink = CleanSymlinks.BINDIR + file
            if realpath(symlink) == CleanSymlinks.FIREJAIL_EXEC:
                print("Removing", symlink)
                unlink(symlink)


if __name__ == "__main__":
    CleanSymlinks().clean()
