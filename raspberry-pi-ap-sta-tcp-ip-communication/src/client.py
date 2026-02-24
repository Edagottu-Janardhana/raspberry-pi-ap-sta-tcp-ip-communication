"""
node_B.py
==================================================
Node B - Station + TCP Client

Role:
1. Connects to Node A as Station (STA)
2. Receives packet from Node A
3. Sends ACK
4. (Optional) Can switch to AP for forwarding

Author: <Your Name>
Project: Raspberry Pi TCP/IP AP-STA Communication
==================================================
"""

import socket
import subprocess

# ================= CONFIGURATION =================

STA_PROFILE = "sage_a_sta"
UPSTREAM_SSID = "SAGE_A_AP"
WIFI_PASS = "sage1234"

A_AP_IP = "10.42.0.1"
PORT = 5000

# =================================================


def run(cmd):
    """
    Executes shell command for Wi-Fi management.
    """
    print(f"[CMD] {cmd}")
    subprocess.run(cmd, shell=True, check=False)


def profile_exists(profile):
    """
    Checks if nmcli profile already exists.
    """
    result = subprocess.run(
        f"nmcli -t -f NAME connection show | grep -w {profile}",
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0


def ensure_sta_profile(profile, ssid, password):
    """
    Creates STA profile if not already present.
    """
    if profile_exists(profile):
        print(f"[WIFI] Profile '{profile}' exists")
        return

    print(f"[WIFI] Creating profile '{profile}'")

    run(
        f'nmcli connection add type wifi ifname wlan0 '
        f'con-name {profile} ssid "{ssid}"'
    )

    run(
        f'nmcli connection modify {profile} '
        f'wifi-sec.key-mgmt wpa-psk '
        f'wifi-sec.psk "{password}"'
    )


def start_sta(profile):
    """
    Connects to AP using stored profile.
    """
    print(f"[WIFI] Connecting using profile '{profile}'")
    run("nmcli dev disconnect wlan0")
    run(f"nmcli connection up {profile}")


def tcp_client_receive(server_ip, port):
    """
    Connects to TCP server and receives packet.
    Sends ACK back to server.
    """
    print("[B][TCP] Connecting to Node A")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, port))

    data = sock.recv(1024).decode()
    print("[B][TCP] Packet received:", data)

    sock.sendall(b"ACK_from_NodeB")
    sock.close()

    return data


if __name__ == "__main__":
    print("\n========== NODE B START ==========\n")

    ensure_sta_profile(STA_PROFILE, UPSTREAM_SSID, WIFI_PASS)
    start_sta(STA_PROFILE)
    tcp_client_receive(A_AP_IP, PORT)

    print("\n========== NODE B COMPLETE ==========\n")
