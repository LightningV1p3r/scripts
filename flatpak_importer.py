import subprocess
import shlex
import json

def execute_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    stdout, stderr = process.communicate()
    return_code = process.poll()
    return stdout


def install_flatpak_by_id(flatpak_id):
    command = f"flatpak install -y flathub {flatpak_id}"
    print(execute_command(command))


def main():
    with open("flatpak_id_list.json", "r") as f:
        id_list = json.loads(f.read())

    for flatpak_id in id_list:
        install_flatpak_by_id(flatpak_id)


if __name__ == "__main__":
    main()
