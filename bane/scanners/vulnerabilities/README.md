<h1>ADB_Exploit_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>ADB_Exploit_Scanner</code> class is part of the "bane" module and is used to scan for Android Debug Bridge (ADB) vulnerabilities on a target device.</p>

<h2>Class Method</h2>
<pre><code>scan(u, timeout=5, p=5555, proxy_host=None, proxy_port=None, proxy_username=None, proxy_password=None, proxy_type=None)
</code></pre>
<p>This method performs an ADB exploit scan with the specified parameters. It takes the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target device's IP address or hostname.</li>
    <li><code>timeout</code> (int): Connection timeout in seconds (default is 5).</li>
    <li><code>p</code> (int): Port for the ADB service (default is 5555).</li>
    <li><code>proxy_host</code> (str): Hostname or IP address of the proxy server (default is None).</li>
    <li><code>proxy_port</code> (int): Port of the proxy server (default is None).</li>
    <li><code>proxy_username</code> (str): Username for proxy authentication (default is None).</li>
    <li><code>proxy_password</code> (str): Password for proxy authentication (default is None).</li>
    <li><code>proxy_type</code> (str): Type of proxy (either 'socks4', 's4', 'socks5', 's5', or None).</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>ADB_Exploit_Scanner</code> class, create an instance of it by providing the required parameters, and call the <code>scan</code> method. Here's an example:</p>

<pre><code>
from bane.scanners.vulnerabilities import ADB_Exploit_Scanner

#Create an instance of ADB_Exploit_Scanner and perform the scan
target_device = "192.168.1.100"
scan_result = ADB_Exploit_Scanner.scan(target_device, timeout=10, p=5555, proxy_host="proxy.example.com", proxy_port=8080, proxy_type="socks5")

#Check the result of the scan
if scan_result:
    print(f"ADB exploit vulnerability found on {}.".format(target_device))
else:
    print(f"No ADB exploit vulnerability found on {}.".format(target_device))
</code></pre>
<h1>Backend_Technologies_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>Backend_Technologies_Scanner</code> class is part of the "bane" module and is used to scan web applications for information about the backend technologies and potential vulnerabilities associated with them.</p>

<h2>Class Method</h2>
<pre><code>scan(u, timeout=10, user_agent=None, cookie=None, logs=True, request_headers=None, headers={}, api_key=None, http_proxies=None, socks4_proxies=None, socks5_proxies=None)
</code></pre>
<p>This method performs a backend technology scan on the target URL with the specified parameters. It takes the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target URL to scan.</li>
    <li><code>timeout</code> (int): Connection timeout in seconds (default is 10).</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is True).</li>
    <li><code>request_headers</code> (dict): Custom request headers to include.</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include.</li>
    <li><code>api_key</code> (str): API key for vulnerability scanning (default is None).</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use.</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use.</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use.</li>
</ul>

<h2>Method Description</h2>
<p>The <code>scan</code> method retrieves information about the target URL's server and backend technologies. It also searches for known vulnerabilities related to these technologies. The results are returned as a dictionary containing the following information:</p>

<ul>
    <li><code>shodan_report</code> (dict): Shodan report for the target IP address, obtained via the Shodan API.</li>
    <li><code>server_exploits</code> (dict): Exploits associated with the server software used by the target.</li>
    <li><code>backend_technology_exploits</code> (dict): Exploits associated with the backend technology used by the target.</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>Backend_Technologies_Scanner</code> class, create an instance of it by providing the required parameters and call the <code>scan</code> method. Here's an example:</p>

<pre><code>
from bane.scanners.vulnerabilities import Backend_Technologies_Scanner

#Define the target URL
target_url = "https://example.com"

#Create an instance of Backend_Technologies_Scanner and perform the scan
scan_result = Backend_Technologies_Scanner.scan(
    u=target_url,
    timeout=10,
    user_agent="CustomUserAgent",
    cookie="CustomCookie",
    logs=True,
    request_headers=None,
    headers={"Custom-Header": "Value"},
    api_key="YourAPIKey",
    http_proxies=["1.2.3.4:80"],
    socks4_proxies=["5.6.7.8:1080"],
    socks5_proxies=["9.10.11.12:1080"]
)

#Access the scan results
shodan_report = scan_result['shodan_report']
server_exploits = scan_result['server_exploits']
backend_technology_exploits = scan_result['backend_technology_exploits']

#Print or process the results as needed
print("Shodan Report:", shodan_report)
print("Server Exploits:", server_exploits)
print("Backend Technology Exploits:", backend_technology_exploits)
</code></pre>
<h1>ClickJacking_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>ClickJacking_Scanner</code> class is part of the "bane" module and is used to scan a web page for Clickjacking protection headers and determine if Clickjacking is possible.</p>

<h2>Class Method</h2>
<pre><code>scan(u, proxy=None, timeout=10, user_agent=None, cookie=None, logs=False, request_headers=None, headers={}, http_proxies=None, socks4_proxies=None, socks5_proxies=None)
</code></pre>
<p>This method performs a Clickjacking scan on the target URL with the specified parameters. It takes the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target URL to scan for Clickjacking protection headers.</li>
    <li><code>proxy</code> (dict): Proxy settings (default is None).</li>
    <li><code>timeout</code> (int): Connection timeout in seconds (default is 10).</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is False).</li>
    <li><code>request_headers</code> (dict): Custom request headers to include.</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include.</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use.</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use.</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use.</li>
</ul>

<h2>Method Description</h2>
<p>The <code>scan</code> method sends an HTTP request to the target URL and checks if the Clickjacking protection header "X-Frame-Options" is present in the response headers. If the header is missing, Clickjacking may be possible, and the method returns <code>True</code>. If the header is present, Clickjacking is not possible, and the method returns <code>False</code>. If requested, it also logs the response headers for analysis.</p>

<h2>Example Usage</h2>
<p>To use the <code>ClickJacking_Scanner</code> class, create an instance of it by providing the required parameters and call the <code>scan</code> method. Here's an example:</p>

<pre><code>
from bane.scanners.vulnerabilities import ClickJacking_Scanner

#Define the target URL
target_url = "https://example.com"

#Create an instance of ClickJacking_Scanner and perform the scan
clickjacking_possible = ClickJacking_Scanner.scan(
    u=target_url,
    proxy=None,
    timeout=10,
    user_agent="CustomUserAgent",
    cookie="CustomCookie",
    logs=True,
    request_headers=None,
    headers={"Custom-Header": "Value"},
    http_proxies=["1.2.3.4:80"],
    socks4_proxies=["5.6.7.8:1080"],
    socks5_proxies=["9.10.11.12:1080"]
)

#Check if Clickjacking is possible
if clickjacking_possible:
    print("Clickjacking may be possible on", target_url)
else:
    print("Clickjacking is not possible on", target_url)
</code></pre>
<h1>CORS_Misconfiguration_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>CORS_Misconfiguration_Scanner</code> class is part of the "bane" module and is used to detect Cross-Origin Resource Sharing (CORS) misconfigurations in web applications.</p>

<h2>Methods</h2>

<h3><code>cors_misconfigurations_urls()</code></h3>
<p>Method to test for CORS misconfigurations in different scenarios.</p>

<h4>Parameters</h4>
<ul>
    <li><code>u</code> (str): The URL to test for CORS misconfigurations.</li>
    <li><code>origin</code> (str): The origin domain (default is 'www.evil-domain.com').</li>
    <li><code>origin_reflection</code> (bool): Test for CORS origin reflection (default is True).</li>
    <li><code>wildcard_origin</code> (bool): Test for CORS wildcard origin (default is True).</li>
    <li><code>null_origin</code> (bool): Test for CORS null origin (default is True).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 10).</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is True).</li>
    <li><code>debug</code> (bool): Enable or disable debug mode (default is False).</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include.</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use.</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use.</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use.</li>
</ul>

<h3><code>scan()</code></h3>
<p>Method to scan a list of URLs for CORS misconfigurations.</p>

<h4>Parameters</h4>
<ul>
    <li><code>urls</code> (list): List of URLs to scan for CORS misconfigurations.</li>
    <li><code>origin</code> (str): The origin domain (default is 'www.evil-domain.com').</li>
    <li><code>origin_reflection</code> (bool): Test for CORS origin reflection (default is True).</li>
    <li><code>wildcard_origin</code> (bool): Test for CORS wildcard origin (default is True).</li>
    <li><code>null_origin</code> (bool): Test for CORS null origin (default is True).</li>
    <li><code>proxy</code> (dict): Proxy settings (HTTP/HTTPS).</li>
    <li><code>proxies</code> (list): List of proxies to use for requests.</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 10).</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is True).</li>
    <li><code>debug</code> (bool): Enable or disable debug mode (default is False).</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include.</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use.</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use.</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use.</li>
</ul>

<h2>Example Usage</h2>
<p>To utilize the <code>CORS_Misconfiguration_Scanner</code> class to scan URLs for CORS misconfigurations, follow this example:</p>

<pre><code>
from bane.scanners.vulnerabilities import CORS_Misconfiguration_Scanner

#List of URLs to scan
urls_to_scan = ["https://example.com/page1", "https://example.com/page2"]

#Scan for CORS misconfigurations
results = CORS_Misconfiguration_Scanner.scan(
    urls=urls_to_scan,
    origin="www.evil-domain.com",
    origin_reflection=True,
    wildcard_origin=True,
    null_origin=True,
    proxy={"http": "http://1.2.3.4:80", "https": "http://1.2.3.4:80"},
    proxies=["1.2.3.4:80"],
    socks4_proxies=["5.6.7.8:1080"],
    socks5_proxies=["9.10.11.12:1080"],
    timeout=10,
    user_agent="CustomUserAgent",
    cookie="CustomCookie",
    logs=True,
    debug=False,
    headers={"Custom-Header": "Value"}
)

#Display vulnerable URLs
for result in results:
    print("Vulnerable URL:", result['page'])
</code></pre>
<h1>CRLF_Injection_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>CRLF_Injection_Scanner</code> class is part of the "bane" module and is used to detect potential CRLF (Carriage Return Line Feed) injection vulnerabilities in web applications.</p>

<h2>Methods</h2>

<h3><code>set_requests()</code></h3>
<p>Method to perform HTTP requests with specified parameters.</p>

<h4>Parameters</h4>
<ul>
    <li><code>u</code> (str): URL for the HTTP request.</li>
    <li><code>method</code> (str): HTTP method for the request (default is 'GET').</li>
    <li><code>data</code> (dict): Data to be sent in the request.</li>
    <li><code>files</code> (dict): Files to be sent in the request.</li>
    <li><code>params</code> (dict): URL parameters.</li>
    <li><code>headers</code> (dict): HTTP headers.</li>
    <li><code>proxy</code> (dict): Proxy settings.</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 15).</li>
    <li><code>shuffle_headers</code> (bool): Shuffle headers (default is False).</li>
</ul>

<h3><code>crlf_unicode_encode()</code></h3>
<p>Method to create CRLF Unicode encoding based on parameters.</p>

<h4>Parameters</h4>
<ul>
    <li><code>random_level</code> (int): Level of randomness for encoding.</li>
    <li><code>line_feed_only</code> (bool): Use only Line Feed character.</li>
    <li><code>carriage_return_only</code> (bool): Use only Carriage Return character.</li>
</ul>

<h3><code>scan_header()</code></h3>
<p>Method to scan for CRLF injection in HTTP response headers.</p>

<h4>Parameters</h4>
<ul>
    <li><code>u</code> (str): URL to scan for CRLF injection.</li>
    <li><code>unicode_random_level</code> (int): Level of randomness for Unicode encoding.</li>
    <li><code>carriage_return_only</code> (bool): Use only Carriage Return character.</li>
    <li><code>line_feed_only</code> (bool): Use only Line Feed character.</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 10).</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>debug</code> (bool): Enable or disable debug mode.</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include.</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use.</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use.</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use.</li>
</ul>

<h3><code>scan_body()</code></h3>
<p>Method to scan for CRLF injection in HTTP response body.</p>

<h4>Parameters</h4>
<ul>
    <li><code>u</code> (str): URL to scan for CRLF injection.</li>
    <li><code>unicode_random_level</code> (int): Level of randomness for Unicode encoding.</li>
    <li><code>carriage_return_only</code> (bool): Use only Carriage Return character.</li>
    <li><code>line_feed_only</code> (bool): Use only Line Feed character.</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 10).</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>debug</code> (bool): Enable or disable debug mode.</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include.</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use.</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use.</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use.</li>
</ul>

<h2>Example Usage</h2>
<p>Usage example for the <code>CRLF_Injection_Scanner</code> class:</p>

<pre><code>
from bane.scanners.vulnerabilities import CRLF_Injection_Scanner

#Example usage of scan_header method
result_header = CRLF_Injection_Scanner.scan_header(
    u="https://example.com",
    unicode_random_level=1,
    carriage_return_only=True,
    line_feed_only=False,
    timeout=10,
    user_agent="CustomUserAgent",
    cookie="CustomCookie",
    debug=True,
    headers={"Custom-Header": "Value"},
    http_proxies=["1.2.3.4:80"],
    socks4_proxies=["5.6.7.8:1080"],
    socks5_proxies=["9.10.11.12:1080"]
)

#Example usage of scan_body method
result_body = CRLF_Injection_Scanner.scan_body(
    u="https://example.com",
    unicode_random_level=1,
    carriage_return_only=True,
    line_feed_only=False,
    timeout=10,
    user_agent="CustomUserAgent",
    cookie="CustomCookie",
    debug=True,
    headers={"Custom-Header": "Value"},
    http_proxies=["1.2.3.4:80"],
    socks4_proxies=["5.6.7.8:1080"],
    socks5_proxies=["9.10.11.12:1080"]
)

</code></pre>

<h1>CSRF_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>CSRF_Scanner</code> class is used for scanning and detecting Cross-Site Request Forgery (CSRF) vulnerabilities on web pages. It provides methods to identify vulnerable forms and perform tests to check for CSRF vulnerabilities.</p>

<h2>Methods</h2>

<h3><code>csrf_filter_tokens(u, proxy=None, timeout=10, user_agent=None, cookie=None, headers={})</code></h3>
<p>This method filters forms on a web page to check for CSRF tokens. It returns a dictionary with vulnerable and safe forms.</p>
<ul>
    <li><code>u</code> (str): The URL of the web page to scan.</li>
    <li><code>proxy</code> (dict): Dictionary of proxy settings (default is None).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 10).</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests (default is None).</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests (required for authentication).</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include in requests (default is an empty dictionary).</li>
</ul>

<h3><code>csrf_forms(u, proxy=None, timeout=10, show_warnings=True, user_agent=None, cookie=None, replaceable_parameters={}, file_extension="png", fill_empty=10, referer="http://www.evil.com", leave_empty=[], dont_send=[], mime_type=None, predefined_inputs={}, headers={}, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This method scans forms for CSRF vulnerabilities and performs tests on them. It returns a list of dictionaries, each containing information about the form and its vulnerability status.</p>
<ul>
    <li><code>u</code> (str): The URL of the web page to scan.</li>
    <li><code>proxy</code> (dict): Dictionary of proxy settings (default is None).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 10).</li>
    <li><code>show_warnings</code> (bool): Enable or disable showing warnings (default is True).</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests (default is None).</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests (required for authentication).</li>
    <li><code>replaceable_parameters</code> (dict): Dictionary of parameters to replace in form submissions (default is an empty dictionary).</li>
    <li><code>file_extension</code> (str): File extension to use for file uploads (default is "png").</li>
    <li><code>fill_empty</code> (int): Number of empty fields to fill in forms (default is 10).</li>
    <li><code>referer</code> (str): Referer URL to include in the headers (default is "http://www.evil.com").</li>
    <li><code>leave_empty</code> (list): List of field names to leave empty (default is an empty list).</li>
    <li><code>dont_send</code> (list): List of fields not to send in form submissions (default is an empty list).</li>
    <li><code>mime_type</code> (str): MIME type for file uploads (default is None).</li>
    <li><code>predefined_inputs</code> (dict): Dictionary of predefined input values (default is an empty dictionary).</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include in requests (default is an empty dictionary).</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use for requests (default is None).</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use for requests (default is None).</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use for requests (default is None).</li>
</ul>

<h3><code>scan(u, max_pages=5, logs=True, proxy=None, timeout=10, show_warnings=True, user_agent=None, cookie=None, replaceable_parameters={}, file_extension="png", fill_empty=10, referer="http://www.evil.com", leave_empty=[], dont_send=[], mime_type=None, predefined_inputs={}, pages=[], headers={}, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This method scans a website for CSRF vulnerabilities on multiple pages. It returns a list of dictionaries, each containing information about the page and its CSRF vulnerability status.</p>
<ul>
    <li><code>u</code> (str): The URL of the website to scan.</li>
    <li><code>max_pages</code> (int): Maximum number of pages to scan (default is 5).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is True).</li>
    <li><code>proxy</code> (dict): Dictionary of proxy settings (default is None).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 10).</li>
    <li><code>show_warnings</code> (bool): Enable or disable showing warnings (default is True).</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests (default is None).</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests (required for authentication).</li>
    <li><code>replaceable_parameters</code> (dict): Dictionary of parameters to replace in form submissions (default is an empty dictionary).</li>
    <li><code>file_extension</code> (str): File extension to use for file uploads (default is "png").</li>
    <li><code>fill_empty</code> (int): Number of empty fields to fill in forms (default is 10).</li>
    <li><code>referer</code> (str): Referer URL to include in the headers (default is "http://www.evil.com").</li>
    <li><code>leave_empty</code> (list): List of field names to leave empty (default is an empty list).</li>
    <li><code>dont_send</code> (list): List of fields not to send in form submissions (default is an empty list).</li>
    <li><code>mime_type</code> (str): MIME type for file uploads (default is None).</li>
    <li><code>predefined_inputs</code> (dict): Dictionary of predefined input values (default is an empty dictionary).</li>
    <li><code>pages</code> (list): List of specific pages to scan (default is an empty list).</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include in requests (default is an empty dictionary).</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use for requests (default is None).</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use for requests (default is None).</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use for requests (default is None).</li>
</ul>

<h2>Example Usage</h2>

<code>
from bane.scanners.vulnerabilities import CSRF_Scanner

#Specify the URL and cookies for authentication
url = "https://example.com"
cookie = "your_auth_cookie_here"

#Scan the website for CSRF vulnerabilities
vulnerable_pages = CSRF_Scanner.scan(url, cookie=cookie)

#Print the results
for page in vulnerable_pages:
    print(f"Vulnerable Page: {page['page']}")
    for result in page['result']:
        form = result['form']
        status = result['status']
        print(f"Form: {form['action']}")
        print(f"Vulnerability Status: {status}")
</code>
</p>
<h1>Exposed_ENV_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>Exposed_ENV_Scanner</code> class is used for scanning and detecting exposed environment (".env") files on web servers. It provides methods to check if a specific path or multiple common paths lead to an exposed environment file.</p>

<h2>Methods</h2>

<h3><code>scan(u, user_agent=None, cookie=None, path="", brute_force=False, timeout=15, headers={}, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This method scans a URL for exposed environment files. It returns a tuple containing a boolean indicating whether an exposed environment file was found and the URL of the found file if applicable.</p>
<ul>
    <li><code>u</code> (str): The URL to scan for exposed environment files.</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests (default is None).</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests (default is None).</li>
    <li><code>path</code> (str): The path to the environment file (default is an empty string).</li>
    <li><code>brute_force</code> (bool): Enable brute force mode to try common paths (default is False).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 15).</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include in requests (default is an empty dictionary).</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use for requests (default is None).</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use for requests (default is None).</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use for requests (default is None).</li>
</ul>

<h2>Example Usage</h2>

<code>
from bane.scanners.vulnerabilities import Exposed_ENV_Scanner

#Specify the URL to scan for exposed environment files
url = "https://example.com"

#Scan the URL for exposed environment files
result, exposed_url = Exposed_ENV_Scanner.scan(url)

#Check the result
if result:
    print(f"Exposed environment file found at: {exposed_url}")
else:
    print("No exposed environment file found.")
</code>
</p>
<h1>Exposed_Git_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>Exposed_Git_Scanner</code> class is used to scan for exposed Git repositories on web servers. It checks if a specific URL is an exposed Git repository and returns a boolean result.</p>

<h2>Methods</h2>

<h3><code>scan(u, user_agent=None, cookie=None, timeout=15, headers={}, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This method scans a URL to check if it is an exposed Git repository. It returns a boolean indicating whether the URL is an exposed Git repository or not.</p>
<ul>
    <li><code>u</code> (str): The URL to scan for exposed Git repositories.</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests (default is None).</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests (default is None).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 15).</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include in requests (default is an empty dictionary).</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use for requests (default is None).</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use for requests (default is None).</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use for requests (default is None).</li>
</ul>

<h2>Example Usage</h2>

<code>
from bane.scanners.vulnerabilities import Exposed_Git_Scanner

#Specify the URL to scan for exposed Git repositories
url = "https://example.com/repo"

#Scan the URL for exposed Git repositories
result = Exposed_Git_Scanner.scan(url)

#Check the result
if result:
    print("Exposed Git repository found.")
else:
    print("No exposed Git repository found.")
</code>
</p>

<h1>Exposed_Telent_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>Exposed_Telent_Scanner</code> class is used to scan for exposed Telnet services on a remote host. It attempts to establish a Telnet connection to a specified host and port and returns a boolean result indicating whether the connection was successful or not.</p>

<h2>Methods</h2>

<h3><code>scan(u, p=23, timeout=5, **kwargs)</code></h3>
<p>This method attempts to establish a Telnet connection to a remote host using the specified parameters and returns a boolean value indicating the success of the connection.</p>
<ul>
    <li><code>u</code> (str): The target host or IP address to connect to via Telnet.</li>
    <li><code>p</code> (int): The port to use for the Telnet connection (default is 23).</li>
    <li><code>timeout</code> (int): Connection timeout in seconds (default is 5).</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the Telnet session (optional).</li>
</ul>

<h2>Example Usage</h2>

<code>
from bane.scanners.vulnerabilities import Exposed_Telent_Scanner

#Specify the host and port for Telnet scanning
host = "example.com"
port = 23

#Attempt to establish a Telnet connection
result = Exposed_Telent_Scanner.scan(host, port)

#Check the result
if result:
    print("Telnet service is exposed on the host.")
else:
    print("Telnet service is not exposed on the host.")
</code>
</p>

<h1>File_Upload_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>File_Upload_Scanner</code> class is used to scan web forms for potential file upload vulnerabilities. It searches for forms that allow file uploads, tests the file upload functionality, and reports potential issues such as unacceptable file extensions.</p>

<h2>Methods</h2>

<h3><code>file_upload_forms(u, timeout=10, show_warnings=True, user_agent=None, cookie=None, replaceble_parameters={"phpvalue": ((".", ""),)}, file_extension="png", fill_empty=10, dont_change=[], referer=None, leave_empty=[], dont_send=[], mime_type=None, predefined_inputs={}, headers={}, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This method scans web forms on a specified URL for file upload vulnerabilities and returns a list of results. It checks whether the forms accept specific file extensions and reports potential issues such as unacceptable extensions or missing submitted data. The method can handle multiple forms on the same page and returns information about each form's status.</p>
<ul>
    <li><code>u</code> (str): The target URL to scan for file upload forms.</li>
    <li><code>timeout</code> (int): The request timeout in seconds (default is 10).</li>
    <li><code>show_warnings</code> (bool): Whether to show warning messages (default is True).</li>
    <li><code>user_agent</code> (str): The user-agent string to use for the HTTP request (optional).</li>
    <li><code>cookie</code> (str): The cookie value to include in the request (optional).</li>
    <li><code>replaceble_parameters</code> (dict): Dictionary of parameters and their replacement values (optional).</li>
    <li><code>file_extension</code> (str): The file extension to use for testing (default is "png").</li>
    <li><code>fill_empty</code> (int): The number of empty fields to fill in the form (default is 10).</li>
    <li><code>dont_change</code> (list): List of form fields not to change (optional).</li>
    <li><code>referer</code> (str): The referer value for the request (optional).</li>
    <li><code>leave_empty</code> (list): List of form fields to leave empty (optional).</li>
    <li><code>dont_send</code> (list): List of form fields not to send (optional).</li>
    <li><code>mime_type</code> (str): The MIME type to use for the file upload (optional).</li>
    <li><code>predefined_inputs</code> (dict): Dictionary of predefined input values (optional).</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include in the request (optional).</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use for the request (optional).</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use for the request (optional).</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use for the request (optional).</li>
</ul>

<h3><code>scan(u, max_pages=5, logs=True, proxy=None, timeout=10, show_warnings=True, user_agent=None, cookie=None, replaceble_parameters={"phpvalue": ((".", ""),)}, file_extension="png", fill_empty=10, referer=None, leave_empty=[], dont_send=[], mime_type=None, predefined_inputs={}, pages=[], headers={}, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This method scans a specified URL and its linked pages for file upload forms. It allows you to perform a comprehensive scan for file upload vulnerabilities across multiple pages. The method returns a list of results, including information about each page and its associated form vulnerabilities.</p>
<ul>
    <li><code>u</code> (str): The target URL to scan for file upload forms.</li>
    <li><code>max_pages</code> (int): The maximum number of pages to scan (default is 5).</li>
    <li><code>logs</code> (bool): Whether to display scan logs (default is True).</li>
    <li><code>proxy</code> (str): The proxy server to use for the scan (optional).</li>
    <li><code>timeout</code> (int): The request timeout in seconds (default is 10).</li>
    <li><code>show_warnings</code> (bool): Whether to show warning messages (default is True).</li>
    <li><code>user_agent</code> (str): The user-agent string to use for the HTTP request (optional).</li>
    <li><code>cookie</code> (str): The cookie value to include in the request (optional).</li>
    <li><code>replaceble_parameters</code> (dict): Dictionary of parameters and their replacement values (optional).</li>
    <li><code>file_extension</code> (str): The file extension to use for testing (default is "png").</li>
    <li><code>fill_empty</code> (int): The number of empty fields to fill in the form (default is 10).</li>
    <li><code>referer</code> (str): The referer value for the request (optional).</li>
    <li><code>leave_empty</code> (list): List of form fields to leave empty (optional).</li>
    <li><code>dont_send</code> (list): List of form fields not to send (optional).</li>
    <li><code>mime_type</code> (str): The MIME type to use for the file upload (optional).</li>
    <li><code>predefined_inputs</code> (dict): Dictionary of predefined input values (optional).</li>
    <li><code>pages</code> (list): List of specific pages to scan (optional).</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include in the request (optional).</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use for the request (optional).</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use for the request (optional).</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use for the request (optional).</li>
</ul>

<h2>Example Usage</h2>

<code>
from bane.scanners.vulnerabilities import File_Upload_Scanner

#Specify the target URL to scan
target_url = "http://example.com"

#Perform a scan for file upload vulnerabilities
results = File_Upload_Scanner.scan(target_url)

#Display the scan results
for result in results:
    print("Page:", result['page'])
    for form_result in result['result']:
        print("Form:", form_result['form'])
        print("Vulnerable:", form_result['vulnerable'])
        print("Status:", form_result['status'])
</code>
</p>
<h1>Open_Redirect_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>Open_Redirect_Scanner</code> class is used to scan web forms for potential open redirect vulnerabilities. It detects and reports open redirect issues in web applications, helping security professionals identify and mitigate these risks.</p>

<h2>Methods</h2>

<h3><code>is_valid_open_redirect(req, payload)</code></h3>
<p>This method checks if a given HTTP request contains a valid open redirect vulnerability based on the payload used. It compares the payload's URL-decoded value to the "Location" header in the HTTP request to determine if it's a valid open redirect.</p>
<ul>
    <li><code>req</code> (requests.Response): The HTTP request to check for open redirect vulnerability.</li>
    <li><code>payload</code> (str): The payload used to test open redirect.</li>
    <li><strong>Returns:</strong> <code>True</code> if the open redirect is valid; otherwise, <code>False</code>.</li>
</ul>

<h3><code>open_redirect_submit(parsed, payload, replaceble_parameters, debug=False, enctype="application/x-www-form-urlencoded")</code></h3>
<p>This method submits a payload to a parsed web form to test for open redirect vulnerabilities. It checks if the response contains a valid open redirect issue and also detects potential security issues such as SQL errors, XML parsing errors, fetching URL errors (potential SSRF), and reading file errors (potential path traversal).</p>
<ul>
    <li><code>parsed</code> (list): A parsed web form consisting of three elements (form data, headers, proxies, and timeout).</li>
    <li><code>payload</code> (str): The payload to submit for open redirect testing.</li>
    <li><code>replaceble_parameters</code> (dict): Dictionary of parameters and their replacement values (optional).</li>
    <li><code>debug</code> (bool): Whether to enable debug mode (default is False).</li>
    <li><code>enctype</code> (str): The enctype type to use for the request (default is "application/x-www-form-urlencoded").</li>
    <li><strong>Returns:</strong> A tuple containing whether the open redirect is valid, a dictionary with the original parsed form data, and flags for various security issues.</li>
</ul>

<h3><code>open_redirect_forms(u, payload, number, email_extension, phone_pattern, dont_change, predefined_inputs, replaceble_parameters, file_extension, save_to_file, logs, fill_empty, leave_empty, dont_send, timeout, user_agent, cookie, debug, mime_type, headers, http_proxies, socks4_proxies, socks5_proxies)</code></h3>
<p>This method scans web forms on a specified URL for open redirect vulnerabilities. It submits payloads to forms to detect open redirect issues and reports other potential security problems. The results are structured and can be saved to a file.</p>
<ul>
    <li><code>u</code> (str): The target URL to scan for open redirect forms.</li>
    <li><code>payload</code> (str): The payload to submit for open redirect testing.</li>
    <li><code>number</code> (tuple): A range for generating numbers (default is (1, 9)).</li>
    <li><code>email_extension</code> (str): The email extension to use (default is "@gmail.com").</li>
    <li><code>phone_pattern</code> (str): The phone pattern (default is "XXX-XXX-XXXX").</li>
    <li><code>dont_change</code> (dict): Dictionary of form fields not to change (optional).</li>
    <li><code>predefined_inputs</code> (dict): Dictionary of predefined input values (optional).</li>
    <li><code>replaceble_parameters</code> (dict): Dictionary of parameters and their replacement values (optional).</li>
    <li><code>file_extension</code> (str): The file extension to use for testing (default is "png").</li>
    <li><code>save_to_file</code> (str): The path to save results to a file (optional).</li>
    <li><code>logs</code> (bool): Whether to show scan logs (default is True).</li>
    <li><code>fill_empty</code> (int): The number of empty fields to fill in the form (default is 10).</li>
    <li><code>leave_empty</code> (list): List of form fields to leave empty (optional).</li>
    <li><code>dont_send</code> (list): List of form fields not to send (optional).</li>
    <li><code>timeout</code> (int): The request timeout in seconds (default is 10).</li>
    <li><code>user_agent</code> (str): The user-agent string to use for the HTTP request (optional).</li>
    <li><code>cookie</code> (str): The cookie value to include in the request (optional).</li>
    <li><code>debug</code> (bool): Whether to enable debug mode (default is False).</li>
    <li><code>mime_type</code> (str): The MIME type to use for the file upload (optional).</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include in the request (optional).</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use for the request (optional).</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use for the request (optional).</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use for the request (optional).</li>
    <li><strong>Returns:</strong> A dictionary containing scan results, including open redirect vulnerabilities and potential security issues.</li>
</ul>

<h3><code>scan(u, max_pages, pages, payload, number, email_extension, phone_pattern, dont_change, predefined_inputs, replaceble_parameters, file_extension, save_to_file, logs, fill_empty, leave_empty, dont_send, timeout, user_agent, cookie, debug, mime_type, headers, http_proxies, socks4_proxies, socks5_proxies)</code></h3>
<p>This method scans a specified URL and its linked pages for open redirect forms. It allows you to perform a comprehensive scan for open redirect vulnerabilities across multiple pages. The method returns structured results that include open redirect issues and potential security problems.</p>
<ul>
    <li><code>u</code> (str): The target URL to scan for open redirect forms.</li>
    <li><code>max_pages</code> (int): The maximum number of pages to scan (default is 5).</li>
    <li><code>pages</code> (list): List of specific pages to scan (optional).</li>
    <li><code>payload</code> (str): The payload to submit for open redirect testing.</li>
    <li><code>number</code> (tuple): A range for generating numbers (default is (1, 9)).</li>
    <li><code>email_extension</code> (str): The email extension to use (default is "@gmail.com").</li>
    <li><code>phone_pattern</code> (str): The phone pattern (default is "XXX-XXX-XXXX").</li>
    <li><code>dont_change</code> (dict): Dictionary of form fields not to change (optional).</li>
    <li><code>predefined_inputs</code> (dict): Dictionary of predefined input values (optional).</li>
    <li><code>replaceble_parameters</code> (dict): Dictionary of parameters and their replacement values (optional).</li>
    <li><code>file_extension</code> (str): The file extension to use for testing (default is "png").</li>
    <li><code>save_to_file</code> (str): The path to save results to a file (optional).</li>
    <li><code>logs</code> (bool): Whether to show scan logs (default is True).</li>
    <li><code>fill_empty</code> (int): The number of empty fields to fill in the form (default is 10).</li>
    <li><code>leave_empty</code> (list): List of form fields to leave empty (optional).</li>
    <li><code>dont_send</code> (list): List of form fields not to send (optional).</li>
    <li><code>timeout</code> (int): The request timeout in seconds (default is 10).</li>
    <li><code>user_agent</code> (str): The user-agent string to use for the HTTP request (optional).</li>
    <li><code>cookie</code> (str): The cookie value to include in the request (optional).</li>
    <li><code>debug</code> (bool): Whether to enable debug mode (default is False).</li>
    <li><code>mime_type</code> (str): The MIME type to use for the file upload (optional).</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include in the request (optional).</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use for the request (optional).</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use for the request (optional).</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use for the request (optional).</li>
    <li><strong>Returns:</strong> A list of dictionaries containing scan results for each page scanned, including open redirect vulnerabilities and potential security issues.</li>
</ul>

<h2>Example Usage</h2>

<p>Here's an example of how to use the <code>Open_Redirect_Scanner</code> class to scan for open redirect vulnerabilities in web forms:</p>

<p><code>
from bane.scanners.vulnerabilities import Open_Redirect_Scanner

#Specify the target URL to scan
target_url = "http://example.com"

#Set other parameters as needed
payload = "http://www.google.com"  #Open redirect payload
max_pages = 5  #Maximum number of pages to scan
logs = True  #Whether to show scan logs

#Perform the open redirect scan
results = Open_Redirect_Scanner.scan(
    u=target_url,
    max_pages=max_pages,
    payload=payload,
    logs=logs,
)

#Display the scan results
for result in results:
    print("Page:", result["page"])
    for form_result in result["result"]:
        print("Form:", form_result["form"])
        print("Method:", form_result["method"])
        if form_result["vulnerable"]:
            print("Open Redirect Vulnerabilities:")
            for vul in form_result["vulnerable"]:
                print("Parameter:", vul["parameter"])
                print("Context:", vul["context"])
        if form_result["sql_errors"]:
            print("SQL Errors Detected:")
            for sql_err in form_result["sql_errors"]:
                print("Parameter:", sql_err["parameter"])
                print("P.O.C.:", sql_err["p_o_c"])
        #Add handling for other detected security issues (xml_parsing_errors, fetching_url_errors, reading_file_errors)
        print()
</code>
</p>