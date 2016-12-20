#!/usr/bin/env python

from __future__ import division
try:
    from cli import cli
except ImportError:
    from cisco import cli
import sys
import json

# Handle cli() type inconsistencies this is for the 3000 series
def make_cli_wrapper(f):
    if type(f("show clock")) is tuple:
        def cli_wrapper(*args, **kwargs):
            return f(*args, **kwargs)[1]
        return cli_wrapper
    return f

cli = make_cli_wrapper(cli)

data = json.loads(cli('show lldp neighbors | json'))

for key in data["TABLE_nbor"]["ROW_nbor"]:
        cliCommand = "conf t ; interface " + key["l_port_id"] + " ; description " + key["chassis_id"]
        cli(cliCommand)
