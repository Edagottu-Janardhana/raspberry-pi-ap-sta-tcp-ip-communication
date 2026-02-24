# Raspberry Pi TCP/IP Communication in AP-STA Mode

## Overview

This project demonstrates TCP/IP communication between two Raspberry Pis
over Wi-Fi using Access Point (AP) and Station (STA) modes.

### Node A

-   Wi-Fi Access Point
-   TCP Server

### Node B

-   Wi-Fi Station
-   TCP Client

The system enables direct device-to-device communication without
requiring an external router.

This module serves as a networking validation layer for gateway-based
embedded systems such as Sage Algiz / Sage Beacon.

------------------------------------------------------------------------

## System Architecture

            Node A (AP + TCP Server)
                    |
                    |  Wi-Fi (AP-STA Mode)
                    |
            Node B (STA + TCP Client)

-   Node A dynamically creates a Wi-Fi hotspot.
-   Node B connects as a Station using NetworkManager.
-   TCP communication is established over the created network.
-   Packet transmission includes ACK-based validation.

------------------------------------------------------------------------

## Hardware Setup

Two Raspberry Pi Compute Module 4 boards were used for testing.

-   Node A: Access Point + TCP Server
-   Node B: Station + TCP Client

![Hardware Setup](docs/images/hardware_setup.jpg)

------------------------------------------------------------------------

## Test Output

### Node A Terminal Output

![Node A Output](docs/images/nodeA_terminal.jpg)

### Node B Terminal Output

![Node B Output](docs/images/nodeB_terminal.jpg)

------------------------------------------------------------------------

## Features

-   Dynamic Wi-Fi Access Point creation using nmcli
-   Automatic STA profile management
-   TCP socket-based communication
-   ACK-based reliability mechanism
-   Router-less embedded networking
-   Modular and extensible design

------------------------------------------------------------------------

## Requirements

### Hardware

-   2 × Raspberry Pi (Raspberry Pi 4 / CM4)
-   Wi-Fi interface enabled

### Software

-   Raspberry Pi OS (Lite recommended)
-   Python 3.x
-   NetworkManager (nmcli enabled)

------------------------------------------------------------------------

## Running the Application

### On Node A (Access Point + Server)

python3 node_A.py

Node A will: 
- Disconnect existing Wi-Fi 
- Create hotspot - Start TCP server 
- Send packet to Node B 
- Wait for ACK

------------------------------------------------------------------------

### On Node B (Station + Client)

python3 node_B.py

Node B will: 
- Create STA profile (if missing) 
- Connect to Node A hotspot 
- Receive packet 
- Send ACK response

------------------------------------------------------------------------

## Use Cases

-   IoT gateway provisioning
-   Embedded device commissioning
-   Router-less communication testing
-   Edge-to-edge networking validation
-   Multi-node relay architecture (extendable to Node C)

------------------------------------------------------------------------

## Future Improvements

-   Ethernet fallback support
-   Multi-hop node forwarding
-   BLE integration
-   LoRa integration (SX1302)
-   Secure socket layer (TLS)

------------------------------------------------------------------------
