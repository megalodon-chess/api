#
#  Megalodon API
#  Server and client files for api.
#  Copyright Megalodon Chess 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import os
import time
import json
from datetime import datetime

BUILD_INC = 60   # Minutes
PARENT = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.join(PARENT, "data")
REPO_PATH = os.path.join(PARENT, "megalodon")
URL = "https://github.com/megalodon-chess/megalodon.git"


def main():
    os.makedirs(DATA_PATH, exist_ok=True)
    while True:
        if not os.path.isdir(REPO_PATH):
            os.system(f"git clone {URL} {REPO_PATH}")
        os.chdir(REPO_PATH)
        os.system("git pull")

        os.makedirs(os.path.join(REPO_PATH, "build"), exist_ok=True)
        os.chdir(os.path.join(REPO_PATH, "build"))
        os.system("cmake ..")
        os.system("make")
        os.rename(os.path.join(REPO_PATH, "build", "Megalodon"), os.path.join(DATA_PATH, "buildbot-Megalodon"))
        with open(os.path.join(DATA_PATH, "buildbot-info.json"), "w") as file:
            json.dump({"date": datetime.now().strftime("%m-%d-%Y %H-%M-%S")}, file, indent=4)

        time.sleep(BUILD_INC*60)


main()
