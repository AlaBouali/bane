from bane.scanners.network_protocols.utils import *

class DNS_Amplification_Scanner:

    @staticmethod
    def scan(
        u,
        timeout=3,
        q='google.com',
        t='ANY',
        ):
        """
    calculate the amplification factor for any given dns server
    """

    # q: the domain name to resolve
    # t: the dns query type

        req = IP(dst=u) / UDP(sport=random.randint(1025, 65500), dport=53) \
            / DNS(rd=1, qd=DNSQR(qname=q, qtype=t))
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                        socket.IPPROTO_UDP)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        s.sendto(bytes(req), (u, 53))
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
            'protocol': 'dns',
            'ip': u,
            'sent': a,
            'received': b,
            'amplification_factor': c,
            }

