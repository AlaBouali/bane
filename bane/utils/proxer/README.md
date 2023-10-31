<h1>BurpSuite_Getter Class</h1>

<h2>Class Overview</h2>
<p>The <code>BurpSuite_Getter</code> class is part of the "bane" module and provides a method for obtaining a Burp Suite proxy configuration. It includes a method for getting the Burp Suite proxy settings with optional host and port parameters.</p>

<h2>Methods</h2>

<h3><code>get_proxy(host=Common_Variables.burpsuit_proxy_host, port=Common_Variables.burpsuit_proxy_port)</code></h3>
<p>This method retrieves the Burp Suite proxy settings as a dictionary. It allows you to specify the host and port for the Burp Suite proxy, or you can use the default values defined in the <code>Common_Variables</code> module. It returns a dictionary containing the Burp Suite proxy configuration. It takes the following parameters:</p>
<ul>
    <li><code>host</code> (str): The host or IP address of the Burp Suite proxy (default is defined in <code>Common_Variables</code>).</li>
    <li><code>port</code> (int): The port of the Burp Suite proxy (default is defined in <code>Common_Variables</code>).</li>
</ul>

<h2>Example Usage</h2>
<p>Here's an example of how to use the <code>BurpSuite_Getter</code> class method:</p>

<pre><code>
from bane import BurpSuite_Getter

#Get the Burp Suite proxy configuration with default values
proxy_settings = BurpSuite_Getter.get_proxy()

#Get the Burp Suite proxy configuration with custom host and port
custom_host = "127.0.0.1"
custom_port = 8080
custom_proxy_settings = BurpSuite_Getter.get_proxy(custom_host, custom_port)

#Now you can use the proxy_settings and custom_proxy_settings as needed
print("Default Proxy Settings:", proxy_settings)
print("Custom Proxy Settings:", custom_proxy_settings)
</code></pre>
<h1>Proxies_Collector Class</h1>

<h2>Class Overview</h2>
<p>The <code>Proxies_Collector</code> class is part of the "bane" module and is used to collect and verify proxy information from various sources.</p>

<h2>Methods</h2>

<h3><code>proxygeonode(is_socket=True, verify_request=False, protocols=['http', 'socks4', 'socks5'], anonymities=["elite", "anonymous"], timeout=20, proxy=None, headers={'Referer': 'https://geonode.com/', 'User-Agent': 'random User-Agent'}, check_proxies=True, check_timeout=10, logs=False, threads=250)</code></h3>
<p>This method collects and verifies proxies from the GeoNode proxy service. It takes the following parameters:</p>
<ul>
    <li><code>is_socket</code> (bool): Use socket for proxy verification (default is True).</li>
    <li><code>verify_request</code> (bool): Verify the proxy by sending an HTTP request (default is False).</li>
    <li><code>protocols</code> (list): List of proxy protocols to collect (default is ['http', 'socks4', 'socks5']).</li>
    <li><code>anonymities</code> (list): List of proxy anonymities to collect (default is ["elite", "anonymous"]).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 20).</li>
    <li><code>proxy</code> (dict): Dictionary of proxy configuration (default is None).</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include in requests.</li>
    <li><code>check_proxies</code> (bool): Perform proxy verification (default is True).</li>
    <li><code>check_timeout</code> (int): Proxy verification timeout in seconds (default is 10).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is False).</li>
    <li><code>threads</code> (int): Number of threads for proxy verification (default is 250).</li>
</ul>

<h3><code>proxyscrape(is_socket=True, verify_request=False, protocols=['http', 'socks4', 'socks5'], anonymities=["elite", "anonymous"], timeout=10, country="all", proxy=None, threads=250, check_timeout=10, logs=False, check_proxies=True)</code></h3>
<p>This method collects and verifies proxies from the ProxyScrape service. It takes the following parameters:</p>
<ul>
    <li><code>is_socket</code> (bool): Use socket for proxy verification (default is True).</li>
    <li><code>verify_request</code> (bool): Verify the proxy by sending an HTTP request (default is False).</li>
    <li><code>protocols</code> (list): List of proxy protocols to collect (default is ['http', 'socks4', 'socks5']).</li>
    <li><code>anonymities</code> (list): List of proxy anonymities to collect (default is ["elite", "anonymous"]).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 10).</li>
    <li><code>country</code> (str): The country code for proxy collection (default is "all").</li>
    <li><code>proxy</code> (dict): Dictionary of proxy configuration (default is None).</li>
    <li><code>threads</code> (int): Number of threads for proxy verification (default is 250).</li>
    <li><code>check_timeout</code> (int): Proxy verification timeout in seconds (default is 10).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is False).</li>
    <li><code>check_proxies</code> (bool): Perform proxy verification (default is True).</li>
</ul>

<!-- Repeat the same format for the remaining methods -->

<h3><code>proxylistdownload(protocols=['socks4', 'socks5'], check_proxies=True, timeout=15, check_timeout=10, logs=False, verify_request=False, is_socket=True, threads=250, proxy=None)</code></h3>

<h3><code>proxyspace(protocols=['socks4', 'socks5'], check_proxies=True, timeout=15, check_timeout=10, logs=False, verify_request=False, is_socket=True, threads=250, proxy=None)</code></h3>

<h3><code>proxybarcode(protocols=['socks4', 'socks5'], check_proxies=True, timeout=15, check_timeout=10, logs=False, verify_request=False, is_socket=True, threads=250, proxy=None)</code></h3>

<h3><code>proxyopenlist(protocols=['socks4', 'socks5'], check_proxies=True, timeout=15, check_timeout=10, logs=False, verify_request=False, is_socket=True, threads=250, proxy=None)</code></h3>

<h3><code>get_valid_proxies(geonode=True, scrape=True, space=True, barcode=True, listdownload=True, openlist=True, update_default_list=True, protocols=['socks4', 'socks5', 'http'], check_proxies=True, timeout=15, check_timeout=5, logs=True, verify_request=False, is_socket=True, threads=300, proxy=None)</code></h3>

<h2>Example Usage</h2>
<p>To use the <code>Proxies_Collector</code> class, you can call its methods to collect and verify proxies from various sources. Here's an example:</p>

<pre><code>
from bane.proxies_collector import Proxies_Collector

#Collect and verify proxies using Proxies_Collector
proxies = Proxies_Collector.proxygeonode(check_proxies=True, verify_request=True, protocols=['http', 'socks4', 'socks5'], timeout=20, proxy={"http": "http://1.2.3.4:80", "https": "http://1.2.3.4:80"}, headers={'Referer': 'https://geonode.com/', 'User-Agent': 'random User-Agent'}, logs=True, threads=250)

#Access the result
print("Verified Proxies:", proxies)
</code></pre>

<h1>Proxies_Interface Class</h1>

<h2>Class Overview</h2>
<p>The <code>Proxies_Interface</code> class is part of the "bane" module and provides methods for loading, parsing, and converting proxy data for use in various applications.</p>

<h2>Methods</h2>

<h3><code>load_and_parse_proxies(source, proxies_type)</code></h3>
<p>This method loads and parses proxy data from various sources based on the provided <code>proxies_type</code>. It supports loading proxies from strings, files, dictionaries, and more. It takes the following parameters:</p>
<ul>
    <li><code>source</code> (str, dict, list, tuple): The source of proxy data to load and parse.</li>
    <li><code>proxies_type</code> (str): The type of proxies to load and parse (e.g., 'http', 'socks4', 'socks5', or None).</li>
</ul>

<h3><code>load_and_parse_proxies_all(http_proxies=None, socks4_proxies=None, socks5_proxies=None, json_file=None)</code></h3>
<p>This method loads and parses proxy data for multiple types (HTTP, SOCKS4, SOCKS5) and combines them into a single list. It takes the following parameters:</p>
<ul>
    <li><code>http_proxies</code> (str, dict, list, tuple): Proxy data for HTTP proxies.</li>
    <li><code>socks4_proxies</code> (str, dict, list, tuple): Proxy data for SOCKS4 proxies.</li>
    <li><code>socks5_proxies</code> (str, dict, list, tuple): Proxy data for SOCKS5 proxies.</li>
    <li><code>json_file</code> (str): JSON file containing proxy data.</li>
</ul>

<h3><code>get_requests_proxies_from_parameter(parameter, proxies_type)</code></h3>
<p>This method converts proxy parameters into a format suitable for HTTP requests. It supports various input types such as dictionaries, strings, lists, and tuples. It takes the following parameters:</p>
<ul>
    <li><code>parameter</code> (dict, str, list, tuple): Proxy parameter data to convert.</li>
    <li><code>proxies_type</code> (str): The type of proxies to convert (e.g., 'http', 'socks4', 'socks5', or None).</li>
</ul>

<h3><code>get_requests_proxies_from_parameters(proxies=None, proxy=None, http_proxies=None, socks4_proxies=None, socks5_proxies=None, json_file=None)</code></h3>
<p>This method combines and converts multiple proxy parameters into a format suitable for HTTP requests. It supports various sources such as dictionaries, strings, lists, tuples, and JSON files. It takes the following parameters:</p>
<ul>
    <li><code>proxies</code> (dict, str, list, tuple): Proxy parameter data for all types.</li>
    <li><code>proxy</code> (dict, str, list, tuple): Proxy parameter data for a specific type.</li>
    <li><code>http_proxies</code> (dict, str, list, tuple): Proxy parameter data for HTTP proxies.</li>
    <li><code>socks4_proxies</code> (dict, str, list, tuple): Proxy parameter data for SOCKS4 proxies.</li>
    <li><code>socks5_proxies</code> (dict, str, list, tuple): Proxy parameter data for SOCKS5 proxies.</li>
    <li><code>json_file</code> (str): JSON file containing proxy data.</li>
</ul>

<h3><code>requests_proxy_to_socket_proxy(proxy)</code></h3>
<p>This method converts a proxy parameter for HTTP requests into a format suitable for socket-level connections. It takes the following parameter:</p>
<ul>
    <li><code>proxy</code> (dict): Proxy parameter data for HTTP requests.</li>
</ul>

<h3><code>get_socket_proxies_from_parameters(proxies=None, proxy=None, http_proxies=None, socks4_proxies=None, socks5_proxies=None, json_file=None)</code></h3>
<p>This method combines and converts multiple proxy parameters into a format suitable for socket-level connections. It supports various sources such as dictionaries, strings, lists, tuples, and JSON files. It takes the following parameters:</p>
<ul>
    <li><code>proxies</code> (dict, str, list, tuple): Proxy parameter data for all types.</li>
    <li><code>proxy</code> (dict, str, list, tuple): Proxy parameter data for a specific type.</li>
    <li><code>http_proxies</code> (dict, str, list, tuple): Proxy parameter data for HTTP proxies.</li>
    <li><code>socks4_proxies</code> (dict, str, list, tuple): Proxy parameter data for SOCKS4 proxies.</li>
    <li><code>socks5_proxies</code> (dict, str, list, tuple): Proxy parameter data for SOCKS5 proxies.</li>
    <li><code>json_file</code> (str): JSON file containing proxy data.</li>
</ul>
<h1>ProxyChecker Class</h1>

<h2>Class Overview</h2>
<p>The <code>ProxyChecker</code> class is responsible for checking the validity and functionality of proxy servers in a list. It can perform proxy checks using either socket-level connections or HTTP requests, depending on the configuration.</p>

<h2>Class Constructor</h2>
<pre><code>class ProxyChecker(proxy_list, threads=250, timeout=10, logs=True, verify_request=False, is_socket=True)
</code></pre>
<p>The constructor initializes an instance of the <code>ProxyChecker</code> class with the following parameters:</p>
<ul>
    <li><code>proxy_list</code> (list of dict): A list of proxy dictionaries to be checked.</li>
    <li><code>threads</code> (int): The number of threads to use for parallel proxy checking (default is 250).</li>
    <li><code>timeout</code> (int): The timeout for proxy checks in seconds (default is 10).</li>
    <li><code>logs</code> (bool): Enable or disable logging during the proxy checking process (default is True).</li>
    <li><code>verify_request</code> (bool): Enable or disable additional verification using an HTTP request (default is False).</li>
    <li><code>is_socket</code> (bool): Use socket-level connections for proxy checks (True) or HTTP requests (False) (default is True).</li>
</ul>

<h2>Methods</h2>

<h3><code>check_proxies()</code></h3>
<p>This method initiates the proxy checking process. It divides the proxy list into chunks and runs proxy checks in parallel using multiple threads. The number of threads is determined by the <code>threads</code> parameter. The method manages the checking process and updates the <code>result</code> attribute with active proxy servers.

<h3><code>_check_chunk(chunk)</code></h3>
<p>This internal method performs proxy checks on a chunk of proxy servers. It is called by <code>check_proxies()</code> for each thread. The method iterates through the proxy servers in the chunk and performs either socket-level or HTTP-based checks based on the <code>is_socket</code> parameter. Active proxy servers are added to the <code>result</code> attribute.

<h3><code>proxy_check_socket(verify_request=False, proxy_host, proxy_port, proxy_username, proxy_password, proxy_type, timeout, **kwargs)</code></h3>
<p>This method checks the validity of a proxy server using socket-level connections. It connects to a test destination, and if successful, it considers the proxy server active. The parameters include proxy details and a timeout for the connection. If <code>verify_request</code> is set to True, it additionally sends an HTTP request to verify the response.

<h3><code>proxy_check_requests(proxy_host, proxy_port, proxy_username, proxy_password, proxy_type, timeout, **kwargs)</code></h3>
<p>This method checks the validity of a proxy server using HTTP requests. It sends an HTTP request to a test destination, and if the response contains the expected content, it considers the proxy server active. The parameters include proxy details and a timeout for the request.

<h2>Example Usage</h2>
<p>To use the <code>ProxyChecker</code> class, create an instance by providing a list of proxy dictionaries and desired configuration parameters. The class will automatically check the proxies and store active ones in the <code>result</code> attribute. Here's an example:</p>
<pre><code>
from bane.proxies_checker import ProxyChecker

#Create an instance of ProxyChecker
proxy_list = [
    {
        'proxy_host': 'proxy1.example.com',
        'proxy_port': 8080,
        'proxy_username': 'user1',
        'proxy_password': 'pass1',
        'proxy_type': 'http'
    },
    {
        'proxy_host': 'proxy2.example.com',
        'proxy_port': 1080,
        'proxy_username': 'user2',
        'proxy_password': 'pass2',
        'proxy_type': 'socks4'
    },
    #Add more proxy dictionaries as needed
]

proxy_checker = ProxyChecker(proxy_list, threads=10, timeout=5, logs=True, verify_request=True, is_socket=False)

#The proxy checking process is performed in the background
#You can access the result after it's done
result = proxy_checker.result
print("Active Proxies:", result)
</code></pre>
<h1>Proxies_Getter Class</h1>

<h2>Class Overview</h2>
<p>The <code>Proxies_Getter</code> class is part of the "bane" module and is used to retrieve proxy sockets and proxy settings for various protocols.</p>

<h2>Class Methods</h2>

<h3><code>get_socks5_proxy_socket(host, port, proxy_host=None, proxy_port=None, proxy_username=None, proxy_password=None, no_delay=False, timeout=5, **kwargs)</code></h3>
<p>This method establishes a SOCKS5 proxy socket connection and returns the socket object. It takes the following parameters:</p>
<ul>
    <li><code>host</code> (str): The target host to connect to.</li>
    <li><code>port</code> (int): The target port to connect to.</li>
    <li><code>proxy_host</code> (str, optional): The SOCKS5 proxy server host.</li>
    <li><code>proxy_port</code> (int, optional): The SOCKS5 proxy server port.</li>
    <li><code>proxy_username</code> (str, optional): Username for proxy authentication.</li>
    <li><code>proxy_password</code> (str, optional): Password for proxy authentication.</li>
    <li><code>no_delay</code> (bool, optional): Set TCP_NODELAY socket option (default is False).</li>
    <li><code>timeout</code> (int, optional): Connection timeout in seconds (default is 5).</li>
</ul>

<h3><code>get_socks4_proxy_socket(host, port, proxy_host=None, proxy_port=None, proxy_username=None, proxy_password=None, no_delay=False, timeout=5, **kwargs)</code></h3>
<p>This method establishes a SOCKS4 proxy socket connection and returns the socket object. It takes the same parameters as <code>get_socks5_proxy_socket</code>.</p>

<h3><code>get_socks_proxy_socket(host, port, proxy_host=None, proxy_port=None, proxy_type=None, proxy_username=None, proxy_password=None, no_delay=False, timeout=5, **kwargs)</code></h3>
<p>This method establishes a SOCKS proxy socket connection and returns the socket object. It automatically detects and uses either SOCKS4 or SOCKS5 based on the proxy type provided. It takes the same parameters as <code>get_socks5_proxy_socket</code> with an additional <code>proxy_type</code> parameter for proxy type selection.</p>

<h3><code>get_http_proxy_socket(host, port, proxy_host=None, proxy_port=None, proxy_username=None, proxy_password=None, no_delay=False, timeout=5, **kwargs)</code></h3>
<p>This method establishes an HTTP proxy socket connection and returns the socket object. It takes the same parameters as <code>get_socks5_proxy_socket</code> but uses the HTTP protocol for proxying.</p>

<h3><code>get_proxy_socket(host, port, proxy_host=None, proxy_port=None, proxy_type=None, proxy_username=None, proxy_password=None, timeout=5, no_delay=False, **kwargs)</code></h3>
<p>This method establishes a proxy socket connection based on the provided proxy type and returns the socket object. It supports SOCKS4, SOCKS5, and HTTP proxy types. It takes the same parameters as <code>get_socks_proxy_socket</code> with an additional <code>proxy_type</code> parameter for proxy type selection.</p>

<h3><code>get_tor_socks5_socket(ip, port, timeout=5, no_delay=False, new_ip=True)</code></h3>
<p>This method retrieves a TOR SOCKS5 proxy socket connection and returns the socket object. It takes the following parameters:</p>
<ul>
    <li><code>ip</code> (str): The IP address of the TOR SOCKS5 proxy.</li>
    <li><code>port</code> (int): The port of the TOR SOCKS5 proxy.</li>
    <li><code>timeout</code> (int, optional): Connection timeout in seconds (default is 5).</li>
    <li><code>no_delay</code> (bool, optional): Set TCP_NODELAY socket option (default is False).</li>
    <li><code>new_ip</code> (bool, optional): Use a new TOR IP address (default is True).</li>
</ul>

<h3><code>get_tor_http_socket(ip, port, timeout=5, new_ip=True)</code></h3>
<p>This method retrieves a TOR HTTP proxy socket connection and returns the socket object. It takes the same parameters as <code>get_tor_socks5_socket</code> with an additional <code>new_ip</code> parameter for IP address renewal.</p>

<h3><code>get_requests_socks5_proxy(proxy_host=None, proxy_port=None, proxy_username=None, proxy_password=None, **kwargs)</code></h3>
<p>This method generates and returns a dictionary with proxy settings for using SOCKS5 proxies with the Python requests library. It takes the following parameters:</p>
<ul>
    <li><code>proxy_host</code> (str, optional): The SOCKS5 proxy server host.</li>
    <li><code>proxy_port</code> (int, optional): The SOCKS5 proxy server port.</li>
    <li><code>proxy_username</code> (str, optional): Username for proxy authentication.</li>
    <li><code>proxy_password</code> (str, optional): Password for proxy authentication.</li>
</ul>

<h3><code>get_requests_socks4_proxy(proxy_host=None, proxy_port=None, proxy_username=None, proxy_password=None, **kwargs)</code></h3>
<p>This method generates and returns a dictionary with proxy settings for using SOCKS4 proxies with the Python requests library. It takes the same parameters as <code>get_requests_socks5_proxy</code>.</p>

<h3><code>get_requests_http_proxy(proxy_host=None, proxy_port=None, proxy_username=None, proxy_password=None, **kwargs)</code></h3>
<p>This method generates and returns a dictionary with proxy settings for using HTTP proxies with the Python requests library. It takes the same parameters as <code>get_requests_socks5_proxy</code>.</p>

<h3><code>get_tor_socks5_proxy_windows(host, port, new_ip=True)</code></h3>
<p>This method retrieves a TOR SOCKS5 proxy for Windows and returns proxy settings in the form of a dictionary. It takes the following parameters:</p>
<ul>
    <li><code>host</code> (str): The IP address of the TOR SOCKS5 proxy.</li>
    <li><code>port</code> (int): The port of the TOR SOCKS5 proxy.</li>
    <li><code>new_ip</code> (bool, optional): Use a new TOR IP address (default is True).</li>
</ul>

<h3><code>get_tor_socks5_proxy_linux(host, port, new_ip=True)</code></h3>
<p>This method retrieves a TOR SOCKS5 proxy for Linux and returns proxy settings in the form of a dictionary. It takes the same parameters as <code>get_tor_socks5_proxy_windows</code>.</p>

<h3><code>get_tor_socks5_proxy(new_ip=True)</code></h3>
<p>This method retrieves a TOR SOCKS5 proxy based on the system platform (Windows or Linux) and returns proxy settings in the form of a dictionary. It takes the following parameters:</p>
<ul>
    <li><code>new_ip</code> (bool, optional): Use a new TOR IP address (default is True).</li>
</ul>

<h3><code>get_tor_http_proxy(host, port, new_ip=True)</code></h3>
<p>This method retrieves a TOR HTTP proxy and returns proxy settings in the form of a dictionary. It takes the following parameters:</p>
<ul>
    <li><code>host</code> (str): The IP address of the TOR HTTP proxy.</li>
    <li><code>port</code> (int): The port of the TOR HTTP proxy.</li>
    <li><code>new_ip</code> (bool, optional): Use a new TOR IP address (default is True).</li>
</ul>

<h3><code>get_requests_proxy(proxy_type=None, **kwargs)</code></h3>
<p>This method generates and returns a dictionary with proxy settings for use with the Python requests library based on the specified proxy type. It takes the following parameters:</p>
<ul>
    <li><code>proxy_type</code> (int or str, optional): The proxy type (3 for HTTP, 4 for SOCKS4, 5 for SOCKS5, or 'http', 'socks4', 'socks5', 'h', 's4', 's5' for proxy type identification).</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>Proxies_Getter</code> class, you can call its methods with the required parameters. Here's an example of using the <code>get_socks5_proxy_socket</code> method:</p>

<pre><code>
from bane.proxies import Proxies_Getter

#Establish a SOCKS5 proxy socket connection
proxy_socket = Proxies_Getter.get_socks5_proxy_socket(
    host="example.com",
    port=80,
    proxy_host="socks5-proxy.com",
    proxy_port=1080,
    proxy_username="user",
    proxy_password="password",
    no_delay=True,
    timeout=10
)

#Use the proxy_socket for further communication
if proxy_socket:
    proxy_socket.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
    response = proxy_socket.recv(1024)
    print(response)
else:
    print("Failed to establish a proxy socket connection")
</code></pre>
<h1>Proxies_Parser Class</h1>

<h2>Class Overview</h2>
<p>The <code>Proxies_Parser</code> class is part of the "bane" module and is used to parse and handle proxy configurations and settings.</p>

<h2>Class Methods</h2>

<h3><code>parse_proxy_string(s, proxy_type)</code></h3>
<p>This method parses a proxy configuration string and returns a dictionary containing proxy settings. It takes the following parameters:</p>
<ul>
    <li><code>s</code> (str): The proxy configuration string to be parsed.</li>
    <li><code>proxy_type</code> (str or int): The type of proxy (e.g., 'socks4', 'socks5', 'http') associated with the proxy string.</li>
</ul>

<h3><code>parse_proxies_list(l, proxy_type)</code></h3>
<p>This method parses a list of proxy configuration strings and returns a list of dictionaries containing proxy settings. It takes the following parameters:</p>
<ul>
    <li><code>l</code> (str, list, or tuple): The list of proxy configuration strings to be parsed.</li>
    <li><code>proxy_type</code> (str or int): The type of proxy associated with the proxy strings in the list.</li>
</ul>

<h3><code>load_and_parse_proxies(source, proxies_type)</code></h3>
<p>This method loads and parses proxy configurations from various sources, such as files, dictionaries, or strings. It returns a list of dictionaries containing proxy settings. It takes the following parameters:</p>
<ul>
    <li><code>source</code> (str, dict, list, tuple, or None): The source of proxy configurations to be parsed.</li>
    <li><code>proxies_type</code> (str or int): The type of proxy (e.g., 'socks4', 'socks5', 'http') associated with the proxy configurations.</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>Proxies_Parser</code> class, you can call its methods with the required parameters. Here's an example of using the <code>parse_proxy_string</code method:</p>

<pre><code>
from bane.proxies import Proxies_Parser

#Parse a proxy string
proxy_string = "socks5-proxy.com:1080:user:password"
proxy_type = "socks5"
parsed_proxy = Proxies_Parser.parse_proxy_string(proxy_string, proxy_type)
print(parsed_proxy)
</code></pre>

<p>Here's an example of using the <code>parse_proxies_list</code method:</p>

<pre><code>
from bane.proxies import Proxies_Parser

#Parse a list of proxy strings
proxy_strings = ["socks5-proxy.com:1080:user:password", "http-proxy.com:8080", "invalid_proxy_string"]
proxy_type = "socks5"
parsed_proxies = Proxies_Parser.parse_proxies_list(proxy_strings, proxy_type)
print(parsed_proxies)
</code></pre>

<p>And here's an example of using the <code>load_and_parse_proxies</code> method:</p>

<pre><code>
from bane.proxies import Proxies_Parser

#Load and parse proxy configurations from a file
proxy_file = "proxies.txt"
proxy_type = "http"
parsed_proxies = Proxies_Parser.load_and_parse_proxies(proxy_file, proxy_type)
print(parsed_proxies)
</code></pre>
