<h1>Userful_Utilities Class</h1>

<h2>Class Overview</h2>
<p>The <code>Userful_Utilities</code> class is part of the "bane" module and provides various utility methods for common tasks and operations.</p>

<h2>Class Methods</h2>

<h3><code>get_public_dns(timeout=15)</code></h3>
<p>This method retrieves a list of public DNS servers. It sends an HTTP request to "https://public-dns.info/nameservers.txt" and returns a list of public DNS servers. It takes the following parameters:</p>
<ul>
    <li><code>timeout</code> (int, optional): Request timeout in seconds (default is 15).</li>
</ul>

<h3><code>load_word_list(l)</code></h3>
<p>This method loads a word list from a file or a provided list and returns it as a list. It takes the following parameters:</p>
<ul>
    <li><code>l</code> (str, list, or tuple): The word list to be loaded, which can be either a file path or a list of words.</li>
</ul>

<h3><code>remove_html_tags(text)</code></h3>
<p>This method removes HTML tags from a string and returns the cleaned text. It takes the following parameter:</p>
<ul>
    <li><code>text</code> (str): The input text containing HTML tags.</li>
</ul>

<h3><code>remove_html_comments(text)</code></h3>
<p>This method removes HTML comments from a string and returns the cleaned text. It takes the following parameter:</p>
<ul>
    <li><code>text</code> (str): The input text containing HTML comments.</li>
</ul>

<h3><code>escape_html(s)</code></h3>
<p>This method escapes an HTML string to prevent cross-site scripting (XSS) attacks and returns the escaped HTML string. It takes the following parameter:</p>
<ul>
    <li><code>s</code> (str): The HTML string to be escaped.</li>
</ul>

<h3><code>unescape_html(s)</code></h3>
<p>This method unescapes an HTML string and returns the unescaped HTML string. It takes the following parameter:</p>
<ul>
    <li><code>s</code> (str): The HTML string to be unescaped.</li>
</ul>

<h3><code>youtube_search(q, proxy=None, timeout=10)</code></h3>
<p>This method performs a search on YouTube for videos related to a query and returns a list of video links. It takes the following parameters:</p>
<ul>
    <li><code>q</code> (str): The search query.</li>
    <li><code>proxy</code> (dict, optional): Proxy settings for the request.</li>
    <li><code>timeout</code> (int, optional): Request timeout in seconds (default is 10).</li>
</ul>

<h3><code>generate_human_poc(data)</code></h3>
<p>This method generates a human-readable Proof of Concept (PoC) based on the provided data. The data specifies whether to generate a URL or an HTML form and provides details of the action, inputs, and form attributes. It takes the following parameter:</p>
<ul>
    <li><code>data</code> (dict): The data containing PoC generation information.</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>Userful_Utilities</code> class, you can call its methods with the required parameters. Here's an example of using the <code>get_public_dns</code method:</p>

<pre><code>
from bane.utils import Userful_Utilities

#Get a list of public DNS servers
public_dns_servers = Userful_Utilities.get_public_dns()
print("Public DNS Servers:", public_dns_servers)
</code></pre>

<p>Here's an example of using the <code>remove_html_tags</code method:</p>

<pre><code>
from bane.utils import Userful_Utilities

#Remove HTML tags from a text
html_text = "<p>This is <strong>HTML</strong> text.</p>"
clean_text = Userful_Utilities.remove_html_tags(html_text)
print("Cleaned Text:", clean_text)
</code></pre>

<p>And here's an example of using the <code>generate_human_poc</code method:</p>

<pre><code>
from bane.utils import Userful_Utilities

#Generate a human-readable PoC as a URL
poc_data = {
    "is_url": True,
    "action": "https://example.com",
    "inputs": [
        {"name": "param1", "value": "value1"},
        {"name": "param2", "value": "value2"}
    ]
}
url_poc = Userful_Utilities.generate_human_poc(poc_data)
print("URL PoC:", url_poc)
</code></pre>
<h1>Files_Interface Class</h1>

<h2>Class Overview</h2>
<p>The <code>Files_Interface</code> class provides utility methods for working with files, including clearing, deleting, writing, and reading files. It also includes methods for creating and reading JSON files.</p>

<h2>Class Methods</h2>

<h3><code>clear_file(w)</code></h3>
<p>This method clears the contents of a file by opening it in write mode, effectively emptying the file. It takes the following parameter:</p>
<ul>
    <li><code>w</code> (str): The path to the file to be cleared.</li>
</ul>

<h3><code>delete_file(w)</code></h3>
<p>This method deletes a file if it exists. It takes the following parameter:</p>
<ul>
    <li><code>w</code> (str): The path to the file to be deleted.</li>
</ul>

<h3><code>write_file(w, fi, encode="utf-8")</code></h3>
<p>This method appends content to a file, optionally specifying the character encoding. It takes the following parameters:</p>
<ul>
    <li><code>w</code> (str): The content to be written to the file.</li>
    <li><code>fi</code> (str): The path to the file to which the content will be written.</li>
    <li><code>encode</code> (str, optional): The character encoding to use (default is "utf-8").</li>
</ul>

<h3><code>read_file(w, split_lines=True, remove_empty_lines=True)</code></h3>
<p>This method reads the contents of a file, optionally splitting it into lines and removing empty lines. It takes the following parameters:</p>
<ul>
    <li><code>w</code> (str): The path to the file to be read.</li>
    <li><code>split_lines</code> (bool, optional): Whether to split the content into lines (default is True).</li>
    <li><code>remove_empty_lines</code> (bool, optional): Whether to remove empty lines (default is True).</li>
</ul>

<h3><code>create_file(w)</code></h3>
<p>This method creates an empty file at the specified path, including any necessary directories in the path. It takes the following parameter:</p>
<ul>
    <li><code>w</code> (str): The path to the file to be created.</li>
</ul>

<h3><code>write_to_json(data, file_name, indent=4, **kwargs)</code></h3>
<p>This method writes data to a JSON file, specifying the data to write, the file name, and optional JSON formatting options. It takes the following parameters:</p>
<ul>
    <li><code>data</code> (dict): The data to be written to the JSON file.</li>
    <li><code>file_name</code> (str): The name of the JSON file to be created or overwritten.</li>
    <li><code>indent</code> (int, optional): The number of spaces for indentation in the JSON file (default is 4).</li>
    <li><code>**kwargs</code>: Additional keyword arguments for the <code>json.dump</code> function.</li>
</ul>

<h3><code>read_from_json(file_name, **kwargs)</code></h3>
<p>This method reads data from a JSON file and returns it as a dictionary, optionally specifying additional keyword arguments for the JSON loading process. It takes the following parameters:</p>
<ul>
    <li><code>file_name</code> (str): The name of the JSON file to be read.</li>
    <li><code>**kwargs</code>: Additional keyword arguments for the <code>json.load</code> function.</li>
</ul>

<h2>Example Usage</h2>
<p>To use the <code>Files_Interface</code> class, you can call its methods with the required parameters. Here's an example of using the <code>write_file</code method:</p>

<pre><code>
from bane.utils import Files_Interface

#Write content to a file
content = "This is a sample content."
file_path = "sample.txt"
Files_Interface.write_file(content, file_path)
</code></pre>

<p>Here's an example of using the <code>write_to_json</code method:</p>

<pre><code>
from bane.utils import Files_Interface

#Write data to a JSON file
data = {"name": "John", "age": 30}
json_file = "data.json"
Files_Interface.write_to_json(data, json_file)
</code></pre>

<p>And here's an example of using the <code>read_from_json</code> method:</p>

<pre><code>
from bane.utils import Files_Interface

#Read data from a JSON file
json_file = "data.json"
data = Files_Interface.read_from_json(json_file)
print("Read Data:", data)
</code></pre>
<h1>Bane_Instances_Interface Class</h1>

<h2>Class Overview</h2>
<p>The <code>Bane_Instances_Interface</code> class provides utility methods for working with instances of other classes, especially those created for parallel processing.</p>

<h2>Class Methods</h2>

<h3><code>process_threaded(a, check_interval=0.1)</code></h3>
<p>This method is used to process threaded instances. It checks if a threaded instance has completed its execution and returns the result or counter. It continuously monitors the threaded instance's status until it's done or interrupted by a keyboard interrupt (Ctrl+C). It takes the following parameters:</p>
<ul>
    <li><code>a</code> (ThreadedInstance): The threaded instance to be monitored.</li>
    <li><code>check_interval</code> (float, optional): The interval in seconds between checks (default is 0.1 seconds).</li>
</ul>

<h3><code>get_current_instances(instance_type)</code></h3>
<p>This method retrieves the currently active and inactive instances of a specified type. It scans the garbage collector's objects to find instances of the given type. It takes the following parameter:</p>
<ul>
    <li><code>instance_type</code> (str): The type of instances to be searched for. It should be specified as a string, such as "Admin_Panel_Finder" for an instance of that class.</li>
</ul>
<p>The method returns a dictionary containing lists of active and inactive instances.</p>

<h2>Example Usage</h2>
<p>Here's an example of using the <code>process_threaded</code method to monitor a threaded instance:</p>

<pre><code>
from bane.instances_interface import Bane_Instances_Interface

#Assume 'my_threaded_instance' is a threaded instance
result = Bane_Instances_Interface.process_threaded(my_threaded_instance)
print("Threaded Instance Result:", result)
</code></pre>

<p>And here's an example of using the <code>get_current_instances</code method to find active and inactive instances of a specific type:</p>

<pre><code>
from bane.instances_interface import Bane_Instances_Interface

#Find active and inactive instances of the 'Admin_Panel_Finder' type
instances_info = Bane_Instances_Interface.get_current_instances("Admin_Panel_Finder")
active_instances = instances_info["active"]
inactive_instances = instances_info["inactive"]

print("Active Instances:", active_instances)
print("Inactive Instances:", inactive_instances)
</code></pre>
<h1>Socket_Connection Class</h1>

<h2>Class Overview</h2>
<p>The <code>Socket_Connection</code> class is part of the "bane" module and provides methods for creating and configuring socket connections.</p>

<h2>Class Methods</h2>

<h3><code>wrap_socket_with_ssl(sock, target_host)</code></h3>
<p>Wrap a socket with SSL/TLS encryption and return the SSL-wrapped socket.</p>
<ul>
    <li><code>sock</code> (socket): The socket to be wrapped with SSL.</li>
    <li><code>target_host</code> (str): The target host for the SSL connection.</li>
</ul>

<h3><code>reorder_headers_randomly(s)</code></h3>
<p>Randomly reorder HTTP headers within an HTTP request string.</p>
<ul>
    <li><code>s</code> (str): The HTTP request string to reorder headers in.</li>
</ul>

<h3><code>random_param()</code></h3>
<p>Generate a random parameter for HTTP requests.</p>

<h3><code>setup_http_packet(target, ty, paths, post_field_min, post_field_max, post_min, post_max, cookie, user_agents)</code></h3>
<p>Generate an HTTP request packet with random headers and parameters.</p>
<ul>
    <li><code>target</code> (str): The target URL for the HTTP request.</li>
    <li><code>ty</code> (int): Type of request (1 for GET, 2 for POST).</li>
    <li><code>paths</code> (list): List of URL paths to choose from.</li>
    <li><code>post_field_min</code> (int): Minimum number of POST fields.</li>
    <li><code>post_field_max</code> (int): Maximum number of POST fields.</li>
    <li><code>post_min</code> (int): Minimum size of POST data.</li>
    <li><code>post_max</code> (int): Maximum size of POST data.</li>
    <li><code>cookie</code> (str): Custom cookies to include in the request.</li>
    <li><code>user_agents</code> (list): List of User-Agent headers to choose from.</li>
</ul>

<h3><code>get_socket_connection(host, port, timeout=5, no_delay=False, ssl_wrap=False, **kwargs)</code></h3>
<p>Get a socket connection using Proxies_Getter and optionally wrap it with SSL.</p>
<ul>
    <li><code>host</code> (str): The host to connect to.</li>
    <li><code>port</code> (int): The port to connect to.</li>
    <li><code>timeout</code> (int): Timeout for the connection (default is 5 seconds).</li>
    <li><code>no_delay</code> (bool): Enable TCP no delay (default is False).</li>
    <li><code>ssl_wrap</code> (bool): Wrap the socket with SSL (default is False).</li>
</ul>

<h3><code>get_tor_socket_connection(host, port, new_ip=True, ssl_wrap=False, timeout=5, no_delay=False, **kwargs)</code></h3>
<p>Get a Tor SOCKS5 socket connection using Proxies_Getter and optionally wrap it with SSL.</p>
<ul>
    <li><code>host</code> (str): The host to connect to.</li>
    <li><code>port</code> (int): The port to connect to.</li>
    <li><code>new_ip</code> (bool): Request a new Tor exit node IP (default is True).</li>
    <li><code>ssl_wrap</code> (bool): Wrap the socket with SSL (default is False).</li>
    <li><code>timeout</code> (int): Timeout for the connection (default is 5 seconds).</li>
    <li><code>no_delay</code> (bool): Enable TCP no delay (default is False).</li>
</ul>

<h2>Example Usage</h2>
<p>Here's an example of how to use the <code>Socket_Connection</code> class methods:</p>

<pre><code>
import socket
from bane import Socket_Connection

#Get a Tor SOCKS5 socket connection with SSL wrapping
s = Socket_Connection.get_tor_socket_connection("example.com", 80, new_ip=True, ssl_wrap=True, timeout=10, no_delay=False)

#Send data through the socket if needed
s.send(b"Hello, World!")

#Wrap an existing socket with SSL
existing_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
existing_socket.connect(("example.com", 443))
ssl_socket = Socket_Connection.wrap_socket_with_ssl(existing_socket, "example.com")
</code></pre>
<h1>Tor_Switch_Interface Class</h1>

<h2>Class Overview</h2>
<p>The <code>Tor_Switch_Interface</code> class provides methods for switching IP addresses when using the Tor network. It allows for automatic IP switching with or without a password, depending on the Tor configuration and platform.</p>

<h2>Class Methods</h2>

<h3><code>no_password(interval=30, logs=True)</code></h3>
<p>Automatically switch IP addresses in the Tor network without a password. This method is not suitable for Windows and relies on restarting the Tor service on Linux.</p>
<ul>
    <li><code>interval</code> (int): The interval in seconds between switching Tor's nodes (default is 30 seconds).</li>
    <li><code>logs</code> (bool): Show screen prints (default is True).</li>
</ul>

<h3><code>with_password(interval=30, password=None, p=9051, logs=True)</code></h3>
<p>Automatically switch IP addresses in the Tor network with a password. This method is platform-independent and works with Tor's control port.</p>
<ul>
    <li><code>interval</code> (int): The interval in seconds between switching Tor's nodes (default is 30 seconds).</li>
    <li><code>password</code> (str): The password for Tor's control port (required).</li>
    <li><code>p</code> (int): The Tor control port (default is 9051).</li>
    <li><code>logs</code> (bool): Show screen prints (default is True).</li>
</ul>

<h2>Example Usage</h2>

<h3>Using <code>no_password</code></h3>
<p>Switching IP addresses in the Tor network without a password (Linux only):</p>
<pre><code>
import bane

#Automatically switch IP addresses every 15 seconds (Linux only)
bane.Tor_Switch_Interface.no_password(interval=15)
</code></pre>

<h3>Using <code>with_password</code></h3>
<p>Switching IP addresses in the Tor network with a password (platform-independent):</p>
<pre><code>
import bane

#Set your Tor control port password
password = "your_password_here"

#Automatically switch IP addresses every 30 seconds (platform-independent)
bane.Tor_Switch_Interface.with_password(interval=30, password=password)
</code></pre>
<h1>Update_Module_Interface Class</h1>

<h2>Class Overview</h2>
<p>The <code>Update_Module_Interface</code> class provides methods for updating the "bane" module to a specified version or the latest version available.</p>

<h2>Class Methods</h2>

<h3><code>update_py2(version=None)</code></h3>
<p>Update the "bane" module for Python 2.x (pip).</p>
<ul>
    <li><code>version</code> (str, optional): The version of the "bane" module to update to (default is None).</li>
</ul>

<h3><code>update_py3(version=None)</code></h3>
<p>Update the "bane" module for Python 3.x (pip3).</p>
<ul>
    <li><code>version</code> (str, optional): The version of the "bane" module to update to (default is None).</li>
</ul>

<h3><code>update(version=None)</code></h3>
<p>Update the "bane" module based on the Python version used. For Python 2.x, it uses <code>update_py2</code>, and for Python 3.x, it uses <code>update_py3</code>.</p>
<ul>
    <li><code>version</code> (str, optional): The version of the "bane" module to update to (default is None).</li>
</ul>

<h2>Example Usage</h2>
<p>Here's how to use the <code>Update_Module_Interface</code> class methods to update the "bane" module:</p>

<h3>Update for Python 2.x (pip)</h3>
<p>Update the "bane" module for Python 2.x to the latest version:</p>
<pre><code>
import bane

#Update "bane" module for Python 2.x
bane.Update_Module_Interface.update_py2()
</code></pre>

<p>Update the "bane" module for Python 2.x to a specific version:</p>
<pre><code>
import bane

#Update "bane" module for Python 2.x to a specific version (e.g., "1.2.3")
bane.Update_Module_Interface.update_py2(version="1.2.3")
</code></pre>

<h3>Update for Python 3.x (pip3)</h3>
<p>Update the "bane" module for Python 3.x to the latest version:</p>
<pre><code>
import bane

#Update "bane" module for Python 3.x
bane.Update_Module_Interface.update_py3()
</code></pre>

<p>Update the "bane" module for Python 3.x to a specific version:</p>
<pre><code>
import bane

#Update "bane" module for Python 3.x to a specific version (e.g., "1.2.3")
bane.Update_Module_Interface.update_py3(version="1.2.3")
</code></pre>

<h3>Update Based on Python Version</h3>
<p>Update the "bane" module based on the Python version in use:</p>
<pre><code>
import bane

#Update "bane" module based on Python version
bane.Update_Module_Interface.update()
</code></pre>
</html>
