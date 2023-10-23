<!DOCTYPE html>
<html>
<head>
  <title>File Manager Finder Documentation</title>
</head>
<body>
  <h1>File Manager Finder Documentation</h1>

  <h2>Class: filemanager_finder</h2>
  <p>
    The <code>filemanager_finder</code> class is designed to find file manager URLs on a target website. It scans for potential file manager paths and reports the results.
  </p>

  <h3>Constructor</h3>
  <pre>
    <code>
      class filemanager_finder:
        __slots__ = ["logs", "stop", "finish", "result"]

        def __init__(
            self,
            u,
            logs=True,
            threads_daemon=True,
            user_agent=None,
            cookie=None,
            timeout=10,
            headers={},
            http_proxies=None,
            socks4_proxies=None,
            socks5_proxies=None
        ):
    </code>
  </pre>

  <h4>Parameters:</h4>
  <ul>
    <li><code>u</code> (str): The target URL for which file manager URLs will be searched.</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is True).</li>
    <li><code>threads_daemon</code> (bool): Whether the scan threads should run as daemon threads (default is True).</li>
    <li><code>user_agent</code> (str): User-Agent header to be used in requests (default is None).</li>
    <li><code>cookie</code> (str): Cookies to include in requests (default is None).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 10).</li>
    <li><code>headers</code> (dict): Additional headers to include in requests (default is an empty dictionary).</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use for requests (default is None).</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use for requests (default is None).</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use for requests (default is None).</li>
  </ul>

  <p>
    The constructor initializes the <code>filemanager_finder</code> class and starts a background thread to scan for file manager URLs on the provided target website.
  </p>

  <h3>Methods</h3>

  <h4><code>crack(self, u, user_agent, cookie, timeout, proxies, headers)</code></h4>
  <p>
    This method performs the actual scanning for file manager URLs. It iterates through a list of possible paths and checks if they exist on the target website.
  </p>

  <ul>
    <li><code>u</code> (str): The target URL.</li>
    <li><code>user_agent</code> (str): User-Agent header for requests.</li>
    <li><code>cookie</code> (str): Cookies to include in requests.</li>
    <li><code>timeout</code> (int): Request timeout in seconds.</li>
    <li><code>proxies</code> (dict): Proxy configuration for requests.</li>
    <li><code>headers</code> (dict): Additional headers for requests.</li>
  </ul>

  <h4><code>done(self)</code></h4>
  <p>
    This method returns <code>True</code> when the scanning is complete.
  </p>

  <h3>Example Usage</h3>
  <pre>
    <code>
      # Example Usage
      finder = filemanager_finder("https://example.com", logs=True)
      while not finder.done():
          # Wait for the scan to finish
          pass
      # Scan complete
    </code>
  </pre>

  <p>
    This is a basic example of how to use the <code>filemanager_finder</code> class to find file manager URLs on a target website.
  </p>
</body>
</html>
