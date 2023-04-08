import os
import bweb
from rich.console import Console
from rich.theme import Theme

import ntsys
import pssys

# change hosts path according to your OS
hosts_path = r'C:\Windows\System32\drivers\etc\hosts'

custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red"
})
console = Console(theme=custom_theme)
console.print("[warning]RFNope[/warning]")
console.print("This Software will Block the German RundFunk and his Services!", style="danger")

accept = console.input("Enter [warning]YES[/warning] when you want Block all Websites and Services!"
                       "Type NO when you want do delete the Block of all Rundfunk Services\n")
# When User Choose YES
if accept == "YES":
    if os.name == "nt":
        ntsys.NTBlocker()
    if os.name == "posix":
        pssys.PSBlocker()

# When User Choose NO
elif accept == "NO":
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
else:
    console.print("You Dont have Choose YES or NO. The Software has do nothing")
