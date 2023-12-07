import socket
import math

class IPCalculator:
    def calculate_network_class(self):
        ip_parts = self.int_to_ip(self.ip).split('.')
        first_octet = int(ip_parts[0])

        if 1 <= first_octet <= 126:
            return "A"
        elif 128 <= first_octet <= 191:
            return "B"
        elif 192 <= first_octet <= 223:
            return "C"
        elif 224 <= first_octet <= 239:
            return "D"
        elif 240 <= first_octet <= 255:
            return "E"
        else:
            return "No se pudo determinar la clase de red"

    def __init__(self, ip, cidr):
        self.ip = self.ip_to_int(ip)
        self.cidr = cidr

    def ip_to_int(self, ip):
        ip_parts = ip.split('.')
        return int(ip_parts[0]) << 24 | int(ip_parts[1]) << 16 | int(ip_parts[2]) << 8 | int(ip_parts[3])

    def calculate(self):
        host_bits = 32 - self.cidr
        Red_bits = self.cidr

        # Create subnet mask
        subnet_mask = ((1 << Red_bits) - 1) << host_bits 
        # Calculate wildcard mask
        wildcard_mask = 0xffffffff ^ ((1 << Red_bits) - 1) << host_bits

        # Calculate subnet
        subnet = self.ip & subnet_mask
        # Calculate network address
        network = subnet

        # Calculate broadcast address
        broadcast = self.ip | (subnet_mask ^ 0xffffffff)

        

        # Calculate host range
        ip_initial = self.ip + 1
        #ip_final = self.ip + (1 << host_bits) - 3

        ip_final = broadcast - 1

        return {
            "Direccion IP: ": f"{self.int_to_ip(self.ip)}/{self.cidr}",
            "Mascara de red": f"{self.int_to_ip(subnet_mask)}",
            "Mascara Wildcard": f"{self.int_to_ip(wildcard_mask)}",
            "Red": f"{self.int_to_ip(network)}",
            "Direccion de Broadcast": f"{self.int_to_ip(broadcast)}",
            "Hosts por subred": f"{2 ** (32 - self.cidr)}",
            "Hosts por subred utilizables": f"{2 ** (32 - self.cidr) - 2}",
            "Red clase ": f"{self.calculate_network_class()}",
            "Primera ip valida": f"{self.int_to_ip(ip_initial)}",
            "Host Maximo": f"{self.int_to_ip(ip_final)}",
        }

    def int_to_ip(self, n):
        return f"{n >> 24}.{(n >> 16) & 0xff}.{(n >> 8) & 0xff}.{n & 0xff}"

def main():
    ip = "192.168.1.1"
    cidr = 24

    ip_calc = IPCalculator(ip, cidr)
    result = ip_calc.calculate()
    for key, value in result.items():
        print(f"{key}: \t{value}")

if __name__ == "__main__":
    main()
