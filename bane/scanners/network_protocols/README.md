<h1>Chargen_Amplification_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>Chargen_Amplification_Scanner</code> class is part of the "bane" module and is used to calculate the amplification factor for a given Chargen server.</p>

<h2>Class Constructor</h2>
<pre><code>class Chargen_Amplification_Scanner</code></pre>
<p>This class has a static method <code>scan</code> to calculate the amplification factor of a Chargen server. The <code>scan</code> method accepts the following parameters:</p>

<ul>
    <li><code>u</code> (str): The IP address of the Chargen server to scan.</li>
    <li><code>timeout</code> (int): The timeout value for the scan operation (default is 3 seconds).</li>
    <li><code>q</code> (str): The character to send to the Chargen server (default is '0').</li>
</ul>

<h2>Methods</h2>
<h3><code>scan(u, timeout=3, q='0')</code></h3>
<p>This static method calculates the amplification factor for a given Chargen server. It returns a dictionary with the following information:</p>
<ul>
    <li><code>'protocol'</code> (str): The protocol, which is 'chargen' in this case.</li>
    <li><code>'ip'</code> (str): The IP address of the Chargen server.</li>
    <li><code>'sent'</code> (int): The number of bytes sent to the server.</li>
    <li><code>'received'</code> (int): The number of bytes received from the server.</li>
    <li><code>'amplification_factor'</code> (float): The amplification factor calculated as the ratio of received bytes to sent bytes.</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>Chargen_Amplification_Scanner</code> class, you can call the <code>scan</code> method with the appropriate parameters. Here's an example:</p>

<pre><code>
from bane.scanners.network_protocols import Chargen_Amplification_Scanner

#Scan a Chargen server
result = Chargen_Amplification_Scanner.scan(u="192.168.1.1", timeout=5, q='A')

#Access the result
print("Chargen Amplification Scan Result:")
print("Protocol:", result['protocol'])
print("IP:", result['ip'])
print("Sent:", result['sent'])
print("Received:", result['received'])
print("Amplification Factor:", result['amplification_factor'])
</code></pre>
<h1>DNS_Amplification_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>DNS_Amplification_Scanner</code> class is used to calculate the amplification factor for a given DNS server. It is part of the "bane" module.</p>

<h2>Method</h2>
<h3><code>scan(u, timeout=3, q='google.com', t='ANY')</code></h3>
<p>This static method calculates the amplification factor for a given DNS server. It accepts the following parameters:</p>
<ul>
    <li><code>u</code> (str): The IP address of the DNS server to scan.</li>
    <li><code>timeout</code> (int): The timeout value for the scan operation (default is 3 seconds).</li>
    <li><code>q</code> (str): The domain name to resolve (default is 'google.com').</li>
    <li><code>t</code> (str): The DNS query type (default is 'ANY').</li>
</ul>

<h2>Method Details</h2>
<p>The <code>scan</code> method constructs a DNS query packet and sends it to the specified DNS server. It then calculates the amplification factor based on the sent and received data. The method returns a dictionary with the following information:</p>
<ul>
    <li><code>'protocol'</code> (str): The protocol, which is 'dns' in this case.</li>
    <li><code>'ip'</code> (str): The IP address of the DNS server.</li>
    <li><code>'sent'</code> (int): The number of bytes sent to the server.</li>
    <li><code>'received'</code> (int): The number of bytes received from the server.</li>
    <li><code>'amplification_factor'</code> (float): The amplification factor calculated as the ratio of received bytes to sent bytes.</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>DNS_Amplification_Scanner</code> class, you can call the <code>scan</code> method with the appropriate parameters. Here's an example:</p>

<pre><code>
from bane.scanners.network_protocols import DNS_Amplification_Scanner

#Scan a DNS server for amplification factor
result = DNS_Amplification_Scanner.scan(u="8.8.8.8", timeout=5, q="example.com", t="A")

#Access the result
print("DNS Amplification Scan Result:")
print("Protocol:", result['protocol'])
print("IP:", result['ip'])
print("Sent:", result['sent'])
print("Received:", result['received'])
print("Amplification Factor:", result['amplification_factor'])
</code></pre>
<h1>Echo_Amplification_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>Echo_Amplification_Scanner</code> class is used to calculate the amplification factor for a given Echo server. It is part of the "bane" module.</p>

<h2>Method</h2>
<h3><code>scan(u, q='a', timeout=3)</code></h3>
<p>This static method calculates the amplification factor for a given Echo server. It accepts the following parameters:</p>
<ul>
    <li><code>u</code> (str): The IP address of the Echo server to scan.</li>
    <li><code>q</code> (str): The data to send as the Echo request (default is 'a').</li>
    <li><code>timeout</code> (int): The timeout value for the scan operation (default is 3 seconds).</li>
</ul>

<h2>Method Details</h2>
<p>The <code>scan</code> method constructs an Echo request packet and sends it to the specified Echo server. It then calculates the amplification factor based on the sent and received data. The method returns a dictionary with the following information:</p>
<ul>
    <li><code>'protocol'</code> (str): The protocol, which is 'echo' in this case.</li>
    <li><code>'ip'</code> (str): The IP address of the Echo server.</li>
    <li><code>'sent'</code> (int): The number of bytes sent to the server.</li>
    <li><code>'received'</code> (int): The number of bytes received from the server.</li>
    <li><code>'amplification_factor'</code> (float): The amplification factor calculated as the ratio of received bytes to sent bytes.</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>Echo_Amplification_Scanner</code> class, you can call the <code>scan</code> method with the appropriate parameters. Here's an example:</p>

<pre><code>
from bane.scanners.network_protocols import Echo_Amplification_Scanner

#Scan an Echo server for amplification factor
result = Echo_Amplification_Scanner.scan(u="8.8.8.8", q="Hello, Echo!", timeout=5)

#Access the result
print("Echo Amplification Scan Result:")
print("Protocol:", result['protocol'])
print("IP:", result['ip'])
print("Sent:", result['sent'])
print("Received:", result['received'])
print("Amplification Factor:", result['amplification_factor'])
</code></pre>
<h1>Memcache_Amplification_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>Memcache_Amplification_Scanner</code> class is used to calculate the amplification factor for a given Memcache server. It is part of the "bane" module.</p>

<h2>Method</h2>
<h3><code>scan(u, timeout=3)</code></h3>
<p>This static method calculates the amplification factor for a given Memcache server. It accepts the following parameters:</p>
<ul>
    <li><code>u</code> (str): The IP address of the Memcache server to scan.</li>
    <li><code>timeout</code> (int): The timeout value for the scan operation (default is 3 seconds).</li>
</ul>

<h2>Method Details</h2>
<p>The <code>scan</code> method constructs a Memcache request packet and sends it to the specified Memcache server. It then calculates the amplification factor based on the sent and received data. The method returns a dictionary with the following information:</p>
<ul>
    <li><code>'protocol'</code> (str): The protocol, which is 'memcache' in this case.</li>
    <li><code>'ip'</code> (str): The IP address of the Memcache server.</li>
    <li><code>'sent'</code> (int): The number of bytes sent to the server.</li>
    <li><code>'received'</code> (int): The number of bytes received from the server.</li>
    <li><code>'amplification_factor'</code> (float): The amplification factor calculated as the ratio of received bytes to sent bytes.</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>Memcache_Amplification_Scanner</code> class, you can call the <code>scan</code> method with the appropriate parameters. Here's an example:</p>

<pre><code>
from bane.scanners.network_protocols import Memcache_Amplification_Scanner

#Scan a Memcache server for amplification factor
result = Memcache_Amplification_Scanner.scan(u="127.0.0.1", timeout=5)

#Access the result
print("Memcache Amplification Scan Result:")
print("Protocol:", result['protocol'])
print("IP:", result['ip'])
print("Sent:", result['sent'])
print("Received:", result['received'])
print("Amplification Factor:", result['amplification_factor'])
</code></pre>
<h1>NTP_Amplification_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>NTP_Amplification_Scanner</code> class is used to calculate the amplification factor for a given NTP (Network Time Protocol) server. It is part of the "bane" module.</p>

<h2>Method</h2>
<h3><code>scan(u, timeout=3)</code></h3>
<p>This static method calculates the amplification factor for a given NTP server. It accepts the following parameters:</p>
<ul>
    <li><code>u</code> (str): The IP address of the NTP server to scan.</li>
    <li><code>timeout</code> (int): The timeout value for the scan operation (default is 3 seconds).</li>
</ul>

<h2>Method Details</h2>
<p>The <code>scan</code> method constructs an NTP request packet and sends it to the specified NTP server. It then calculates the amplification factor based on the sent and received data. The method returns a dictionary with the following information:</p>
<ul>
    <li><code>'protocol'</code> (str): The protocol, which is 'ntp' in this case.</li>
    <li><code>'ip'</code> (str): The IP address of the NTP server.</li>
    <li><code>'sent'</code> (int): The number of bytes sent to the server.</li>
    <li><code>'received'</code> (int): The number of bytes received from the server.</li>
    <li><code>'amplification_factor'</code> (float): The amplification factor calculated as the ratio of received bytes to sent bytes.</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>NTP_Amplification_Scanner</code> class, you can call the <code>scan</code> method with the appropriate parameters. Here's an example:</p>

<pre><code>
from bane.scanners.network_protocols import NTP_Amplification_Scanner

#Scan an NTP server for amplification factor
result = NTP_Amplification_Scanner.scan(u="time.example.com", timeout=5)

#Access the result
print("NTP Amplification Scan Result:")
print("Protocol:", result['protocol'])
print("IP:", result['ip'])
print("Sent:", result['sent'])
print("Received:", result['received'])
print("Amplification Factor:", result['amplification_factor'])
</code></pre>
<h1>Ports_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>Ports_Scanner</code> class is used to scan a range of ports on a target IP address to check if they are open or closed. It is part of the "bane" module.</p>

<h2>Class Constructor</h2>
<pre><code>class Ports_Scanner(u, ports=[21, 22, 23, 25, 43, 53, 80, 443, 2082, 3306], threads_daemon=True, timeout=3, retry=0, check_open=True, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></pre>
<p>This constructor initializes an instance of the <code>Ports_Scanner</code> class with the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target IP address to scan.</li>
    <li><code>ports</code> (list): A list of port numbers to scan (default includes common ports).</li>
    <li><code>threads_daemon</code> (bool): Set thread as daemon (default is True).</li>
    <li><code>timeout</code> (int): Timeout for port scanning in seconds (default is 3 seconds).</li>
    <li><code>retry</code> (int): Number of retry attempts for scanning (default is 0).</li>
    <li><code>check_open</code> (bool): Check if the port is open (default is True).</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use for scanning (optional).</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use for scanning (optional).</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use for scanning (optional).</li>
</ul>

<h2>Methods</h2>
<h3><code>scan(self, target, port, check_open, timeout, retry)</code></h3>
<p>This method scans a specified port on the target IP address. It checks if the port is open or closed and updates the results in the <code>result</code> dictionary.</p>

<h2>Attributes</h2>
<p>The <code>Ports_Scanner</code> class has the following attributes:</p>
<ul>
    <li><code>result</code> (dict): A dictionary that stores the results of port scanning with port numbers as keys and "open" or "closed" as values.</li>
    <li><code>proxies</code> (list): A list of proxy configurations obtained from the provided HTTP and SOCKS proxies parameters.</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>Ports_Scanner</code> class, create an instance by providing the required parameters, and it will start scanning the specified ports in separate threads. Here's an example:</p>

<pre><code>
from bane.gather_info.network_protocols import Ports_Scanner

#Create an instance of Ports_Scanner
port_scanner = Ports_Scanner(
    u="192.168.1.1",
    ports=[80, 443, 22],
    threads_daemon=True,
    timeout=5,
    retry=1,
    check_open=True,
    socks4_proxies=["5.6.7.8:1080"],
    socks5_proxies=["9.10.11.12:1080"]
)

#Start port scanning
#The results will be available in port_scanner.result
while len(port_scanner.result) != len(port_scanner.ports):
    pass

#Access the results
print("Port Scanning Results:")
for port, status in port_scanner.result.items():
    print(f"Port {port}: {status}")
</code></pre>
<h1>SNMP_Amplification_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>SNMP_Amplification_Scanner</code> class is used to calculate the amplification factor for a given SNMP (Simple Network Management Protocol) server. It is part of the "bane" module.</p>

<h2>Method</h2>
<h3><code>scan(u, timeout=3)</code></h3>
<p>This static method calculates the amplification factor for a given SNMP server. It accepts the following parameters:</p>
<ul>
    <li><code>u</code> (str): The IP address of the SNMP server to scan.</li>
    <li><code>timeout</code> (int): The timeout value for the scan operation (default is 3 seconds).</li>
</ul>

<h2>Method Details</h2>
<p>The <code>scan</code> method constructs an SNMP request packet and sends it to the specified SNMP server. It then calculates the amplification factor based on the sent and received data. The method returns a dictionary with the following information:</p>
<ul>
    <li><code>'protocol'</code> (str): The protocol, which is 'snmp' in this case.</li>
    <li><code>'ip'</code> (str): The IP address of the SNMP server.</li>
    <li><code>'sent'</code> (int): The number of bytes sent to the server.</li>
    <li><code>'received'</code> (int): The number of bytes received from the server.</li>
    <li><code>'amplification_factor'</code> (float): The amplification factor calculated as the ratio of received bytes to sent bytes.</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>SNMP_Amplification_Scanner</code> class, you can call the <code>scan</code> method with the appropriate parameters. Here's an example:</p>

<pre><code>
from bane.scanners.network_protocols import SNMP_Amplification_Scanner

#Scan an SNMP server for amplification factor
result = SNMP_Amplification_Scanner.scan(u="192.168.1.1", timeout=5)

#Access the result
print("SNMP Amplification Scan Result:")
print("Protocol:", result['protocol'])
print("IP:", result['ip'])
print("Sent:", result['sent'])
print("Received:", result['received'])
print("Amplification Factor:", result['amplification_factor'])
</code></pre>
<h1>SSDP_Amplification_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>SSDP_Amplification_Scanner</code> class is used to calculate the amplification factor for a given SSDP (Simple Service Discovery Protocol) server. It is part of the "bane" module.</p>

<h2>Method</h2>
<h3><code>scan(u, timeout=3)</code></h3>
<p>This static method calculates the amplification factor for a given SSDP server. It accepts the following parameters:</p>
<ul>
    <li><code>u</code> (str): The IP address of the SSDP server to scan.</li>
    <li><code>timeout</code> (int): The timeout value for the scan operation (default is 3 seconds).</li>
</ul>

<h2>Method Details</h2>
<p>The <code>scan</code> method constructs an SSDP request packet and sends it to the specified SSDP server. It then calculates the amplification factor based on the sent and received data. The method returns a dictionary with the following information:</p>
<ul>
    <li><code>'protocol'</code> (str): The protocol, which is 'ssdp' in this case.</li>
    <li><code>'ip'</code> (str): The IP address of the SSDP server.</li>
    <li><code>'sent'</code> (int): The number of bytes sent to the server.</li>
    <li><code>'received'</code> (int): The number of bytes received from the server.</li>
    <li><code>'amplification_factor'</code> (float): The amplification factor calculated as the ratio of received bytes to sent bytes.</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>SSDP_Amplification_Scanner</code> class, you can call the <code>scan</code> method with the appropriate parameters. Here's an example:</p>

<pre><code>
from bane.scanners.network_protocols import SSDP_Amplification_Scanner

#Scan an SSDP server for amplification factor
result = SSDP_Amplification_Scanner.scan(u="239.255.255.250", timeout=5)

#Access the result
print("SSDP Amplification Scan Result:")
print("Protocol:", result['protocol'])
print("IP:", result['ip'])
print("Sent:", result['sent'])
print("Received:", result['received'])
print("Amplification Factor:", result['amplification_factor'])
</code></pre>
