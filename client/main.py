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
import pysocket
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename
Tk().withdraw()

IP = input("IP: ")


def main():
    if not len(sys.argv) > 1:
        print("Please provide an argument.")

    conn = pysocket.Client(IP, 5555, b"9s5i6cZEmRp_P91LwrLebemgzPNhQsiQLHZAr1849Ec=")
    if sys.argv[1] == "getbuild":
        conn.send({"type": "getbuild"})
        data = conn.recv()
        if data["success"]:
            with open(asksaveasfilename(), "wb") as file:
                file.write(data)
        else:
            print("Server error. Please try again later.")


main()
