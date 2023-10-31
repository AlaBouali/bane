<h1>Admin_Panel_Finder Class</h1>

<h2>Class Overview</h2>
<p>The <code>Admin_Panel_Finder</code> class is part of the "bane" module and is used to search for potential admin panel URLs on a website using a predefined list of extensions.</p>

<h2>Class Constructor</h2>
<pre><code>class Admin_Panel_Finder(target, logs=True, threads_daemon=True, user_agent=None, cookie=None, ext="php", timeout=10, headers={}, http_proxies=None, socks4_proxies=None, socks5_proxies=None)
</code></pre>
<p>This constructor initializes an instance of the <code>Admin_Panel_Finder</code> class with the following parameters:</p>

<ul>
    <li><code>target</code> (str): The target website URL.</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is True).</li>
    <li><code>threads_daemon</code> (bool): Set thread as daemon (default is True).</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>ext</code> (str): Extension to use for URLs (default is 'php').</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 10).</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include.</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use.</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use.</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use.</li>
</ul>

<h2>Methods</h2>
<h3><code>done(self)</code></h3>
<p>This method returns the value of the <code>finish</code> attribute, indicating whether the operation is done or not.</p>

<h3><code>crack(self, target, timeout, logs, ext, user_agent, cookie, proxies, headers)</code></h3>
<p>This method performs the admin panel URL search operation with the specified parameters. It takes the following parameters:</p>
<ul>
    <li><code>target</code> (str): The target website URL.</li>
    <li><code>timeout</code> (int): Request timeout in seconds.</li>
    <li><code>logs</code> (bool): Enable or disable logging.</li>
    <li><code>ext</code> (str): Extension to use for URLs.</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>proxies</code> (list): List of proxies to use for requests.</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include.</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>Admin_Panel_Finder</code> class, create an instance of it by providing the required parameters, and it will start searching for admin panel URLs in a separate thread. Here's an example:</p>

<pre><code>
from bane.bruteforce import *

# Create an instance of Admin_Panel_Finder
admin_finder = Admin_Panel_Finder(
    target="https://example.com",
    logs=True,
    threads_daemon=True,
    user_agent="CustomUserAgent",
    cookie="CustomCookie",
    ext="php",
    timeout=10,
    headers={"Custom-Header": "Value"},
    http_proxies=["http://proxy1.com", "http://proxy2.com"],
    socks4_proxies=["socks4proxy1.com", "socks4proxy2.com"],
    socks5_proxies=["socks5proxy1.com", "socks5proxy2.com"]
)

# Admin panel search is performed in the background
# You can check the status with admin_finder.done()
while not admin_finder.done():
    time.sleep(1)

# Access the result
result = admin_finder.result
print("Admin Panel URLs:", result)
</code></pre>
