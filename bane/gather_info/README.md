<h1>Domain_Info Class</h1>

<h2>Class Overview</h2>
<p>The <code>Domain_Info</code> class is part of the "bane" module and provides methods for gathering information about a domain, including WHOIS data, domain information, and DNS resolution.</p>

<h2>Class Methods</h2>

<h3><code>whois(u, proxy=None, cookie=None, user_agent=None, timeout=10, headers={})</code></h3>
<p>This method retrieves WHOIS information for a domain.</p>

<p>Parameters:</p>
<ul>
    <li><code>u</code> (str): The domain to perform a WHOIS lookup on.</li>
    <li><code>proxy</code> (dict, optional): HTTP and/or HTTPS proxy configuration. Example: {"http": "http://1.2.3.4:80", "https": "http://1.2.3.4:80"}</li>
    <li><code>cookie</code> (str, optional): Custom cookies to include in requests.</li>
    <li><code>user_agent</code> (str, optional): Custom User-Agent header for requests.</li>
    <li><code>timeout</code> (int, optional): Request timeout in seconds (default is 10).</li>
    <li><code>headers</code> (dict, optional): Additional HTTP headers to include in the request.</li>
</ul>

<h3><code>info(u, timeout=10, proxy=None, user_agent=None, cookie=None, headers={})</code></h3>
<p>This method gathers domain information, such as geolocation data, from a website.</p>

<p>Parameters:</p>
<ul>
    <li><code>u</code> (str): The domain for which to gather information.</li>
    <li><code>timeout</code> (int, optional): Request timeout in seconds (default is 10).</li>
    <li><code>proxy</code> (dict, optional): HTTP and/or HTTPS proxy configuration.</li>
    <li><code>user_agent</code> (str, optional): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str, optional): Custom cookies to include in requests.</li>
    <li><code>headers</code> (dict, optional): Additional HTTP headers to include in the request.</li>
</ul>

<h3><code>resolve(u, server="8.8.8.8", timeout=1, lifetime=1)</code></h3>
<p>This method performs DNS resolution for a given domain.</p>

<p>Parameters:</p>
<ul>
    <li><code>u</code> (str): The domain to perform DNS resolution on.</li>
    <li><code>server</code> (str, optional): DNS server IP address (default is "8.8.8.8").</li>
    <li><code>timeout</code> (int, optional): Resolver timeout in seconds (default is 1).</li>
    <li><code>lifetime</code> (int, optional): Resolver lifetime in seconds (default is 1).</li>
</ul>

<h3><code>get_domain_info(domain, headers={}, timeout=10, proxy=None, user_agent=None, cookie=None, resolve_server='8.8.8.8', resolve_timeout=1, resolve_lifetime=1)</code></h3>
<p>This method combines the results of WHOIS data, domain information, and DNS resolution for a domain into a dictionary.</p>

<p>Parameters:</p>
<ul>
    <li><code>domain</code> (str): The domain for which to gather information.</li>
    <li><code>headers</code> (dict, optional): Additional HTTP headers to include in the requests.</li>
    <li><code>timeout</code> (int, optional): Request timeout in seconds (default is 10).</li>
    <li><code>proxy</code> (dict, optional): HTTP and/or HTTPS proxy configuration.</li>
    <li><code>user_agent</code> (str, optional): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str, optional): Custom cookies to include in requests.</li>
    <li><code>resolve_server</code> (str, optional): DNS server IP address for DNS resolution (default is "8.8.8.8").</li>
    <li><code>resolve_timeout</code> (int, optional): Resolver timeout in seconds (default is 1).</li>
    <li><code>resolve_lifetime</code> (int, optional): Resolver lifetime in seconds (default is 1).</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>Domain_Info</code> class, you can call its methods to gather information about a domain. Here's an example:</p>

<pre><code>
from bane.gather_info import Domain_Info

#Example domain for information gathering
domain = "example.com"

#Gather domain information
info = Domain_Info.get_domain_info(
    domain,
    headers={"Custom-Header": "Value"},
    timeout=10,
    proxy={"http": "http://1.2.3.4:80", "https": "http://1.2.3.4:80"},
    user_agent="CustomUserAgent",
    cookie="CustomCookie",
    resolve_server="8.8.8.8",
    resolve_timeout=1,
    resolve_lifetime=1
)

#Access the gathered information
print("Resolved Hosts:", info["resolved_host"])
print("Domain Information:", info["info"])
print("WHOIS Information:", info["whois"])
</code></pre>
<h1>Dorking_Info Class</h1>

<h2>Class Overview</h2>
<p>The <code>Dorking_Info</code> class provides a method for performing Google dork searches to find URLs related to a specific query.</p>

<h2>Class Methods</h2>

<h3><code>google(q, max_results=100, language="en", start_from=1, stop_on=None, top_level_domain="com", pause=2)</code></h3>
<p>This method performs a Google dork search to find URLs related to a specific query.</p>

<p>Parameters:</p>
<ul>
    <li><code>q</code> (str): The query for the Google dork search.</li>
    <li><code>max_results</code> (int, optional): The maximum number of results to retrieve (default is 100).</li>
    <li><code>language</code> (str, optional): The language in which to perform the search (default is "en" for English).</li>
    <li><code>start_from</code> (int, optional): The starting result index (default is 1).</li>
    <li><code>stop_on</code> (int, optional): The index at which to stop the search (default is None, meaning no stopping point).</li>
    <li><code>top_level_domain</code> (str, optional): The top-level domain to limit the search to (default is "com").</li>
    <li><code>pause</code> (int, optional): The delay between making HTTP requests to Google (default is 2 seconds).</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>Dorking_Info</code> class, call its <code>google</code> method to perform a Google dork search. Here's an example:</p>

<pre><code>
from bane.gather_info import Dorking_Info

#Perform a Google dork search for a specific query
query = "example query"
results = Dorking_Info.google(
    q=query,
    max_results=50,
    language="en",
    start_from=1,
    stop_on=None,
    top_level_domain="com",
    pause=2
)

#Access the list of URLs related to the query
for result in results:
    print(result)
</code></pre>
<h1>IP_Info Class</h1>

<h2>Class Overview</h2>
<p>The <code>IP_Info</code> class in the "bane" module provides methods for gathering information related to IP addresses, including obtaining your own IP, geolocation information, reverse IP lookup, and Shodan reports.</p>

<h2>Class Methods</h2>

<h3><code>my_ip(proxy=None, timeout=15)</code></h3>
<p>This method is used to retrieve your own IP address using the ipify.org service.</p>

<p>Parameters:</p>
<ul>
    <li><code>proxy</code> (dict, optional): HTTP and/or HTTPS proxy configuration.</li>
    <li><code>timeout</code> (int, optional): Request timeout in seconds (default is 15).</li>
</ul>

<h3><code>geo_ip(u, timeout=15, proxy=None)</code></h3>
<p>This method retrieves geolocation information for a given IP address.</p>

<p>Parameters:</p>
<ul>
    <li><code>u</code> (str): The IP address for which to gather geolocation information.</li>
    <li><code>timeout</code> (int, optional): Request timeout in seconds (default is 15).</li>
    <li><code>proxy</code> (dict, optional): HTTP and/or HTTPS proxy configuration.</li>
</ul>

<h3><code>reverse_ip_lookup(u, timeout=10, proxy=None)</code></h3>
<p>This method performs a reverse IP lookup to find domains associated with a given IP address.</p>

<p>Parameters:</p>
<ul>
    <li><code>u</code> (str): The IP address for which to perform a reverse IP lookup.</li>
    <li><code>timeout</code> (int, optional): Request timeout in seconds (default is 10).</li>
    <li><code>proxy</code> (dict, optional): HTTP and/or HTTPS proxy configuration.</li>
</ul>

<h3><code>check_ip_via_shodan(ip, proxy=None, timeout=15, logs=False)</code></h3>
<p>This method checks information related to an IP address using Shodan and returns details such as common vulnerabilities and exposures (CVEs).</p>

<p>Parameters:</p>
<ul>
    <li><code>ip</code> (str): The IP address for which to check information.</li>
    <li><code>proxy</code> (dict, optional): HTTP and/or HTTPS proxy configuration.</li>
    <li><code>timeout</code> (int, optional): Request timeout in seconds (default is 15).</li>
    <li><code>logs</code> (bool, optional): Enable or disable logging (default is False).</li>
</ul>

<h3><code>get_IP_Info(ip, timeout=15, proxy=None)</code></h3>
<p>This method combines the results of geolocation information, reverse IP lookup, and Shodan reports for a given IP address into a dictionary.</p>

<p>Parameters:</p>
<ul>
    <li><code>ip</code> (str): The IP address for which to gather information.</li>
    <li><code>timeout</code> (int, optional): Request timeout in seconds (default is 15).</li>
    <li><code>proxy</code> (dict, optional): HTTP and/or HTTPS proxy configuration.</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>IP_Info</code> class, call its methods to gather information about IP addresses. Here's an example:</p>

<pre><code>
from bane.gather_info import IP_Info

#Example IP address for information gathering
ip_address = "192.168.1.1"

#Gather IP information
info = IP_Info.get_IP_info(
    ip=ip_address,
    timeout=15,
    proxy={"http": "http://1.2.3.4:80", "https": "http://1.2.3.4:80"}
)

#Access the gathered information
print("Geolocation Information:", info["geo_ip_location"])
print("Reverse IP Lookup:", info["reverse_ip_lookup"])
print("Shodan Report:", info["shodan_report"])
</code></pre>
<h1>Network_Info Class</h1>

<h2>Class Overview</h2>
<p>The <code>Network_Info</code> class in the "bane" module provides methods for network-related tasks, including retrieving local IP addresses, checking if a host is alive, performing TCP port scanning, and obtaining banners from network services.</p>

<h2>Class Methods</h2>

<h3><code>get_local_ip()</code></h3>
<p>This method retrieves the local IP address of the machine.</p>

<h3><code>host_alive(target)</code></h3>
<p>This method checks if a host is alive by sending ICMP echo requests (ping).</p>

<p>Parameters:</p>
<ul>
    <li><code>target</code> (str): The target host to check.</li>
</ul>

<h3><code>close_socket(soc)</code></h3>
<p>This method closes a network socket gracefully.</p>

<p>Parameters:</p>
<ul>
    <li><code>soc</code> (socket): The socket to close.</li>
</ul>

<h3><code>tcp_scan(ip, port=1, timeout=2, proxy_type=None, proxy_host=None, proxy_port=None, proxy_username=None, proxy_password=None)</code></h3>
<p>This method performs a TCP port scan on a given IP address to check if a specific port is open.</p>

<p>Parameters:</p>
<ul>
    <li><code>ip</code> (str): The IP address to scan.</li>
    <li><code>port</code> (int, optional): The port to check (default is 1).</li>
    <li><code>timeout</code> (int, optional): Scan timeout in seconds (default is 2).</li>
    <li><code>proxy_type</code> (str, optional): Type of proxy to use (e.g., 'socks4', 'socks5', 'http').</li>
    <li><code>proxy_host</code> (str, optional): Proxy server hostname or IP address.</li>
    <li><code>proxy_port</code> (int, optional): Proxy server port.</li>
    <li><code>proxy_username</code> (str, optional): Username for proxy authentication.</li>
    <li><code>proxy_password</code> (str, optional): Password for proxy authentication.</li>
</ul>

<h3><code>get_banner(u, p=23, timeout=3, payload=None, **kwargs)</code></h3>
<p>This method retrieves banners from network services, typically using Telnet.</p>

<p>Parameters:</p>
<ul>
    <li><code>u</code> (str): The target host to connect to.</li>
    <li><code>p</code> (int, optional): The port to connect to (default is 23).</li>
    <li><code>timeout</code> (int, optional): Connection timeout in seconds (default is 3).</li>
    <li><code>payload</code> (str, optional): Additional payload to send to the target.</li>
    <li><code>**kwargs</code>: Additional keyword arguments for Telnet connection settings.</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>Network_Info</code> class, call its methods for network-related tasks. Here's an example:</p>

<pre><code>
from bane.gather_info import Network_Info

#Retrieve local IP address
local_ip = Network_Info.get_local_ip()
print("Local IP Address:", local_ip)

#Check if a host is alive
target_host = "example.com"
is_alive = Network_Info.host_alive(target_host)
print("Host Is Alive:", is_alive)

#Perform TCP port scanning
ip_to_scan = "192.168.1.1"
port_to_scan = 80
is_port_open = Network_Info.tcp_scan(ip_to_scan, port=port_to_scan)
print(f"Port {port_to_scan} Is Open:", is_port_open)

#Get a banner from a network service
target_host = "example.com"
port_to_connect = 23
banner = Network_Info.get_banner(target_host, p=port_to_connect)
print("Service Banner:", banner)
</code></pre>
<h1>Subdomain_Info Class</h1>

<h2>Class Overview</h2>
<p>The <code>Subdomain_Info</code> class in the "bane" module provides methods for extracting and analyzing subdomains associated with a given domain. It can fetch subdomains from sources like crt.sh and the Wayback Machine, allowing you to discover subdomains for a target domain.</p>

<h2>Class Methods</h2>

<h3><code>extract_root_domain(subdomain)</code></h3>
<p>This method extracts the root domain from a subdomain.</p>

<p>Parameters:</p>
<ul>
    <li><code>subdomain</code> (str): The subdomain to extract the root domain from.</li>
</ul>

<h3><code>subdomains_crt(domain, dns_server='8.8.8.8', resolve_timeout=2, resolve_lifetime=1, logs=True, subdomain_check_timeout=10, crt_timeout=120, cookie=None, user_agent=None, proxy=None, subdomains_only=False)</code></h3>
<p>This method retrieves subdomains for a given domain from crt.sh.</p>

<p>Parameters:</p>
<ul>
    <li><code>domain</code> (str): The target domain to fetch subdomains for.</li>
    <li><code>dns_server</code> (str, optional): DNS server for resolving subdomains (default is '8.8.8.8').</li>
    <li><code>resolve_timeout</code> (int, optional): DNS resolve timeout in seconds (default is 2).</li>
    <li><code>resolve_lifetime</code> (int, optional): DNS resolve lifetime in seconds (default is 1).</li>
    <li><code>logs</code> (bool, optional): Enable or disable logging (default is True).</li>
    <li><code>subdomain_check_timeout</code> (int, optional): Subdomain check timeout in seconds (default is 10).</li>
    <li><code>crt_timeout</code> (int, optional): CRT.sh request timeout in seconds (default is 120).</li>
    <li><code>cookie</code> (str, optional): Custom cookies to include in requests.</li>
    <li><code>user_agent</code> (str, optional): Custom User-Agent header for requests.</li>
    <li><code>proxy</code> (dict, optional): HTTP/HTTPS proxy settings.</li>
    <li><code>subdomains_only</code> (bool, optional): Return subdomains only, not the associated URLs (default is False).</li>
</ul>

<h3><code>get_subdomains_from_wayback(domain, dns_server='8.8.8.8', resolve_timeout=2, resolve_lifetime=1, logs=True, user_agent=None, cookie=None, wayback_timeout=50, subdomain_check_timeout=10, max_urls=10, subdomains_only=False, proxy=None)</code></h3>
<p>This method retrieves subdomains for a given domain from the Wayback Machine.</p>

<p>Parameters:</p>
<ul>
    <li><code>domain</code> (str): The target domain to fetch subdomains for.</li>
    <li><code>dns_server</code> (str, optional): DNS server for resolving subdomains (default is '8.8.8.8').</li>
    <li><code>resolve_timeout</code> (int, optional): DNS resolve timeout in seconds (default is 2).</li>
    <li><code>resolve_lifetime</code> (int, optional): DNS resolve lifetime in seconds (default is 1).</li>
    <li><code>logs</code> (bool, optional): Enable or disable logging (default is True).</li>
    <li><code>user_agent</code> (str, optional): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str, optional): Custom cookies to include in requests.</li>
    <li><code>wayback_timeout</code> (int, optional): Wayback Machine request timeout in seconds (default is 50).</li>
    <li><code>subdomain_check_timeout</code> (int, optional): Subdomain check timeout in seconds (default is 10).</li>
    <li><code>max_urls</code> (int, optional): Maximum URLs to fetch for each subdomain (default is 10).</li>
    <li><code>subdomains_only</code> (bool, optional): Return subdomains only, not the associated URLs (default is False).</li>
    <li><code>proxy</code> (dict, optional): HTTP/HTTPS proxy settings.</li>
</ul>

<h3><code>get_subdomains(domain, dns_server='8.8.8.8', resolve_timeout=2, resolve_lifetime=1, logs=True, crt_timeout=120, user_agent=None, cookie=None, wayback_timeout=120, subdomain_check_timeout=10, max_wayback_urls=10, proxy=None, subdomains_only=False)</code></h3>
<p>This method combines subdomains fetched from both CRT.sh and the Wayback Machine.</p>

<p>Parameters:</p>
<ul>
    <li><code>domain</code> (str): The target domain to fetch subdomains for.</li>
    <li><code>dns_server</code> (str, optional): DNS server for resolving subdomains (default is '8.8.8.8').</li>
    <li><code>resolve_timeout</code> (int, optional): DNS resolve timeout in seconds (default is 2).</li>
    <li><code>resolve_lifetime</code> (int, optional): DNS resolve lifetime in seconds (default is 1).</li>
    <li><code>logs</code> (bool, optional): Enable or disable logging (default is True).</li>
    <li><code>crt_timeout</code> (int, optional): CRT.sh request timeout in seconds (default is 120).</li>
    <li><code>user_agent</code> (str, optional): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str, optional): Custom cookies to include in requests.</li>
    <li><code>wayback_timeout</code> (int, optional): Wayback Machine request timeout in seconds (default is 120).</li>
    <li><code>subdomain_check_timeout</code> (int, optional): Subdomain check timeout in seconds (default is 10).</li>
    <li><code>max_wayback_urls</code> (int, optional): Maximum Wayback Machine URLs to fetch for each subdomain (default is 10).</li>
    <li><code>proxy</code> (dict, optional): HTTP/HTTPS proxy settings.</li>
    <li><code>subdomains_only</code> (bool, optional): Return subdomains only, not the associated URLs (default is False).</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>Subdomain_Info</code> class, call its methods to extract subdomains and perform subdomain discovery. Here's an example:</p>

<pre><code>
from bane.gather_info import Subdomain_Info

#Fetch subdomains from CRT.sh
target_domain = "example.com"
subdomains_crt = Subdomain_Info.subdomains_crt(target_domain)
print("Subdomains from CRT.sh:", subdomains_crt)

#Fetch subdomains from the Wayback Machine
subdomains_wayback = Subdomain_Info.get_subdomains_from_wayback(target_domain)
print("Subdomains from Wayback Machine:", subdomains_wayback)

#Combine subdomains from CRT.sh and Wayback Machine
subdomains_combined = Subdomain_Info.get_subdomains(target_domain)
print("Combined Subdomains:", subdomains_combined)
</code></pre>
</p>
<h1>URL_Info Class</h1>

<h2>Class Overview</h2>
<p>The <code>URL_Info</code> class in the "bane" module provides methods for performing security checks, deep inspection, and HTTP OPTIONS requests on a given URL. You can use these methods to analyze and gather information about a specific URL, such as its security status, response headers, and more.</p>

<h2>Class Methods</h2>

<h3><code>security_check(url, timeout=25, proxy=None, user_agent=None, cookie=None, headers={})</code></h3>
<p>This method performs a security check on a given URL using Sucuri's SiteCheck service.</p>

<p>Parameters:</p>
<ul>
    <li><code>url</code> (str): The URL to perform a security check on.</li>
    <li><code>timeout</code> (int, optional): Request timeout in seconds (default is 25).</li>
    <li><code>proxy</code> (dict, optional): HTTP/HTTPS proxy settings.</li>
    <li><code>user_agent</code> (str, optional): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str, optional): Custom cookies to include in requests.</li>
    <li><code>headers</code> (dict, optional): Custom headers to include in the request.</li>
</ul>

<h3><code>deep_inspect(url, timeout=25, proxy=None, user_agent=None, cookie=None, headers={})</code></h3>
<p>This method performs a deep inspection of a URL using Cloudflare Radar's scanning service.</p>

<p>Parameters:</p>
<ul>
    <li><code>url</code> (str): The URL to perform deep inspection on.</li>
    <li><code>timeout</code> (int, optional): Request timeout in seconds (default is 25).</li>
    <li><code>proxy</code> (dict, optional): HTTP/HTTPS proxy settings.</li>
    <li><code>user_agent</code> (str, optional): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str, optional): Custom cookies to include in requests.</li>
    <li><code>headers</code> (dict, optional): Custom headers to include in the request.</li>
</ul>

<h3><code>http_options(u, timeout=10, user_agent=None, cookie=None, headers=None, proxy=None)</code></h3>
<p>This method performs an HTTP OPTIONS request on a given URL to retrieve specific headers.</p>

<p>Parameters:</p>
<ul>
    <li><code>u</code> (str): The URL to send the OPTIONS request to.</li>
    <li><code>timeout</code> (int, optional): Request timeout in seconds (default is 10).</li>
    <li><code>user_agent</code> (str, optional): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str, optional): Custom cookies to include in requests.</li>
    <li><code>headers</code> (dict, optional): Custom headers to include in the request.</li>
    <li><code>proxy</code> (dict, optional): HTTP/HTTPS proxy settings.</li>
</ul>

<h3><code>headers(u, timeout=10, user_agent=None, cookie=None, headers=None, proxy=None)</code></h3>
<p>This method retrieves response headers from a given URL.</p>

<p>Parameters:</p>
<ul>
    <li><code>u</code> (str): The URL to retrieve response headers from.</li>
    <li><code>timeout</code> (int, optional): Request timeout in seconds (default is 10).</li>
    <li><code>user_agent</code> (str, optional): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str, optional): Custom cookies to include in requests.</li>
    <li><code>headers</code> (dict, optional): Custom headers to include in the request.</li>
    <li><code>proxy</code> (dict, optional): HTTP/HTTPS proxy settings.</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>URL_Info</code> class, call its methods to perform security checks, deep inspection, HTTP OPTIONS requests, and retrieve response headers for a given URL. Here's an example:</p>

<pre><code>
from bane.gather_info import URL_Info

#Perform a security check on a URL
url = "https://example.com"
security_report = URL_Info.security_check(url)
print("Security Check:", security_report)

#Perform a deep inspection on a URL
deep_inspection = URL_Info.deep_inspect(url)
print("Deep Inspection:", deep_inspection)

#Perform an HTTP OPTIONS request on a URL
options_headers = URL_Info.http_options(url)
print("HTTP OPTIONS Headers:", options_headers)

#Retrieve response headers from a URL
response_headers = URL_Info.headers(url)
print("Response Headers:", response_headers)
</code></pre>
</p>
