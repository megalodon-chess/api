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
import json
import pysocket

PARENT = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.join(PARENT, "data")
with open(os.path.join(PARENT, "ip.txt")) as file:
    IP = file.read().strip()


def start(self: pysocket.server.Client):
    cmd = self.recv()

    if cmd["type"] == "getbuildinfo":
        if os.path.isfile(os.path.join(DATA_PATH, "buildbot-info.json")):
            with open(os.path.join(DATA_PATH, "buildbot-info.json"), "r") as file:
                data = json.load(file)
            self.send({"success": True, "data": data})
        else:
            self.send({"success": False})

    elif cmd["type"] == "getbuild":
        if os.path.isfile(os.path.join(DATA_PATH, "buildbot-Megalodon")):
            with open(os.path.join(DATA_PATH, "buildbot-Megalodon"), "rb") as file:
                data = file.read()
            self.send({"success": True, "data": data})
        else:
            self.send({"success": False})


def main():
    server = pysocket.Server(IP, 5050, start, b"9s5i6cZEmRp_P91LwrLebemgzPNhQsiQLHZAr1849Ec=")
    server.start()


main()
