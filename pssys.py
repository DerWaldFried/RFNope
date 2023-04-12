import os

import pyuac
from rich.console import Console
import bweb


def psblocker():
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:
        # change hosts path according to your OS
        hosts_path = r'/etc/hosts'

        console = Console()

        console.print("You have accepted with [warning]YES[/warning], we will now Block")
        # Open Host Data in Write mode
        with open(hosts_path, 'a') as hosts_file:

            # We Block now all Sites
            for url in bweb.blocked_urls:
                hosts_file.write('127.0.0.1 {}\n'.format(url))

        # Reload the DNS-Cache to load blocked List
        os.system('ipconfig /flushdns')


def psdeblocker():
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:
        hosts_path = r'/etc/hosts'
        console = Console()

        console.print("You have Choose NO. The Software will now delete all Blocked Website and Services")
        # Reading the Content of Host Data in Write mode
        with open(hosts_path, 'r') as hosts_file:
            hosts_contents = hosts_file.readlines()

        # Writing new Host Data without blocking
        with open(hosts_path, 'w') as hosts_file:
            for line in hosts_contents:
                if not any(url in line for url in bweb.blocked_urls):
                    hosts_file.write(line)
        os.system('ipconfig /flushdns')
