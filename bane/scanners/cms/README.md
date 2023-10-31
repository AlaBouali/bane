<h1>Drupal_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>Drupal_Scanner</code> class is used to scan a website for Drupal-related information and vulnerabilities. It checks the target URL for Drupal version, server information, subdomains, and possible vulnerabilities.</p>

<h2>Static Method</h2>
<h3><code>scan(u, user_agent=None, cookie=None, timeout=10, logs=True, crt_timeout=120, wayback_timeout=120, subdomain_check_timeout=10, max_wayback_urls=10, subdomains_only=True, headers={}, api_key=None, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This static method scans a target website for Drupal-related information and vulnerabilities. It takes the following parameters:</p>

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
<p>To use the <code>Drupal_Scanner</code> class, call the <code>scan</code> method with the required parameters, and it will perform the Drupal scanning process. Here's an example:</p>

<pre><code>
from bane.scanners.cms import Drupal_Scanner

# Target website URL
target_url = "https://example.com"

# Call the scan method
result = Drupal_Scanner.scan(
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

# Access the result
print(result)
</code></pre>
<h1>Joomla_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>Joomla_Scanner</code> class is used to scan a website for Joomla-related information and vulnerabilities. It checks the target URL for Joomla version, server information, subdomains, and possible vulnerabilities.</p>

<h2>Static Method</h2>
<h3><code>scan(u, user_agent=None, cookie=None, timeout=10, proxy=None, logs=True, crt_timeout=120, wayback_timeout=120, subdomain_check_timeout=10, max_wayback_urls=10, subdomains_only=True, headers={}, api_key=None, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This static method scans a target website for Joomla-related information and vulnerabilities. It takes the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target website URL to scan.</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests (default is None).</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests (default is None).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 10).</li>
    <li><code>proxy</code> (dict): Proxy configuration (default is None).</li>
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
<p>To use the <code>Joomla_Scanner</code> class, call the <code>scan</code method with the required parameters, and it will perform the Joomla scanning process. Here's an example:</p>

<pre><code>
from bane.scanners.cms import Joomla_Scanner

# Target website URL
target_url = "https://example.com"

# Call the scan method
result = Joomla_Scanner.scan(
    target_url,
    user_agent="CustomUserAgent",
    cookie="CustomCookie",
    timeout=10,
    proxy=None,
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

# Access the result
print(result)
</code></pre>
<h1>Magento_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>Magento_Scanner</code> class is used to scan a website for Magento-related information and vulnerabilities. It checks the target URL for Magento version, server information, subdomains, and possible vulnerabilities.</p>

<h2>Static Method</h2>
<h3><code>scan(u, user_agent=None, cookie=None, timeout=10, proxy=None, logs=True, crt_timeout=120, wayback_timeout=120, subdomain_check_timeout=10, max_wayback_urls=10, subdomains_only=True, headers={}, api_key=None, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This static method scans a target website for Magento-related information and vulnerabilities. It takes the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target website URL to scan.</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests (default is None).</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests (default is None).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 10).</li>
    <li><code>proxy</code> (dict): Proxy configuration (default is None).</li>
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
<p>To use the <code>Magento_Scanner</code> class, call the <code>scan</code method with the required parameters, and it will perform the Magento scanning process. Here's an example:</p>

<pre><code>
from bane.scanners.cms import Magento_Scanner

# Target website URL
target_url = "https://example.com"

# Call the scan method
result = Magento_Scanner.scan(
    u=target_url,
    user_agent="CustomUserAgent",
    cookie="CustomCookie",
    timeout=10,
    proxy=None,
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

# Access the result
print(result)
</code></pre>
<h1>WordPress_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>WordPress_Scanner</code> class is used to scan a website for WordPress-related information and vulnerabilities. It checks the target URL for WordPress version, server information, subdomains, themes, plugins, and possible vulnerabilities.</p>

<h2>Static Method</h2>
<h3><code>scan(u, max_wpscan_tries=3, cookie=None, user_agent=None, timeout=20, proxy=None, user_enum_start=1, user_enum_end=20, wpscan_cookie=None, sleep_time_min=10, sleep_time_max=20, when_blocked_sleep=30, logs=True, crt_timeout=120, wayback_timeout=120, subdomain_check_timeout=10, max_wayback_urls=10, subdomains_only=True, headers={}, api_key=None, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This static method scans a target website for WordPress-related information and vulnerabilities. It takes the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target website URL to scan.</li>
    <li><code>max_wpscan_tries</code> (int): Maximum number of WPScan retries (default is 3).</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests (default is None).</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests (default is None).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 20).</li>
    <li><code>proxy</code> (dict): Proxy configuration (default is None).</li>
    <li><code>user_enum_start</code> (int): Start of user enumeration range (default is 1).</li>
    <li><code>user_enum_end</code> (int): End of user enumeration range (default is 20).</li>
    <li><code>wpscan_cookie</code> (str): Custom cookies for WPScan requests (default is None).</li>
    <li><code>sleep_time_min</code> (int): Minimum sleep time between WPScan requests (default is 10).</li>
    <li><code>sleep_time_max</code> (int): Maximum sleep time between WPScan requests (default is 20).</li>
    <li><code>when_blocked_sleep</code> (int): Sleep time when blocked by WPScan (default is 30).</li>
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
<p>To use the <code>WordPress_Scanner</code> class, call the <code>scan</code> method with the required parameters, and it will perform the WordPress scanning process. Here's an example:</p>

<pre><code>
from bane.scanners.cms import WordPress_Scanner

# Target website URL
target_url = "https://example.com"

# Call the scan method
result = WordPress_Scanner.scan(
    u=target_url,
    max_wpscan_tries=3,
    cookie="CustomCookie",
    user_agent="CustomUserAgent",
    timeout=20,
    proxy=None,
    user_enum_start=1,
    user_enum_end=20,
    wpscan_cookie=None,
    sleep_time_min=10,
    sleep_time_max=20,
    when_blocked_sleep=30,
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

# Access the result
print(result)
</code></pre>
