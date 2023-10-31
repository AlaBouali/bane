<h1>Botnet_Scanner Class</h1>

<h2>Class Overview</h2>
<p>The <code>Botnet_Scanner</code> class is part of the "bane" module and is used for scanning safe IPs all over the internet with a word list to bruteforce various login protocols, including FTP, SSH, Telnet, SMTP, and MySQL. The scan results are saved to text files in the same directory.</p>
<p>It is recommended to use this class with a VPS or a fast internet connection for efficient scanning.</p>

<h2>Class Constructor</h2>
<pre><code>class Botnet_Scanner(
    file_name="results.csv",
    protocol="telnet",
    telnet_bots=True,
    threads_daemon=True,
    logs=True,
    threads=100,
    word_list=[],
    ip_range=None,
    timeout=7,
    p=23,
    socks4_proxies=None,
    socks5_proxies=None
)
</code></pre>
<p>This constructor initializes an instance of the <code>Botnet_Scanner</code> class with the following parameters:</p>

<ul>
    <li><code>file_name</code> (str): The name of the results file (default is "results.csv").</li>
    <li><code>protocol</code> (str): The protocol to scan (FTP, SSH, Telnet, SMTP, or MySQL) (default is "telnet").</li>
    <li><code>telnet_bots</code> (bool): Enable Telnet bot mode (default is True).</li>
    <li><code>threads_daemon</code> (bool): Set threads as daemon (default is True).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is True).</li>
    <li><code>threads</code> (int): Number of scanning threads to run (default is 100).</li>
    <li><code>word_list</code> (list): List of usernames and passwords to use for scanning.</li>
    <li><code>ip_range</code> (str): IP range for scanning (e.g., "192.168.1.{}").</li>
    <li><code>timeout</code> (int): Connection timeout in seconds (default is 7).</li>
    <li><code>p</code> (int): Port to use for scanning (default is 23).</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use.</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use.</li>
</ul>

<h2>Methods</h2>
<h3><code>scan(self)</code></h3>
<p>This method initiates the scanning process. It spawns threads to scan for login credentials and save the results to the specified file.</p>

<h3><code>done(self)</code></h3>
<p>This method checks if the scanning process is completed and returns a boolean indicating whether it's done or not.</p>

<h3><code>reset(self)</code></h3>
<p>This method resets the class attributes to their initial state.</p>

<h3><code>kill(self)</code></h3>
<p>This method stops the scanning process by setting the stop flag to True and resetting the class attributes. It returns the number of found credentials.</p>

<h2>Example Usage</h2>
<p>To use the <code>Botnet_Scanner</code> class, create an instance of it by providing the required parameters, and it will start scanning for login credentials in a separate thread. Here's an example:</p>

<pre><code>
import time
from bane import Botnet_Scanner

# Create an instance of Botnet_Scanner
scanner = Botnet_Scanner(
    file_name="results.csv",
    protocol="telnet",
    telnet_bots=True,
    threads_daemon=True,
    logs=True,
    threads=100,
    word_list=["user1:pass1", "user2:pass2"],
    timeout=7,
    p=23,
    socks4_proxies=["1.2.3.4:1080"],
    socks5_proxies=["5.6.7.8:1080"]
)

# Scanning is performed in the background
while not scanner.done():
    time.sleep(1)

# Access the result
result = scanner.result
print("Found credentials:", result)
</code></pre>
