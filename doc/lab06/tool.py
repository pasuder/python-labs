import subprocess


def run(cmd):
    print(subprocess.run(cmd.split(),
                         capture_output=True).stdout.decode())