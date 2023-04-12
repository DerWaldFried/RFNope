import os
from rich.console import Console
from rich.theme import Theme


custom_theme = Theme({
        "info": "dim cyan",
        "warning": "magenta",
        "danger": "bold red"
    })

console = Console(theme=custom_theme)
console.print("[warning]RFNope[/warning]")
console.print("This Software will Block the German RundFunk and his Services!", style="danger")

console.print("Enter [warning]YES[/warning] when you want Block all Websites and Services!\n")
console.print(" Type NO when you want do delete the Block of all Rundfunk Services\n")
accept = console.input()

# When User Choose YES
if accept == "YES":
    if os.name == "nt":
        from ntsys import ntblocker
        console.print("NTBLocker will called")
        ntblocker()
    else:
        from pssys import psblocker
        console.print("PSBlocker will called")
        psblocker()

# When User Choose NO
if accept == "NO":
    if os.name == "nt":
        from ntsys import ntdeblocker
        ntdeblocker()
    else:
        from pssys import psdeblocker
        psdeblocker()

else:
    console.print("You Dont have Choose YES or NO. The Software has do nothing")
