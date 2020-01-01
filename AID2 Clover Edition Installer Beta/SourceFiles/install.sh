#!/usr/bin/env bash
set -e
cd "$(dirname "${0}")"
BASE_DIR="$(pwd)"
PACKAGES=(aria2 git unzip wget)
#MIN_PYTHON_VERS="3.4.0"

#version_check () {
#	MAX_VERS=$(echo -e "$(python3 --version | cut -d' ' -f2)\n$MAX_PYTHON_VERS\n$MIN_PYTHON_VERS"\
#	| sort -V | tail -n1)
#	MIN_VERS=$(echo -e "$(python3 --version | cut -d' ' -f2)\n$MAX_PYTHON_VERS\n$MIN_PYTHON_VERS"\
#	| sort -V | head -n1)
#	if [ "$MIN_VERS" != "$MIN_PYTHON_VERS" ]; then
#		echo "Your installed python version, $(python3 --version), is too old."
#		echo "Please update to at least $MIN_PYTHON_VERS."
#		exit 1
#	elif [ "$MAX_VERS" != "$MAX_PYTHON_VERS" ]; then
#		echo "Your installed python version, $(python3 --version), is too new."
#		echo "Please install $MAX_PYTHON_VERS."
#		exit 1
#	fi
#}

pip_install () {
	if [ ! -d "./venv" ]; then
		# Some distros have venv built into python so this isn't always needed.
		if is_command 'apt-get'; then
			apt-get install python3-venv
		fi
		#WARNING: Changing to --copies for colab users, not optimal way to do this
		python3 -m venv --copies ./venv
	fi
	commit_hash=$(git log --pretty=format:'%h' -n 1)
	echo "You are using https://github.com/cloveranon/Clover-Edition/commit/${commit_hash}"
	source "${BASE_DIR}/venv/bin/activate"
	pip install --upgrade pip setuptools
	pip install -r "${BASE_DIR}/requirements.txt"
}

is_command() {
	command -v "${@}" > /dev/null
}

system_package_install() {
	#why is this list duplicated?
	PACKAGES=(aria2 git unzip wget)
	if is_command 'apt-get'; then
		sudo apt-get install ${PACKAGES[@]}
	elif is_command 'brew'; then
		brew install ${PACKAGES[@]}
	elif is_command 'yum'; then
		sudo yum install ${PACKAGES[@]}
	elif is_command 'dnf'; then
		sudo dnf install ${PACKAGES[@]}
	elif is_command 'pacman'; then
		sudo pacman -S ${PACKAGES[@]}
	elif is_command 'apk'; then
		sudo apk --update add ${PACKAGES[@]}
	else
		echo "You do not seem to be using a supported package manager."
		echo "Please make sure ${PACKAGES[@]} are installed then press [ENTER]"
		read NOT_USED
	fi
}

install_aid () {
#	version_check
	#the order of this may be wrong, changing it back to original for now
	pip_install
	system_package_install
}

install_aid
