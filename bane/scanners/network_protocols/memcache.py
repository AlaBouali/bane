from bane.scanners.network_protocols.utils import *


class Memcache_Amplification_Scanner:

    @staticmethod
    def scan(u, timeout=3):
        """
    calculate the amplification factor for any given memcache server
    """

    # creating the payload

        req = IP(dst=u) / UDP(sport=random.randint(1025, 65500),
                            dport=11211) \
            / Raw(load='\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n')
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                        socket.IPPROTO_UDP)  # creating a raw socket
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        s.sendto(bytes(req), (u, 11211))
        s.settimeout(timeout)  # set timeout
        d = ''
        while True:
            try:
                o = ''
                o += str(s.recv(4096))
            except KeyboardInterrupt:
                s.close()
                break
            except:
                pass
            if len(o) == 0:
                break
            else:
                d += o
        a = len(req)
        b = len(d)
        c = round(len(d) * 1. / len(req), 3)
        return {
            'protocol': 'memcache',
            'ip': u,
            'sent': a,
            'received': b,
            'amplification_factor': c,
            }

