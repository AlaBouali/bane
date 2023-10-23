<!DOCTYPE html>
<html>
<head>
</head>
<body>
<h1>Hydra Class Documentation</h1>

<h2>Class: hydra</h2>

<p>
        The `hydra` class is designed for performing brute force attacks on various protocols such as SSH, Telnet, FTP, SMTP, MySQL, and others. It provides methods for attempting authentication using different username and password combinations.
</p>

<h3>Attributes:</h3>
<ul>
    <li><code>stop</code> (bool): Indicates whether the attack should be stopped.</li>
    <li><code>finish</code> (bool): Indicates whether the attack has finished.</li>
    <li><code>result</code> (dict): Stores the result of the attack in the format <code>{target_url: username:password}</code>.</li>
    <li><code>logs</code> (bool): Indicates whether logging is enabled.</li>
</ul>

<h3>Methods:</h3>

<h4>Method: <code>__init__</code></h4>

<pre>
    def __init__(
        self,
        u,
        p=22,
        protocol="ssh",
        word_list=[],
        threads_daemon=True,
        logs=True,
        exchange_key=None,
        timeout=5,
        ehlo=False,
        helo=True,
        ttls=False,
        user_agent=None,
        cookie=None,
        headers={},
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None
    )
</pre>

<p>
        Initializes an instance of the Hydra class for conducting brute force attacks.
</p>

<h4>Parameters:</h4>
<ul>
    <li><code>u</code> (str): The target URL or IP address.</li>
    <li><code>p</code> (int): The port number to connect to (default is 22 for SSH).</li>
    <li><code>protocol</code> (str): The protocol to use for the attack (e.g., "ssh", "telnet", "ftp").</li>
    <li><code>word_list</code> (list): List of username:password combinations to try.</li>
    <li><code>threads_daemon</code> (bool): Set thread as daemon (default is True).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is True).</li>
    <li><code>exchange_key</code> (str): Key for SSH exchange (if needed).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 5).</li>
    <li><code>ehlo</code> (bool): Enable EHLO during SMTP (default is False).</li>
    <li><code>helo</code> (bool): Enable HELO during SMTP (default is True).</li>
    <li><code>ttls</code> (bool): Enable TLS during SMTP (default is False).</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>headers</code> (dict): Additional HTTP headers for requests.</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use.</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use.</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use.</li>
</ul>

<h4>Method: <code>crack</code></h4>

<pre>
    def crack(
        self, u, p, protocol, word_list, logs, exchange_key, timeout, ehlo, helo, ttls, proxies, socket_proxies, user_agent, cookie, headers
    )
</pre>

<p>
        Performs the brute force attack using the specified protocol and parameters.
</p>

<h4>Parameters:</h4>
<ul>
    <li><code>u</code> (str): The target URL or IP address.</li>
    <li><code>p</code> (int): The port number to connect to.</li>
    <li><code>protocol</code> (str): The protocol to use for the attack.</li>
    <li><code>word_list</code> (list): List of username:password combinations to try.</li>
    <li><code>logs</code> (bool): Enable or disable logging.</li>
    <li><code>exchange_key</code> (str): Key for SSH exchange (if needed).</li>
    <li><code>timeout</code> (int): Request timeout in seconds.</li>
    <li><code>ehlo</code> (bool): Enable EHLO during SMTP (if applicable).</li>
    <li><code>helo</code> (bool): Enable HELO during SMTP (if applicable).</li>
    <li><code>ttls</code> (bool): Enable TLS during SMTP (if applicable).</li>
    <li><code>proxies</code> (list): List of HTTP proxies to use.</li>
    <li><code>socket_proxies</code> (list): List of SOCKS4 and SOCKS5 proxies to use.</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>headers</code> (dict): Additional HTTP headers for requests.</li>
</ul>

<h4>Method: <code>done</code></h4>

<pre>
    def done(self)
</pre>

<p>
        Checks if the brute force attack is done.
</p>

<h4>Return:</h4>
<ul>
    <li><code>bool</code>: True if the attack is finished, False otherwise.</li>
</ul>

<p>
        This class is used to conduct brute force attacks on various protocols securely and without false positive results.
</p>

</body>
</html>
