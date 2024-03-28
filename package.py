import os
import sys


def install():
    print("[App] Starting install.")
    os.system("sudo bash build.sh")
    print("[App] Install Completed.")
    sys.exit()


def uninstall():
    print("[App] Starting Uninstall.")
    os.system("sudo bash uninstall.sh")
    print("[App] Uninstall Completed.")
