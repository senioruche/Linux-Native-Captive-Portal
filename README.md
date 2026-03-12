# Linux-Native-Captive-Portal
A lightweight, high-performance Walled Garden and Captive Portal system built for Debian using nftables, dnsmasq, and a multi-threaded Python backend.

🛠️ The Tech Stack

Routing: Debian 12 (Bookworm)

Firewall: nftables (Dynamic sets for IP whitelisting)

DNS/DHCP: dnsmasq (IPSet/nftset integration)

Backend: Python 3 (Multi-threaded HTTP server)

🧠 How It Works

Interception: nftables intercepts unauthorized Port 80 traffic and redirects it to a local Python handler.

The Walled Garden: dnsmasq populates a dynamic nftables set (google_ips) to allow access to specific domains (Google/YouTube) before authentication.

Authentication: The Python script serves a local splash page. Upon clicking "Accept," the script dynamically updates the nftables set to grant the client full internet access for a configurable timeout.

Security: Implements "Secret Path" obfuscation and TCP Resets on Port 443 to prevent browser hanging and directory brute-forcing.
