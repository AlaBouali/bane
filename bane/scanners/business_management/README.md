<h1>Dolibarr_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>Dolibarr_Scanner</code> class is designed to scan a Dolibarr server for information and vulnerabilities. It checks the target server for Dolibarr version, server information, subdomains, and possible vulnerabilities.</p>

<h2>Static Methods</h2>

<h3><code>scan(u, version='', user_agent=None, cookie=None, timeout=10, logs=True, crt_timeout=120, wayback_timeout=120, subdomain_check_timeout=10, max_wayback_urls=10, subdomains_only=True, headers={}, api_key=None, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This static method scans a target Dolibarr server for information and vulnerabilities. It takes the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target Dolibarr server URL to scan.</li>
    <li><code>version</code> (str): Dolibarr version (default is '').</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests (default is None).</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests (default is None).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 10).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is True).</li>
    <li><code>crt_timeout</code> (int): Timeout for CRT.sh subdomain enumeration (default is 120).</li>
    <li><code>wayback_timeout</code> (int): Timeout for Wayback Machine subdomain enumeration (default is 120).</li>
    <li><code>subdomain_check_timeout</code> (int): Timeout for subdomain availability check (default is 10).</li>
    <li><code>max_wayback_urls</code> (int): Maximum number of Wayback Machine URLs to check for subdomains (default is 10).</li>
    <li><code>subdomains_only</code> (bool): Include subdomains only in the results (default is True).</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include (default is an empty dictionary).</li>
    <li><code>api_key</code> (str): API key for vulnerability scanning (default is None).</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use (default is None).</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use (default is None).</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use (default is None).</li>
</ul>

<p>The method performs an HTTP request to the Dolibarr server and retrieves relevant information. It also checks for subdomains, performs clickjacking scans, and searches for vulnerabilities using the Vulners database.</p>

<h2>Example Usage</h2>
<p>To use the <code>Dolibarr_Scanner</code> class, call the <code>scan</code> method with the required parameters, and it will perform the Dolibarr scanning process. Here's an example:</p>

<pre><code>
from bane import Dolibarr_Scanner

#Target Dolibarr server URL
target_url = "https://example.com"

#Call the scan method
result = Dolibarr_Scanner.scan(
    target_url,
    version="8.0.1",
    user_agent="CustomUserAgent",
    cookie="CustomCookie",
    timeout=10,
    logs=True,
    crt_timeout=120,
    wayback_timeout=120,
    subdomain_check_timeout=10,
    max_wayback_urls=10,
    subdomains_only=True,
    headers={"Custom-Header": "Value"},
    http_proxies=["1.2.3.4:80"],
    socks4_proxies=["5.6.7.8:1080"],
    socks5_proxies=["9.10.11.12:1080"]
)

#Access the result
print(result)
</code></pre>



<h1>Odoo_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>Odoo_Scanner</code> class is designed to scan a Odoo server for information and vulnerabilities. It checks the target server for Odoo version, server information, subdomains, and possible vulnerabilities.</p>

<h2>Static Methods</h2>

<h3><code>scan(u, version='', user_agent=None, cookie=None, timeout=10, logs=True, crt_timeout=120, wayback_timeout=120, subdomain_check_timeout=10, max_wayback_urls=10, subdomains_only=True, headers={}, api_key=None, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This static method scans a target Odoo server for information and vulnerabilities. It takes the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target Odoo server URL to scan.</li>
    <li><code>version</code> (str): Odoo version (default is '').</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests (default is None).</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests (default is None).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 10).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is True).</li>
    <li><code>crt_timeout</code> (int): Timeout for CRT.sh subdomain enumeration (default is 120).</li>
    <li><code>wayback_timeout</code> (int): Timeout for Wayback Machine subdomain enumeration (default is 120).</li>
    <li><code>subdomain_check_timeout</code> (int): Timeout for subdomain availability check (default is 10).</li>
    <li><code>max_wayback_urls</code> (int): Maximum number of Wayback Machine URLs to check for subdomains (default is 10).</li>
    <li><code>subdomains_only</code> (bool): Include subdomains only in the results (default is True).</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include (default is an empty dictionary).</li>
    <li><code>api_key</code> (str): API key for vulnerability scanning (default is None).</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use (default is None).</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use (default is None).</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use (default is None).</li>
</ul>

<p>The method performs an HTTP request to the Odoo server and retrieves relevant information. It also checks for subdomains, performs clickjacking scans, and searches for vulnerabilities using the Vulners database.</p>

<h2>Example Usage</h2>
<p>To use the <code>Odoo_Scanner</code> class, call the <code>scan</code> method with the required parameters, and it will perform the Odoo scanning process. Here's an example:</p>

<pre><code>
from bane import Odoo_Scanner

#Target Odoo server URL
target_url = "https://example.com"

#Call the scan method
result = Odoo_Scanner.scan(
    target_url,
    version="8.0.1",
    user_agent="CustomUserAgent",
    cookie="CustomCookie",
    timeout=10,
    logs=True,
    crt_timeout=120,
    wayback_timeout=120,
    subdomain_check_timeout=10,
    max_wayback_urls=10,
    subdomains_only=True,
    headers={"Custom-Header": "Value"},
    http_proxies=["1.2.3.4:80"],
    socks4_proxies=["5.6.7.8:1080"],
    socks5_proxies=["9.10.11.12:1080"]
)

#Access the result
print(result)
</code></pre>
