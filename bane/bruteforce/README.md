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


<h2>Example Usage</h2>
<p>To use the <code>Force_Browsing</code> class , you can create an instance of the class and call its methods or use the function as shown below:</p>

<pre><code>
import time
from bane.bruteforce import Force_Browsing

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
is_accessible = Force_Browsing.access(
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

<h1>HTTP_Auth_Bruteforce Class</h1>

<h2>Class Overview</h2>
<p>The <code>HTTP_Auth_Bruteforce</code> class is part of the "bane" module and is used to perform HTTP authentication bruteforce attacks on a website.</p>

<h2>Class Constructor</h2>
<pre><code>class HTTP_Auth_Bruteforce(u, word_list=[], threads_daemon=True, logs=True, domain=None, cookie=None, user_agent=None, timeout=10, headers={}, http_proxies=None, socks4_proxies=None, socks5_proxies=None)</code></pre>
<p>This constructor initializes an instance of the <code>HTTP_Auth_Bruteforce</code> class with the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target website URL where the HTTP authentication bruteforce is to be performed.</li>
    <li><code>word_list</code> (list): A list of usernames and passwords for the bruteforce attack (default is an empty list).</li>
    <li><code>threads_daemon</code> (bool): Set thread as daemon (default is True).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is True).</li>
    <li><code>domain</code> (str): The domain for NTLM authentication (default is None).</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests.</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 10).</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include.</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use (default is None).</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use (default is None).</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use (default is None).</li>
</ul>

<h2>Methods</h2>
<h3><code>crack(self, u, domain, word_list, logs, proxies, cookie, user_agent, timeout, headers)</code></h3>
<p>This method performs the HTTP authentication bruteforce operation with the specified parameters. It takes the following parameters:</p>
<ul>
    <li><code>u</code> (str): The target website URL where the bruteforce attack is to be performed.</li>
    <li><code>domain</code> (str): The domain for NTLM authentication.</li>
    <li><code>word_list</code> (list): A list of usernames and passwords for the bruteforce attack.</li>
    <li><code>logs</code> (bool): Enable or disable logging.</li>
    <li><code>proxies</code> (list): List of proxies to use for requests.</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests.</li>
    <li><code>timeout</code> (int): Request timeout in seconds.</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include.</li>
</ul>

<h3><code>done(self)</code></h3>
<p>This method returns the value of the <code>finish</code attribute, indicating whether the operation is done or not.</p>

<h2>Example Usage</h2>
<p>To use the <code>HTTP_Auth_Bruteforce</code> class, create an instance of it by providing the required parameters, and it will start performing an HTTP authentication bruteforce attack in a separate thread. Here's an example:</p>

<pre><code>
import time
from bane.bruteforce import HTTP_Auth_Bruteforce

# Create an instance of HTTP_Auth_Bruteforce
auth_bruteforce = HTTP_Auth_Bruteforce(
    u="https://example.com",
    word_list=["username1:password1", "username2:password2"],
    threads_daemon=True,
    logs=True,
    domain=None,
    cookie="CustomCookie=ghjhhjkjhjk",
    user_agent="CustomUserAgent",
    timeout=10,
    headers={"Custom-Header": "Value"},
    http_proxies=["1.1.1.1:8080", "2.2.2.2:80"],
    socks4_proxies=None,
    socks5_proxies=None
)

# HTTP authentication bruteforce attack is performed in the background
# You can check the status with auth_bruteforce.done()
while not auth_bruteforce.done():
    time.sleep(1)

# Access the result
result = auth_bruteforce.result
print("auth_bruteforce Result:", result)
</code></pre>

<h1>Services_Login Class</h1>

<h2>Class Overview</h2>
<p>The <code>Services_Login</code> class provides a set of methods for performing various login/authentication attempts for different services, such as SMTP, Telnet, SSH, FTP, and MySQL. These methods check for successful login using the provided credentials and options.</p>

<h2>SMTP Login</h2>
<h3><code>smtp(u, username, password, p=25, ehlo=True, helo=False, ttls=False, proxy_type=None, proxy_host=None, proxy_port=None, proxy_username=None, proxy_password=None, timeout=5)</code></h3>
<p>This method attempts to log in to an SMTP server with the provided credentials and options. It returns <code>True</code> if the login is successful and <code>False</code> otherwise.</p>

<h2>Telnet Login</h2>
<h3><code>telnet(u, username, password, p=23, timeout=5, bot_mode=False, proxy_type=None, proxy_host=None, proxy_port=None, proxy_username=None, proxy_password=None)</code></h3>
<p>This method attempts to log in to a Telnet server with the provided credentials and options. It returns <code>True</code> if the login is successful and <code>False</code> otherwise. It also supports bot mode, where additional checks are performed to detect certain commands.</p>

<h2>SSH Login</h2>
<h3><code>ssh(u, username, password, p=22, timeout=5, exchange_key=None, proxy_type=None, proxy_host=None, proxy_port=None, proxy_username=None, proxy_password=None)</code></h3>
<p>This method attempts to log in to an SSH server with the provided credentials and options. It returns <code>True</code> if the login is successful and <code>False</code> otherwise. It supports the use of an exchange key for added security.</p>

<h2>FTP Login</h2>
<h3><code>ftp_anon(ip, p, timeout=5, proxy_type=None, proxy_host=None, proxy_port=None, proxy_username=None, proxy_password=None)</code></h3>
<p>This method attempts an anonymous FTP login to the specified IP and port. It returns <code>True</code> if the login is successful and <code>False</code> otherwise.</p>

<h3><code>ftp(ip, p, username, password, timeout=5, proxy_type=None, proxy_host=None, proxy_port=None, proxy_username=None, proxy_password=None)</code></h3>
<p>This method attempts to log in to an FTP server with the provided credentials and options. It returns <code>True</code> if the login is successful and <code>False</code> otherwise.</p>

<h2>MySQL Login</h2>
<h3><code>mysql(u, username, password, timeout=5, p=3306, proxy_type=None, proxy_host=None, proxy_port=None, proxy_username=None, proxy_password=None)</code></h3>
<p>This method attempts to log in to a MySQL database server with the provided credentials and options. It returns <code>True</code> if the login is successful and <code>False</code> otherwise.</p>

<h2>Parameters</h2>
<p>Many of the methods accept various parameters, including server address (<code>u</code>), username (<code>username</code>), password (<code>password</code>), port (<code>p</code>), and optional proxy settings. These parameters are used to customize the login attempts based on the specific service.</p>

<h1>Hydra Class</h1>

<h2>Class Overview</h2>
<p>The <code>Hydra</code> class is used for performing brute-force login attempts on various services, including SSH, Telnet, FTP, SMTP, MySQL, and WordPress. It takes a list of username-password combinations and tries to log in using different protocols. It reports success or failure for each combination.</p>

<h2>Class Constructor</h2>
<pre><code>class Hydra(u, p=22, protocol="ssh", word_list=[], threads_daemon=True, logs=True, exchange_key=None, timeout=5, ehlo=False, helo=True, ttls=False, user_agent=None, cookie=None, headers={}, http_proxies=None, socks4_proxies=None, socks5_proxies=None)
</code></pre>
<p>This constructor initializes an instance of the <code>Hydra</code> class with the following parameters:</p>

<ul>
    <li><code>u</code> (str): The target server or website URL.</li>
    <li><code>p</code> (int): The port to use for the protocol (default is 22).</li>
    <li><code>protocol</code> (str): The protocol to use for brute-forcing (e.g., "ssh", "telnet", "ftp", "smtp", "mysql", "wp").</li>
    <li><code>word_list</code> (list): List of username-password combinations to try.</li>
    <li><code>threads_daemon</code> (bool): Set thread as daemon (default is True).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is True).</li>
    <li><code>exchange_key</code> (str): The exchange key to use for SSH login (default is None).</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 5).</li>
    <li><code>ehlo</code> (bool): Enable EHLO for SMTP (default is False).</li>
    <li><code>helo</code> (bool): Enable HELO for SMTP (default is True).</li>
    <li><code>ttls</code> (bool): Enable TTLS for SMTP (default is False).</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests.</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include.</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use.</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use.</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use.</li>
</ul>

<h2>Methods</h2>
<h3><code>crack(self, u, p, protocol, word_list, logs, exchange_key, timeout, ehlo, helo, ttls, proxies, socket_proxies, user_agent, cookie, headers)</code></h3>
<p>This method performs brute-force login attempts with the specified parameters. It tries different combinations from the provided word list and checks for successful logins. The specific service is determined by the <code>protocol</code> parameter.</p>

<h3><code>done(self)</code></h3>
<p>This method returns <code>True</code> if the brute-force operation is finished and <code>False</code> otherwise.</p>

<h2>Example Usage</h2>
<p>To use the <code>Hydra</code> class, create an instance of it by providing the required parameters, and it will start brute-forcing logins for the specified protocol. Here's an example:</p>

<pre><code>
import time
from bane.bruteforce import Hydra

# Create an instance of Hydra for SSH login
hydra_ssh = Hydra(
    u="ssh.example.com",
    p=22,
    protocol="ssh",
    word_list=["user1:pass1", "user2:pass2"],
    logs=True,
    exchange_key=None,
    timeout=5
)

# Wait for the brute-force operation to finish
while not hydra_ssh.done():
    time.sleep(1)

# Access the result
result = hydra_ssh.result
print("Successful SSH login:", result)
</code></pre>
</p>

<h1>Web_Login_Bruteforce Class</h1>

<h2>Class Overview</h2>
<p>The <code>Web_Login_Bruteforce</code> class is used for performing brute-force login attempts on web-based login forms. It takes a list of username-password combinations and tries to log in by filling out the login form. It reports success or failure for each combination.</p>

<h2>Class Constructor</h2>
<pre><code>class Web_Login_Bruteforce(u, word_list=[], threads_daemon=True, logs=True, cookie=None, user_agent=None, timeout=10, headers={}, http_proxies=None, socks4_proxies=None, socks5_proxies=None)
</code></pre>
<p>This constructor initializes an instance of the <code>Web_Login_Bruteforce</code> class with the following parameters:</p>

<ul>
    <li><code>u</code> (str): The URL of the login page.</li>
    <li><code>word_list</code> (list): List of username-password combinations to try.</li>
    <li><code>threads_daemon</code> (bool): Set thread as daemon (default is True).</li>
    <li><code>logs</code> (bool): Enable or disable logging (default is True).</li>
    <li><code>cookie</code> (str): Custom cookies to include in requests.</li>
    <li><code>user_agent</code> (str): Custom User-Agent header for requests.</li>
    <li><code>timeout</code> (int): Request timeout in seconds (default is 10).</li>
    <li><code>headers</code> (dict): Additional HTTP headers to include.</li>
    <li><code>http_proxies</code> (list): List of HTTP proxies to use.</li>
    <li><code>socks4_proxies</code> (list): List of SOCKS4 proxies to use.</li>
    <li><code>socks5_proxies</code> (list): List of SOCKS5 proxies to use.</li>
</ul>

<h2>Methods</h2>
<h3><code>crack(self, u, word_list, logs, proxies, cookie, user_agent, timeout, headers)</code></h3>
<p>This method performs brute-force login attempts with the specified parameters. It tries different combinations from the provided word list and checks for successful logins by filling out the login form.</p>

<h3><code>done(self)</code></h3>
<p>This method returns <code>True</code> if the brute-force operation is finished and <code>False</code> otherwise.</p>

<h2>Example Usage</h2>
<p>To use the <code>Web_Login_Bruteforce</code> class, create an instance of it by providing the required parameters, and it will start brute-forcing logins on the specified web-based login form. Here's an example:</p>

<pre><code>
import time
from bane.bruteforce import Web_Login_Bruteforce

# Create an instance of Web_Login_Bruteforce
web_bruteforce = Web_Login_Bruteforce(
    u="https://example.com/login",
    word_list=["user1:pass1", "user2:pass2"],
    logs=True,
    cookie=None,
    user_agent="Custom User-Agent",
    timeout=10,
    headers={"Custom-Header": "Value"},
    http_proxies=["http://proxy1.com", "http://proxy2.com"],
    socks4_proxies=["socks4://socks4_proxy1", "socks4://socks4_proxy2"],
    socks5_proxies=["socks5://socks5_proxy1", "socks5://socks5_proxy2"]
)

# Wait for the brute-force operation to finish
while not web_bruteforce.done():
    time.sleep(1)

# Access the result
result = web_bruteforce.result
print("Successful login:", result)
</code></pre>
</p>