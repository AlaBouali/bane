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
    cookie="CustomCookie=yuioiuyuioihyujiop",
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

<h1>Files_Manager_Finder Class</h1>

<h2>Class Overview</h2>
<p>The <code>Files_Manager_Finder</code> class is part of the "bane" module and is used to search for a specific file or resource on a website.</p>

<h2>Class Constructor</h2>
<pre><code>class Files_Manager_Finder(u, logs=True, threads_daemon=True, user_agent=None, cookie=None, timeout=10, headers={}, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></pre>
<p>This constructor initializes an instance of the <code>Files_Manager_Finder</code> class with the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target URL or website where the file or resource is being searched.</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is True).</li>
    <li><code>threads_daemon</code> (bool): Set thread as daemon (default is True).</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 10).</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include.</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use.</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use.</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use.</li>
</ul>

<h2>Methods</h2>
<h3><code>crack(self, u, user_agent, cookie, timeout, proxies, headers)</code></h3>
<p>This method performs the file or resource search operation with the specified parameters. It takes the following parameters:</p>
<ul>
    <li><code>u</code> (str): The target URL or website where the file or resource is being searched.</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>timeout</code> (int): Request timeout in seconds.</li>
    <li><code>proxies</code> (list): List of proxies to use for requests.</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include.</li>
</ul>

<h3><code>done(self)</code></h3>
<p>This method returns the value of the <code>finish</code> attribute, indicating whether the operation is done or not.</p>

<h2>Example Usage</h2>
<p>To use the <code>Files_Manager_Finder</code> class, create an instance of it by providing the required parameters, and it will start searching for the file or resource in a separate thread. Here's an example:</p>

<pre><code>
from bane.bruteforce import Files_Manager_Finder
import time

# Create an instance of Files_Manager_Finder
finder = Files_Manager_Finder(
    u="https://example.com",
    logs=True,
    threads_daemon=True,
    user_agent="CustomUserAgent",
    cookie="CustomCookie=ghjuiko",
    timeout=10,
    headers={"Custom-Header": "Value"},
    http_proxies=["1.1.1.1:8080", "2.2.2.2:80"],
    socks4_proxies=["3.3.3.3:1080"],
    socks5_proxies=None
)

# File/resource search is performed in the background
# You can check the status with finder.done()
while not finder.done():
    time.sleep(1)

# Access the result
result = finder.result
print("File/Resource Found:", result)
</code></pre>
<h1>Force_Browsing Class</h1>

<h2>Class Overview</h2>
<p>The <code>Force_Browsing</code> class is part of the "bane" module and is used to perform force browsing on a website by attempting to access various URLs with different extensions.</p>

<h2>Class Constructor</h2>
<pre><code>class Force_Browsing(u, timeout=10, threads_daemon=True, logs=True, ext="php", user_agent=None, cookie=None, headers={}, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></pre>
<p>This constructor initializes an instance of the <code>Force_Browsing</code> class with the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target website URL where force browsing is to be performed.</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 10).</li>
    <li><code>threads_daemon</code> (bool): Set thread as daemon (default is True).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is True).</li>
    <li><code>ext</code> (str): Default extension to use for URLs (default is 'php').</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include.</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use.</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use.</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use.</li>
</ul>

<h2>Methods</h2>
<h3><code>crack(self, u, timeout, logs, ext, user_agent, cookie, proxies)</code></h3>
<p>This method performs the force browsing operation with the specified parameters. It takes the following parameters:</p>
<ul>
    <li><code>u</code> (str): The target website URL where force browsing is to be performed.</li>
    <li><code>timeout</code> (int): Request timeout in seconds.</li>
    <li><code>logs</code> (bool): Enable or disable logging.</li>
    <li><code>ext</code> (str): Default extension to use for URLs.</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>proxies</code> (list): List of proxies to use for requests.</li>
</ul>

<h3><code>done(self)</code></h3>
<p>This method returns the value of the <code>finish</code attribute, indicating whether the operation is done or not.</p>

<h1>access Function</h1>

<h2>Function Overview</h2>
<p>The <code>access</code> function is part of the "bane" module and is used to access a specified URL with customizable parameters and check if it is accessible.</p>

<h3>Function Signature</h3>
<pre><code>access(u, timeout=10, user_agent=None, cookie=None, bypass=False, proxy=None, headers={})</code></pre>
<p>This function takes the following parameters:</p>

<ul>
    <li><code>u</code> (str): The URL to be accessed and checked.</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 10).</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>bypass</code> (bool): Enable or disable bypassing (default is False).</li>
    <li><code>proxy</code> (str): The proxy to use for requests.</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include.</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>Force_Browsing</code> class and the <code>access</code> function, you can create an instance of the class and call its methods or use the function as shown below:</p>

<pre><code>
import time
from bane.bruteforce.utils import *

# Create an instance of Force_Browsing
browsing = Force_Browsing(
    u="https://example.com",
    timeout=10,
    threads_daemon=True,
    logs=True,
    ext="php",
    user_agent="CustomUserAgent",
    cookie="CustomCookie=fgtyhuio",
    headers={"Custom-Header": "Value"},
    http_proxies=["1.1.1.1:8080", "2.2.2.2:80"],
    socks4_proxies=["3.3.3.3:1080"],
    socks5_proxies=None
)

# Force browsing is performed in the background
# You can check the status with browsing.done()
while not browsing.done():
    time.sleep(1)

# Access the result
result = browsing.result
print("Browsing Result:", result)

# Using the access function
url_to_access = "https://example.com/page"
is_accessible = access(
    u=url_to_access,
    timeout=10,
    user_agent="CustomUserAgent",
    cookie="CustomCookie=fghjkjhghujikjhujik",
    bypass=False,
    proxy={"http":"http://1.1.1.1:8080","https":"http://1.1.1.1:8080"},
    headers={"Custom-Header": "Value"}
)

if is_accessible:
    print("{} is accessible.".format(url_to_access))
else:
    print("{} is not accessible.".format(url_to_access))
</code></pre>
