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

import sys
import os
import time
import json
import pysocket
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename
Tk().withdraw()

PARENT = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(PARENT, "ip.txt")) as file:
    IP = file.read().strip()


def main():
    if not len(sys.argv) > 1:
        print("Please provide an argument.")
        return

    conn = pysocket.Client(IP, 5050, b"9s5i6cZEmRp_P91LwrLebemgzPNhQsiQLHZAr1849Ec=")
    if sys.argv[1] == "getbuild":
        conn.send({"type": "getbuild"})
        data = conn.recv()
        if data["success"]:
            path = asksaveasfilename()
            with open(path, "wb") as file:
                file.write(data["data"])
            os.system(f"chmod +x {path}")
        else:
            print("Server error. Please try again later.")

    elif sys.argv[1] == "getbuildinfo":
        conn.send({"type": "getbuildinfo"})
        data = conn.recv()
        if data["success"]:
            print(json.dumps(data["data"], indent=4))
        else:
            print("Server error. Please try again later.")

    elif sys.argv[1] == "lag":
        start = time.time()
        conn.send({"type": "ping"})
        data = conn.recv()
        if data["success"]:
            print(f"Lag: {int(1000*(time.time()-start))} milliseconds.")
        else:
            print("Server error. Please try again later.")


main()
