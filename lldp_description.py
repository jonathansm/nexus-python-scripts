#!/usr/bin/env python

"""
This will take the LLDP names and add a description to the interfaces
with the names from LLDP. Can be ran once or added to a schedule.

You can run the script with a -v option to give feed back as it applies the description

"""

from __future__ import print_function
try:
    from cli import cli
except ImportError:
    from cisco import cli
import sys
import json
import argparse

# Handle cli() type inconsistencies this is for the 3000 series
def make_cli_wrapper(f):
    if type(f("show clock")) is tuple:
        def cli_wrapper(*args, **kwargs):
            return f(*args, **kwargs)[1]
        return cli_wrapper
    return f

cli = make_cli_wrapper(cli)

parser = argparse.ArgumentParser(
    description='Add LLDP names to the connected interface descriptions'
)
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()

verboseprint = print if args.verbose else lambda *a, **k: None

verboseprint("Getting LLDP Neighbors")
data = json.loads(cli('show lldp neighbors | json'))

for key in data["TABLE_nbor"]["ROW_nbor"]:
		verboseprint("Applying interface description to " + key["l_port_id"])
        cliCommand = "configure terminal ; interface " + key["l_port_id"] + " ; description " + key["chassis_id"]
        cli(cliCommand)

verboseprint("Done. I will now exit")
sys.exit
