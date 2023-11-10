from bane.scanners.network_protocols.utils import *

class SNMP_Amplification_Scanner:

    @staticmethod
    def scan(u, timeout=3):
        """
    calculate the amplification factor for any given snmp server
    """
        started_at=time.time()

        req = IP(dst=u) / UDP(sport=random.randint(1025, 65500), dport=161) \
            / Raw(load='\x30\x26\x02\x01\x01\x04\x06\x70\x75\x62\x6c\x69\x63\xa5\x19\x02\x04\x71\xb4\xb5\x68\x02\x01\x00\x02\x01\x7F\x30\x0b\x30\x09\x06\x05\x2b\x06\x01\x02\x01\x05\x00'
                )
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                        socket.IPPROTO_UDP)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        s.sendto(bytes(req), (u, 161))
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
            'protocol': 'snmp',
            'ip': u,
            'sent': a,
            'received': b,
            'amplification_factor': c,
            'start_date':started_at,
            'end_date':time.time()
            }
