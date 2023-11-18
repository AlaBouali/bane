<h1>ElasticSearch_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>ElasticSearch_Scanner</code> class is designed to scan an Elasticsearch server for information and vulnerabilities. It checks the target server for Elasticsearch version, performs a basic HTTP request, and retrieves relevant vulnerability information using the Vulners database.</p>

<h2>Static Method</h2>
<h3><code>scan(u, ssl_enabled=False, timeout=5, p=9200, proxy_host=None, proxy_port=None, proxy_username=None, proxy_password=None, proxy_type=None, api_key=None)</code></h3>
<p>This static method scans a target Elasticsearch server for information and vulnerabilities. It takes the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target Elasticsearch server URL to scan.</li>
    <li><code>ssl_enabled</code> (bool): Enable SSL for the connection (default is False).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 5).</li>
    <li><code>p</code> (int): Port number for the Elasticsearch server (default is 9200).</li>
    <li><code>proxy_host</code> (str): Proxy host for the connection (default is None).</li>
    <li><code>proxy_port</code> (int): Proxy port for the connection (default is None).</li>
    <li><code>proxy_username</code> (str): Proxy username for authentication (default is None).</li>
    <li><code>proxy_password</code> (str): Proxy password for authentication (default is None).</li>
    <li><code>proxy_type</code> (str): Proxy type, e.g., 'socks4', 's4', 'socks5', 's5' (default is None).</li>
    <li><code>api_key</code> (str): API key for vulnerability scanning (default is None).</li>
</ul>

<p>If a <code>proxy_type</code> is specified, the appropriate SOCKS proxy type is determined (either SOCKS4 or SOCKS5).</p>

<p>The method performs a basic HTTP request to the Elasticsearch server and retrieves version information. It then uses the Vulners database to search for Elasticsearch-related vulnerabilities.</p>

<h2>Example Usage</h2>
<p>To use the <code>ElasticSearch_Scanner</code> class, call the <code>scan</code> method with the required parameters, and it will perform the Elasticsearch scanning process. Here's an example:</p>

<pre><code>
from bane import ElasticSearch_Scanner

#Target Elasticsearch server URL
target_url = "localhost"

#Call the scan method
result = ElasticSearch_Scanner.scan(
    target_url,
    ssl_enabled=True,
    timeout=5,
    p=9200,
    proxy_host="proxy.example.com",
    proxy_port=8080,
    proxy_username="username",
    proxy_password="password",
    proxy_type="socks5",
)

#Access the result
print(result)
</code></pre>
<h1>Grafana_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>Grafana_Scanner</code> class is designed to scan a Grafana server for information and vulnerabilities. It checks the target server for Grafana version, server information, subdomains, and possible vulnerabilities.</p>

<h2>Static Methods</h2>

<h3><code>get_version(text)</code></h3>
<p>Returns the Grafana version extracted from the provided text.</p>

<h3><code>scan(u, user_agent=None, grafana_paths=['', 'grafana'], cookie=None, timeout=10, logs=True, crt_timeout=120, wayback_timeout=120, subdomain_check_timeout=10, max_wayback_urls=10, subdomains_only=True, headers={}, api_key=None, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This static method scans a target Grafana server for information and vulnerabilities. It takes the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target Grafana server URL to scan.</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests (default is None).</li>
    <li><code>grafana_paths</code> (list): List of paths to check for Grafana (default is ['', 'grafana']).</li>
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

<p>The method performs HTTP requests to different paths to identify the Grafana version and retrieve relevant information. It also checks for subdomains, performs clickjacking scans, and searches for vulnerabilities using the Vulners database.</p>

<h2>Example Usage</h2>
<p>To use the <code>Grafana_Scanner</code> class, call the <code>scan</code> method with the required parameters, and it will perform the Grafana scanning process. Here's an example:</p>

<pre><code>
from bane import Grafana_Scanner

#Target Grafana server URL
target_url = "https://example.com"

#Call the scan method
result = Grafana_Scanner.scan(
    target_url,
    user_agent="CustomUserAgent",
    grafana_paths=['', 'grafana'],
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
