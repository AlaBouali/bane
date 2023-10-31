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

# Example domain for information gathering
domain = "example.com"

# Gather domain information
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

# Access the gathered information
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

# Perform a Google dork search for a specific query
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

# Access the list of URLs related to the query
for result in results:
    print(result)
</code></pre>
<h1>IP_info Class</h1>

<h2>Class Overview</h2>
<p>The <code>IP_info</code> class in the "bane" module provides methods for gathering information related to IP addresses, including obtaining your own IP, geolocation information, reverse IP lookup, and Shodan reports.</p>

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

<h3><code>get_IP_info(ip, timeout=15, proxy=None)</code></h3>
<p>This method combines the results of geolocation information, reverse IP lookup, and Shodan reports for a given IP address into a dictionary.</p>

<p>Parameters:</p>
<ul>
    <li><code>ip</code> (str): The IP address for which to gather information.</li>
    <li><code>timeout</code> (int, optional): Request timeout in seconds (default is 15).</li>
    <li><code>proxy</code> (dict, optional): HTTP and/or HTTPS proxy configuration.</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>IP_info</code> class, call its methods to gather information about IP addresses. Here's an example:</p>

<pre><code>
from bane.gather_info import IP_info

# Example IP address for information gathering
ip_address = "192.168.1.1"

# Gather IP information
info = IP_info.get_IP_info(
    ip=ip_address,
    timeout=15,
    proxy={"http": "http://1.2.3.4:80", "https": "http://1.2.3.4:80"}
)

# Access the gathered information
print("Geolocation Information:", info["geo_ip_location"])
print("Reverse IP Lookup:", info["reverse_ip_lookup"])
print("Shodan Report:", info["shodan_report"])
</code></pre>
