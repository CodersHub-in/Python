import socket
import argparse
import tqdm
import concurrent.futures

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            return True
        else:
            return False
    except socket.error as e:
        print(f"Error scanning port {port}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Network Scanner")
    parser.add_argument("ip", help="IP address to scan")
    args = parser.parse_args()

    common_ports = [22, 80, 443, 110, 143, 161, 162, 389, 636, 993, 995 , 3306, 5432, 8080, 8443,3000]
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(scan_port, args.ip, port): port for port in common_ports}
        for future in concurrent.futures.as_completed(futures):
            port = futures[future]
            try:
                result = future.result()
            except Exception as e:
                print(f"Error scanning port {port}: {e}")
            else:
                if result:
                    print(f"{port}\tOpen")
                else:
                    print(f"{port}\tClosed")

if __name__ == "__main__":
    main()
