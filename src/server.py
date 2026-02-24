"""
node_A.py
===============================================
Node A - Access Point + TCP Server

Role:
1. Configures Raspberry Pi as Wi-Fi Access Point (AP)
2. Starts TCP server
3. Sends predefined packet to Node B
4. Waits for ACK response

Author: <Your Name>
Project: Raspberry Pi TCP/IP AP-STA Communication
===============================================
"""

import socket
import subprocess

# ================= CONFIGURATION =================

AP_SSID = "SAGE_A_AP"
WIFI_PASS = "sage1234"
PORT = 5000

PACKET = "5aa50700440000100155"

# =================================================


def run(cmd):
    """
    Executes shell command.
    Used for nmcli Wi-Fi configuration.
    """
    print(f"[CMD] {cmd}")
    subprocess.run(cmd, shell=True, check=False)


def start_ap():
    """
    Starts Wi-Fi hotspot using NetworkManager.
    """
    print("[A][WIFI] Starting Access Point mode")
    run("nmcli dev disconnect wlan0")
    run(
        f'nmcli dev wifi hotspot ifname wlan0 '
        f'ssid "{AP_SSID}" password "{WIFI_PASS}"'
    )


def tcp_server_send():
    """
    Starts TCP server and sends packet to connected client.
    """
    print("[A][TCP] Starting TCP server")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("", PORT))
    server.listen(1)

    print("[A][TCP] Waiting for client connection...")
    conn, addr = server.accept()
    print("[A][TCP] Client connected from", addr[0])

    # Send data packet
    conn.sendall(PACKET.encode())
    print("[A][TCP] Packet sent")

    # Wait for ACK
    ack = conn.recv(1024).decode()
    print("[A][TCP] ACK received:", ack)

    conn.close()
    server.close()


if __name__ == "__main__":
    print("\n========== NODE A START ==========\n")
    start_ap()
    tcp_server_send()
    print("\n========== NODE A COMPLETE ==========\n")
