from bane.scanners.network_protocols.utils import *

class SSDP_Amplification_Scanner:

    @staticmethod
    def scan(u, timeout=3):
        """
    calculate the amplification factor for any given ssdp server
    """
        started_at=time.time()
        req = IP(dst=u) / UDP(sport=random.randint(1025, 65500),
                            dport=1900) \
            / Raw(load='''M-SEARCH * HTTP/1.1\r
    HOST: 239.255.255.250:1900\r
    MAN: "ssdp:discover"\r
    MX: 2\r
    ST: ssdp:all\r
    \r
    ''')
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                        socket.IPPROTO_UDP)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        s.sendto(bytes(req), (u, 1900))
        s.settimeout(timeout)
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
            'protocol': 'ssdp',
            'ip': u,
            'sent': a,
            'received': b,
            'amplification_factor': c,
            'start_date':started_at,
            'end_date':time.time()
            }
