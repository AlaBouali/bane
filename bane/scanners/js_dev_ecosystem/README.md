<h1>Angular_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>Angular_Scanner</code> class is designed to scan Angular applications and packages for security vulnerabilities using the Snyk database. It provides methods to scan Angular core and specific packages for known vulnerabilities.</p>

<h2>Static Methods</h2>

<h3><code>scan_core(version, user_agent=None, cookie=None, timeout=20, headers={}, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This static method scans the Angular core for security vulnerabilities based on the specified version. It takes the following parameters:</p>

<ul>
    <li><code>version</code> (str): The version of Angular core to scan.</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests (default is None).</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests (default is None).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 20).</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include (default is an empty dictionary).</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use (default is None).</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use (default is None).</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use (default is None).</li>
</ul>

<p>The method performs an HTTP request to the Snyk database for Angular core vulnerabilities and returns a list of vulnerabilities with their titles and URLs.</p>

<h3><code>scan_package(package, version, user_agent=None, cookie=None, timeout=20, headers={}, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This static method scans a specific Angular package for security vulnerabilities based on the specified version. It takes the following parameters:</p>

<ul>
    <li><code>package</code> (str): The name of the Angular package to scan.</li>
    <li><code>version</code> (str): The version of the Angular package to scan.</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests (default is None).</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests (default is None).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 20).</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include (default is an empty dictionary).</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use (default is None).</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use (default is None).</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use (default is None).</li>
</ul>

<p>The method performs an HTTP request to the Snyk database for the specified Angular package vulnerabilities and returns a list of vulnerabilities with their titles and URLs.</p>

<h2>Example Usage</h2>
<p>To use the <code>Angular_Scanner</code> class, call the <code>scan_core</code> or <code>scan_package</code> method with the required parameters, and it will perform the Angular scanning process. Here's an example:</p>

<pre><code>
from bane import Angular_Scanner

#Scan Angular core for vulnerabilities
core_vulnerabilities = Angular_Scanner.scan_core(
    version="12.3.4",
    user_agent="CustomUserAgent",
    cookie="CustomCookie",
    timeout=20,
    headers={"Custom-Header": "Value"},
    http_proxies=["1.2.3.4:80"],
    socks4_proxies=["5.6.7.8:1080"],
    socks5_proxies=["9.10.11.12:1080"]
)

#Scan a specific Angular package for vulnerabilities
package_vulnerabilities = Angular_Scanner.scan_package(
    package="router",
    version="5.6.7",
    user_agent="CustomUserAgent",
    cookie="CustomCookie",
    timeout=20,
    headers={"Custom-Header": "Value"},
    http_proxies=["1.2.3.4:80"],
    socks4_proxies=["5.6.7.8:1080"],
    socks5_proxies=["9.10.11.12:1080"]
)

#Access the results
print("Core Vulnerabilities:", core_vulnerabilities)
print("Package Vulnerabilities:", package_vulnerabilities)
</code></pre>

<h1>NodeJS_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>NodeJS_Scanner</code> class is designed to scan Node.js installations for known vulnerabilities using the Vulners database. It provides a static method to perform the scanning process based on the specified Node.js version.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>This static method scans a Node.js installation for known vulnerabilities based on the specified version. It utilizes the Vulners database for vulnerability information. It takes the following parameters:</p>

<ul>
    <li><code>version</code> (str): The version of Node.js to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the Vulners_Search_Scanner, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns a list of vulnerabilities with their titles, descriptions, and links.</p>

<h2>Example Usage</h2>
<p>To use the <code>NodeJS_Scanner</code> class, call the <code>scan</code> method with the Node.js version and any additional parameters needed for the Vulners_Search_Scanner. Here's an example:</p>

<pre><code>
from bane import NodeJS_Scanner

#Scan Node.js for vulnerabilities
nodejs_vulnerabilities = NodeJS_Scanner.scan(
    version="14.17.6",
    http_proxies=["1.2.3.4:80"],
)

#Access the results
print("Node.js Vulnerabilities:", nodejs_vulnerabilities)
</code></pre>

<h1>NPM_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>NPM_Scanner</code> class is designed for scanning NPM (Node Package Manager) libraries and packages for vulnerabilities using the Snyk security database. It provides static methods for scanning libraries and library packages, fetching vulnerability information, and returning the results.</p>

<h2>Static Methods</h2>

<h3><code>scan_library_core(library, version, user_agent=None, cookie=None, timeout=20, headers={}, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This static method scans an NPM library for vulnerabilities using the Snyk security database. It takes parameters such as the library name, version, user agent, cookie, timeout, headers, and proxies. The method returns a list of dictionaries containing vulnerability information, including title and URL.</p>

<h3><code>scan_library_package(library, package, version, user_agent=None, cookie=None, timeout=20, headers={}, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></h3>
<p>This static method scans an NPM library package for vulnerabilities using the Snyk security database. It takes parameters such as the library name, package name, version, user agent, cookie, timeout, headers, and proxies. The method returns a list of dictionaries containing vulnerability information, including title and URL.</p>

<h2>Example Usage</h2>
<p>To use the <code>NPM_Scanner</code> class, call the static methods <code>scan_library_core</code> or <code>scan_library_package</code> with the required parameters. Here's an example:</p>

<pre><code>
from bane import NPM_Scanner

#Scan an NPM library for vulnerabilities
library_core_result = NPM_Scanner.scan_library_core(
    library="example_library",
    version="1.2.3",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    cookie="your_cookie_string",
    timeout=15,
    headers={"Custom-Header": "header_value"},
    http_proxies=["http://proxy1:8080", "http://proxy2:8080"],
    socks4_proxies=["socks4://proxy3:1080"],
    socks5_proxies=["socks5://proxy4:1080"]
)

#Scan an NPM library package for vulnerabilities
library_package_result = NPM_Scanner.scan_library_package(
    library="example_library",
    package="example_package",
    version="1.2.3",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    cookie="your_cookie_string",
    timeout=15,
    headers={"Custom-Header": "header_value"},
    http_proxies=["http://proxy1:8080", "http://proxy2:8080"],
    socks4_proxies=["socks4://proxy3:1080"],
    socks5_proxies=["socks5://proxy4:1080"]
)

#Access the scan results
print("Library Core Vulnerabilities:", library_core_result)
print("Library Package Vulnerabilities:", library_package_result)
</code></pre>


<h1>ReactJS_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>ReactJS_Scanner</code> class is designed to scan React.js installations for known vulnerabilities using the Vulners database. It provides a static method to perform the scanning process based on the specified React.js version.</p>

<h2>Static Method</h2>
<h3><code>scan(version, **kwargs)</code></h3>
<p>This static method scans a React.js installation for known vulnerabilities based on the specified version. It utilizes the Vulners database for vulnerability information specific to React.js. It takes the following parameters:</p>

<ul>
    <li><code>version</code> (str): The version of React.js to scan.</li>
    <li><code>**kwargs</code>: Additional keyword arguments to pass to the Vulners_Search_Scanner, such as HTTP proxies, API keys, etc.</li>
</ul>

<p>The method returns a list of vulnerabilities with their titles, descriptions, and links.</p>

<h2>Example Usage</h2>
<p>To use the <code>ReactJS_Scanner</code> class, call the <code>scan</code> method with the React.js version and any additional parameters needed for the Vulners_Search_Scanner. Here's an example:</p>

<pre><code>
from bane import ReactJS_Scanner

#Scan React.js for vulnerabilities
reactjs_vulnerabilities = ReactJS_Scanner.scan(
    version="17.0.2",
    http_proxies=["1.2.3.4:80"],
)

#Access the results
print("React.js Vulnerabilities:", reactjs_vulnerabilities)
</code></pre>
