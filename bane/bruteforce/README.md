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
import time
from bane.bruteforce import Admin_Panel_Finder

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
    http_proxies=["2.2.2.2:80", "1.1.1.1:8080"],
    socks4_proxies='3.3.3.3:1080',
    socks5_proxies=None
)

# Admin panel search is performed in the background
# You can check the status with admin_finder.done()
while not admin_finder.done():
    time.sleep(1)

# Access the result
result = admin_finder.result
print("Admin Panel URLs:", result)
</code></pre>



<h1>Decryptor Class</h1>

<h2>Class Overview</h2>
<p>The <code>Decryptor</code> class is part of the "bane" module and is used for performing various cryptographic hash decryption attempts.</p>

<h2>Class Constructor</h2>
<pre><code>class Decryptor(u, word_list=[], threads_daemon=True, md5_hash=False, sha1_hash=False, sha256_hash=False, sha224_hash=False, sha384_hash=False, sha512_hash=False, base64_string=False, caesar_hash=False, logs=False)
</code></pre>
<p>This constructor initializes an instance of the <code>decrypt</code> class with the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target hash to decrypt.</li>
    <li><code>word_list</code> (list): List of words to use for decryption attempts (default is an empty list).</li>
    <li><code>threads_daemon</code> (bool): Set the thread as daemon (default is True).</li>
    <li><code>md5_hash</code> (bool): Enable MD5 hash decryption attempt (default is False).</li>
    <li><code>sha1_hash</code> (bool): Enable SHA-1 hash decryption attempt (default is False).</li>
    <li><code>sha256_hash</code> (bool): Enable SHA-256 hash decryption attempt (default is False).</li>
    <li><code>sha224_hash</code> (bool): Enable SHA-224 hash decryption attempt (default is False).</li>
    <li><code>sha384_hash</code> (bool): Enable SHA-384 hash decryption attempt (default is False).</li>
    <li><code>sha512_hash</code> (bool): Enable SHA-512 hash decryption attempt (default is False).</li>
    <li><code>base64_string</code> (bool): Enable Base64 string decryption attempt (default is False).</li>
    <li><code>caesar_hash</code> (bool): Enable Caesar cipher decryption attempt (default is False).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is False).</li>
</ul>

<h2>Main Method: <code>crack</code></h2>
<pre><code>def crack(self, u, word_list, md5_hash, sha1_hash, sha256_hash, sha224_hash, sha384_hash, sha512_hash, base64_string, caesar_hash, logs)
</code></pre>
<p>The <code>crack</code> method performs the hash decryption attempts with the specified parameters. It takes the following parameters:</p>
<ul>
    <li><code>u</code> (str): The target hash to decrypt.</li>
    <li><code>word_list</code> (list): List of words to use for decryption attempts.</li>
    <li><code>md5_hash</code> (bool): Enable MD5 hash decryption attempt.</li>
    <li><code>sha1_hash</code> (bool): Enable SHA-1 hash decryption attempt.</li>
    <li><code>sha256_hash</code> (bool): Enable SHA-256 hash decryption attempt.</li>
    <li><code>sha224_hash</code> (bool): Enable SHA-224 hash decryption attempt.</li>
    <li><code>sha384_hash</code> (bool): Enable SHA-384 hash decryption attempt.</li>
    <li><code>sha512_hash</code> (bool): Enable SHA-512 hash decryption attempt.</li>
    <li><code>base64_string</code> (bool): Enable Base64 string decryption attempt.</li>
    <li><code>caesar_hash</code> (bool): Enable Caesar cipher decryption attempt.</li>
    <li><code>logs</code> (bool): Enable or disable logging.</li>
</ul>

<h3>Example Usage</h3>
<p>To use the <code>Decryptor</code> class, create an instance of it by providing the required parameters, and it will start performing hash decryption attempts in a separate thread. Here's an example:</p>

<pre><code>
import time
from bane.bruteforce import Decryptor

# Create an instance of Decryptor
u = "5f4dcc3b5aa765d61d8327deb882cf99"  # Example MD5 hash
word_list = ["password", "admin", "secret"]
decrypt_instance = Decryptor(u, word_list=word_list, md5_hash=True, logs=True)

# Hash decryption is performed in the background
# You can check the status with decrypt_instance.done()
while not decrypt_instance.done():
    time.sleep(1)

# Access the result
result = decrypt_instance.result
print("Decryption Result:", result)
</code></pre>
