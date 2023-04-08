import os
from rich.console import Console
import bweb


class PSBlocker:
    # change hosts path according to your OS
    hosts_path = r'C:\Windows\System32\drivers\etc\hosts'

    console = Console

    console.print("You have accepted with [warning]YES[/warning], we will now Block")
    # Open Host Data in Write mode
    with open(hosts_path, 'a') as hosts_file:

        # We Block now all Sites
        for url in bweb.blocked_urls:
            hosts_file.write('127.0.0.1 {}\n'.format(url))

    # Reload the DNS-Cache to load blocked List
    os.system('ipconfig /flushdns')
