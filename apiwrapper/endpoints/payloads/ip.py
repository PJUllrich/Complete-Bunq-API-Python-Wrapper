class IP:
    def __init__(self, ip, status):
        self.ip = ip if isinstance(ip, str) else str(ip)
        self.status = status.upper()
        if status != "ACTIVE" or status != "INACTIVE":
            print('Error: The status is not ACTIVE or INACTIVE')
