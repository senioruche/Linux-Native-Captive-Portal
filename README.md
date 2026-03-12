# Linux-Native Hardened Captive Portal

A lightweight, secure, and scalable captive portal for Debian using `nftables` and `Python`.

## Features
- **Walled Garden:** Selective access to Google/YouTube before login via `dnsmasq` nftsets.
- **Security:** Obfuscated unlock paths and TCP Resets on Port 443 to prevent browser hangs.
- **Scalability:** Multi-threaded Python backend.
- **Dynamic Rules:** Automated firewall whitelisting with 2-hour session timeouts.

## Logic Flow

1. Client makes an HTTP request.
2. `nftables` redirects unauthorized traffic to the local Python server.
3. User clicks "Accept," triggering a call to the secret endpoint.
4. Python executes an `nft` command to add the user's IP to the `allowed_clients` set.
5. User gains full internet access via NAT.

## Installation
1. Install dependencies: `sudo apt install nftables dnsmasq python3`
2. Apply firewall: `sudo nft -f config/nftables.conf`
3. Start portal: `sudo python3 src/portal.py`
