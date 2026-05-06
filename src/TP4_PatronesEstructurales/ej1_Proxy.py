# TP4 - Ejercicio 1: Ping

class Ping:
    def execute(self, ip_string):
        if not ip_string.startswith("192."):
            raise ValueError(f"Dirección IP no permitida: {ip_string}. Debe comenzar con '192.'")
        print(f"Realizando 10 pings a {ip_string}...")
        for i in range(1, 11):
            print(f"  Intento {i}: Ping exitoso a {ip_string}")
        
    def executefree(self, ip_string):
        print(f"Realizando 10 pings libres a {ip_string}...")
        for i in range(1, 11):
            print(f"  Intento {i}: Ping exitoso a {ip_string}")

class PingProxy:
    def __init__(self):
        self._ping = Ping()

    def execute(self, ip_string):
        if ip_string == "192.168.0.254":
            print(f"Proxy detectado: Dirección especial {ip_string}. Redirigiendo a google.com")
            self._ping.executefree("www.google.com")
        else:
            print(f"Proxy detectado: Dirección estándar {ip_string}.")
            self._ping.execute(ip_string)

# Ejemplo de uso:
if __name__ == "__main__":
    proxy = PingProxy()
    print("--- Caso 1: IP normal ---")
    proxy.execute("192.168.1.1")
    
    print("\n--- Caso 2: IP especial (redirección) ---")
    proxy.execute("192.168.0.254")