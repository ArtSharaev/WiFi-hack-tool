from subprocess import Popen, PIPE
import os
import csv


def take_password(name: str):
    password = ""
    mas_not_formated: list = [line.decode('cp866', 'ignore')
                              for line in Popen(
            ["powershell", f"netsh wlan show profiles \"{name}\" key=clear"],
            stdout=PIPE).stdout.readlines()]
    for line in mas_not_formated:
        if ("Key Content" in line) or ("Содержимое ключа" in line):
            password = line.split(":")[1]

    return password.strip()


mas_not_formated: list = [line.decode("cp866", "ignore") for line in
                          Popen(["powershell", f"netsh wlan show profiles"],
                                stdout=PIPE).stdout.readlines()]

print(f"\033[94mWi-Fi hack tool by prok0l and ArtSharaev\033[94m")
print()
writing_file = open("passwords.csv", mode="a", encoding="utf-8")
file_writer = csv.writer(writing_file, delimiter=";")
for i in range(9, len(mas_not_formated) - 1, 1):
    wifi_name = mas_not_formated[i].split(":")[1].strip("\n").strip()
    wifi_password = take_password(wifi_name)
    file_writer.writerow([wifi_name, wifi_password])
    p = " " * (40 - len(wifi_name))
    print(f"\033[92m{wifi_name}\x1b[m{p}\033[91m{wifi_password}\x1b[m")
writing_file.close()

os.system("cmd.exe")
