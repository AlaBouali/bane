<!DOCTYPE html>
<html>
<head>

</head>
<body>
<h1>Filemanager Finder Documentation</h1>
<p>This Python code provides a tool for finding potential paths to file managers on web servers. It can be used by security researchers to identify these paths for further analysis and assessment.</p>

<h2>Class: force_browsing</h2>
<p>The <code>force_browsing</code> class is used to initiate the file manager path discovery process.</p>

<h3>Parameters:</h3>
<ul>
    <li><code>u</code>: The base URL where the file manager paths will be appended to.</li>
    <li><code>logs</code>: A boolean flag to enable or disable logging (default is True).</li>
    <li><code>threads_daemon</code>: A boolean flag indicating whether threads should run as daemons (default is True).</li>
    <li><code>ext</code>: The file extension to append to potential file manager paths (default is "php").</li>
    <li><code>user_agent</code>: A custom User-Agent header to be used in HTTP requests (default is None).</li>
    <li><code>cookie</code>: A custom Cookie header to be used in HTTP requests (default is None).</li>
    <li><code>timeout</code>: The timeout for HTTP requests in seconds (default is 10).</li>
    <li><code>headers</code>: A dictionary of custom headers to be included in HTTP requests (default is an empty dictionary).</li>
    <li><code>http_proxies</code>: A list of HTTP proxies to be used for requests (default is None).</li>
    <li><code>socks4_proxies</code>: A list of SOCKS4 proxies to be used for requests (default is None).</li>
    <li><code>socks5_proxies</code>: A list of SOCKS5 proxies to be used for requests (default is None).</li>
</ul>

<h3>Methods:</h3>
<ul>
    <li><code>crack</code>: Initiates the process of searching for file manager paths.</li>
    <li><code>done</code>: Returns a boolean indicating whether the search process has finished.</li>
</ul>

<p>The <code>crack</code> method runs the discovery process using the specified parameters and updates the result dictionary with any found paths. The process can be stopped by setting the <code>stop</code> attribute to True. The <code>done</code> method can be used to check if the search process has finished.</p>

<h2>Example Usage:</h2>
<p>Below is an example of how to use the <code>force_browsing</code class to search for file manager paths:</p>

<pre><code>
from bane.bruteforce.utils import *

# Initialize the force_browsing class with appropriate parameters
f = force_browsing(
    u="http://example.com",
    logs=True,
    threads_daemon=True,
    ext="php",
    user_agent="Custom User Agent",
    cookie="Custom Cookie",
    timeout=10,
    headers={"Custom-Header": "Value"},
    http_proxies=["1.1.11.1:80", "1.1.1.1:8080"],
    socks4_proxies=["2.2.2.2:1080"],
    socks5_proxies=[]
)

# Check if the search process has finished
if f.done():
    # Get the result
    result = f.result
    print("File manager paths found:", result)
</code></pre>

<p>Ensure that you have the required libraries and a valid base URL for successful path discovery. The <code>logs</code> parameter controls whether logging information is displayed during the process.</p>
</body>
</html>
