<h1>ASPNET_DAST_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>ASPNET_DAST_Scanner</code> class is designed to perform dynamic application security testing (DAST) on ASP.NET sites. It scans for known vulnerabilities using the Vulners database and provides detailed information about the ASP.NET site's configuration, version, and potential exploits.</p>

<h2>Static Method</h2>
<h3><code>scan(u, user_agent=None, cookie=None, timeout=10, logs=True, crt_timeout=120, wayback_timeout=120, subdomain_check_timeout=10, max_wayback_urls=10, subdomains_only=True, headers={}, api_key=None, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This static method initiates a DAST scan on the provided ASP.NET site. It takes various parameters for customization and returns a comprehensive report on the site's security posture. The parameters are as follows:</p>

<ul>
    <li><code>u</code> (str): The URL of the ASP.NET site to scan.</li>
    <li><code>user_agent</code> (str): User-agent string to use in HTTP requests.</li>
    <li><code>cookie</code> (str): Cookie string to include in HTTP requests.</li>
    <li><code>timeout</code> (int): Request timeout in seconds.</li>
    <li><code>logs</code> (bool): Whether to print scan information to the console.</li>
    <li><code>crt_timeout</code> (int): Timeout for certificate retrieval.</li>
    <li><code>wayback_timeout</code> (int): Timeout for Wayback Machine requests.</li>
    <li><code>subdomain_check_timeout</code> (int): Timeout for subdomain enumeration.</li>
    <li><code>max_wayback_urls</code> (int): Maximum number of Wayback Machine URLs to fetch.</li>
    <li><code>subdomains_only</code> (bool): Whether to focus on subdomain enumeration only.</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include in requests.</li>
    <li><code>api_key</code> (str): API key for accessing certain services.</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use.</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use.</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use.</li>
</ul>

<p>The method returns a detailed report containing information about the site's URL, domain, IP, server details, operating system, backend technology, ASP.NET version, vulnerabilities, and more.</p>

<h2>Example Usage</h2>
<p>To use the <code>ASPNET_DAST_Scanner</code> class, call the <code>scan</code> method with the URL of the ASP.NET site and any additional parameters needed for the scan. Here's an example:</p>

<pre><code>
from bane import ASPNET_DAST_Scanner

#Scan ASP.NET site for vulnerabilities
aspnet_scan_result = ASPNET_DAST_Scanner.scan(
    u="https://example.com",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    cookie="your_cookie_string",
    timeout=15,
    logs=True,
    crt_timeout=120,
    wayback_timeout=120,
    subdomain_check_timeout=10,
    max_wayback_urls=10,
    subdomains_only=True,
    headers={"Custom-Header": "header_value"},
    http_proxies=["http://proxy1:8080", "http://proxy2:8080"],
    socks4_proxies=["socks4://proxy3:1080"],
    socks5_proxies=["socks5://proxy4:1080"]
)

#Access the scan results
print("ASP.NET Scan Results:", aspnet_scan_result)
</code></pre>
<h1>PHP_DAST_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>PHP_DAST_Scanner</code> class is designed to perform dynamic application security testing (DAST) on PHP sites. It scans for known vulnerabilities using the Vulners database and provides detailed information about the PHP site's configuration, version, and potential exploits.</p>

<h2>Static Method</h2>
<h3><code>scan(u, user_agent=None, cookie=None, timeout=10, logs=True, crt_timeout=120, wayback_timeout=120, subdomain_check_timeout=10, max_wayback_urls=10, subdomains_only=True, headers={}, api_key=None, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This static method initiates a DAST scan on the provided PHP site. It takes various parameters for customization and returns a comprehensive report on the site's security posture. The parameters are as follows:</p>

<ul>
    <li><code>u</code> (str): The URL of the PHP site to scan.</li>
    <li><code>user_agent</code> (str): User-agent string to use in HTTP requests.</li>
    <li><code>cookie</code> (str): Cookie string to include in HTTP requests.</li>
    <li><code>timeout</code> (int): Request timeout in seconds.</li>
    <li><code>logs</code> (bool): Whether to print scan information to the console.</li>
    <li><code>crt_timeout</code> (int): Timeout for certificate retrieval.</li>
    <li><code>wayback_timeout</code> (int): Timeout for Wayback Machine requests.</li>
    <li><code>subdomain_check_timeout</code> (int): Timeout for subdomain enumeration.</li>
    <li><code>max_wayback_urls</code> (int): Maximum number of Wayback Machine URLs to fetch.</li>
    <li><code>subdomains_only</code> (bool): Whether to focus on subdomain enumeration only.</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include in requests.</li>
    <li><code>api_key</code> (str): API key for accessing certain services.</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use.</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use.</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use.</li>
</ul>

<p>The method returns a detailed report containing information about the site's URL, domain, IP, server details, operating system, backend technology, PHP version, vulnerabilities, and more.</p>

<h2>Example Usage</h2>
<p>To use the <code>PHP_DAST_Scanner</code> class, call the <code>scan</code> method with the URL of the PHP site and any additional parameters needed for the scan. Here's an example:</p>

<pre><code>
from bane import PHP_DAST_Scanner

#Scan PHP site for vulnerabilities
php_scan_result = PHP_DAST_Scanner.scan(
    u="https://example.com",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    cookie="your_cookie_string",
    timeout=15,
    logs=True,
    crt_timeout=120,
    wayback_timeout=120,
    subdomain_check_timeout=10,
    max_wayback_urls=10,
    subdomains_only=True,
    headers={"Custom-Header": "header_value"},
    http_proxies=["http://proxy1:8080", "http://proxy2:8080"],
    socks4_proxies=["socks4://proxy3:1080"],
    socks5_proxies=["socks5://proxy4:1080"]
)

#Access the scan results
print("PHP Scan Results:", php_scan_result)
</code></pre>

<h1>Ruby_DAST_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>Ruby_DAST_Scanner</code> class is designed to perform dynamic application security testing (DAST) on Ruby on Rails sites. It scans for known vulnerabilities using the Vulners database and provides detailed information about the Ruby on Rails site's configuration, versions, and potential exploits.</p>

<h2>Static Methods</h2>

<h3><code>get_details(text)</code></h3>
<p>This method extracts details from the HTML content of a Ruby on Rails site. It looks for information in a table and returns a dictionary containing various details.</p>

<h3><code>get_ruby_version(text)</code></h3>
<p>Extracts the Ruby version from the HTML content of a Ruby on Rails site.</p>

<h3><code>get_Rails_version(text)</code></h3>
<p>Extracts the Rails version from the HTML content of a Ruby on Rails site.</p>

<h3><code>get_RubyGems_version(text)</code></h3>
<p>Extracts the RubyGems version from the HTML content of a Ruby on Rails site.</p>

<h3><code>scan(u, user_agent=None, cookie=None, timeout=10, logs=True, crt_timeout=120, wayback_timeout=120, subdomain_check_timeout=10, max_wayback_urls=10, subdomains_only=True, headers={}, api_key=None, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This static method initiates a DAST scan on the provided Ruby on Rails site. It takes various parameters for customization and returns a comprehensive report on the site's security posture. The parameters are similar to those used in other DAST scanner classes.</p>

<p>The method returns a detailed report containing information about the site's URL, domain, IP, server details, operating system, backend technology, Rails version, installation details, vulnerabilities, and more.</p>

<h2>Example Usage</h2>
<p>To use the <code>Ruby_DAST_Scanner</code> class, call the <code>scan</code> method with the URL of the Ruby on Rails site and any additional parameters needed for the scan. Here's an example:</p>

<pre><code>
from bane import Ruby_DAST_Scanner

#Scan Ruby on Rails site for vulnerabilities
rails_scan_result = Ruby_DAST_Scanner.scan(
    u="https://example.com",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    cookie="your_cookie_string",
    timeout=15,
    logs=True,
    crt_timeout=120,
    wayback_timeout=120,
    subdomain_check_timeout=10,
    max_wayback_urls=10,
    subdomains_only=True,
    headers={"Custom-Header": "header_value"},
    api_key="YourAPIKey",
    http_proxies=["http://proxy1:8080", "http://proxy2:8080"],
    socks4_proxies=["socks4://proxy3:1080"],
    socks5_proxies=["socks5://proxy4:1080"]
)

#Access the scan results
print("Ruby on Rails Scan Results:", rails_scan_result)
</code></pre>
