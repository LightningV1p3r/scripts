import subprocess
import shlex
import json
import re

regex_pattern_app_ids = r"\b[a-z]+(?:\.[a-z]+)+\.[a-zA-Z0-9_]+\b"
ignore_list = [
	"org.freedesktop.Platform",
	"org.freedesktop.Sdk",
	"org.gnome.Platform",
	"org.kde.Platform",
	"org.kde.PlatformTheme",
	"org.kde.WaylandDecoration",
	"org.gnome.design",
	"org.gnome.design.AppIconPreview",
	"org.gnome.design.Emblem",
	"org.gnome.design.IconLibrary",
	"org.gnome.design.Palette",
	"org.gnome.design.SymbolicPreview",
	"org.winehq.Wine"
]

def get_app_ids():
	command = "flatpak list"
	return execute_command(command)


def filter_app_ids(id_list_raw: str) -> list:
	result = re.findall(regex_pattern_app_ids, id_list_raw)
	id_list = []

	for id in result:
		if id in ignore_list:
			continue
		id_list.append(id)

	return id_list


def export_to_file(id_list: list):
	with open("flatpak_id_list.json", "w") as f:
		f.write(json.dumps(id_list))


def execute_command(command):
	process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
	stdout, stderr = process.communicate()
	return_code = process.poll()
	return stdout

def main():
	id_list_raw = get_app_ids()
	id_list = filter_app_ids(id_list_raw)
	export_to_file(id_list)


if __name__ == '__main__':
	main()
