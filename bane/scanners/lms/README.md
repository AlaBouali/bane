<h1>Moodle_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>Moodle_Scanner</code> class is used to scan a website for Moodle-related information and vulnerabilities. It checks the target URL for Moodle version, server information, subdomains, and possible vulnerabilities.</p>

<h2>Static Method</h2>
<h3><code>scan(u, user_agent=None, cookie=None, timeout=10, logs=True, crt_timeout=120, wayback_timeout=120, subdomain_check_timeout=10, max_wayback_urls=10, subdomains_only=True, headers={}, api_key=None, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This static method scans a target website for Moodle-related information and vulnerabilities. It takes the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target website URL to scan.</li>
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

<h2>Example Usage</h2>
<p>To use the <code>Moodle_Scanner</code> class, call the <code>scan</code> method with the required parameters, and it will perform the Moodle scanning process. Here's an example:</p>

<pre><code>
from bane.scanners.cms import Moodle_Scanner

#Target website URL
target_url = "https://example.com"

#Call the scan method
result = Moodle_Scanner.scan(
    target_url,
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
    api_key="YourAPIKey",
    http_proxies=["1.2.3.4:80"],
    socks4_proxies=["5.6.7.8:1080"],
    socks5_proxies=["9.10.11.12:1080"]
)

#Access the result
print(result)
</code></pre>
