<h1>Botnet_Master Class</h1>

<h2>Class Overview</h2>
<p>The <code>Botnet_Master</code> class is part of the "bane" module and is used for managing botnet operations.</p>

<h2>Class Methods</h2>
<h3><code>send_data(data, sock, timeout=2, real_timeout=3, xor_key=None)</code></h3>
<p>Sends data over a socket connection, optionally XOR encrypting it.</p>

<h3><code>login(host, port, username, password, timeout=3, read_timeout=2, tor=False)</code></h3>
<p>Logs in to a remote host using a socket connection.</p>

<h3><code>execute(cmd, timeout=2, real_timeout=3)</code></h3>
<p>Sends a command to the remote host and receives the response.</p>

<h3><code>close()</code></h3>
<p>Closes the socket connection.</p>

<h3><code>read_data(sock, timeout=2, real_timeout=3, xor_key=None)</code></h3>
<p>Reads data from a socket connection, optionally XOR decrypting it.</p>

<h3><code>interact(host, port, read_timeout=3, timeout=3, tor=False, xor_key=None)</code></h3>
<p>Interacts with a remote host, allowing commands to be sent and responses to be received.</p>

<h2>Method Parameters</h2>
<p>Here are the parameters used by the class methods:</p>

<ul>
<li><code>data</code> (str): The data to be sent.</li>
<li><code>sock</code> (socket object): The socket connection.</li>
<li><code>timeout</code> (int, optional): Timeout for socket operations. Default is 2 seconds.</li>
<li><code>real_timeout</code> (int, optional): Real timeout for socket operations. Default is 3 seconds.</li>
<li><code>xor_key</code> (str, optional): XOR encryption key. Default is None.</li>
<li><code>host</code> (str): The target host for the socket connection.</li>
<li><code>port</code> (int): The port for the socket connection.</li>
<li><code>username</code> (str): Username for login.</li>
<li><code>password</code> (str): Password for login.</li>
<li><code>tor</code> (bool, optional): Use Tor for the connection. Default is False.</li>
</ul>

<h2>Example Usage</h2>
<p>Here's an example of how to use the <code>Botnet_Master</code> class:</p>

<pre>
<code>
import time
from bane import Botnet_Master

#Create an instance of Botnet_Master
botnet = Botnet_Master()

#Connect to a remote host
botnet.login("example.com", 80, "username", "password")

#Execute a command on the remote host
response = botnet.execute("ls -l")

#Close the connection
botnet.close()

#Interact with the host
botnet.interact("example.com", 80)
</code>
</pre>

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

#Create an instance of Botnet_Scanner
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

#Scanning is performed in the background
while not scanner.done():
    time.sleep(1)

#Access the result
result = scanner.result
print("Found credentials:", result)
</code></pre>
<h1>Botnet_C_C_Server Class</h1>

<h2>Class Overview</h2>
<p>The <code>Botnet_C_C_Server</code> class is part of the "bane" module and is used for managing a Command and Control (C&C) server for a botnet.</p>

<h2>Class Methods</h2>

<h3><code>send_data(self, data, sock, xor_key=None, read_output=False, is_bot=True)</code></h3>
<p>Sends data over a socket connection, optionally XOR encrypting it.</p>

<h3><code>read_data(sock, xor_key=None)</code></h3>
<p>Reads data from a socket connection, optionally XOR decrypting it.</p>

<h3><code>process_cmd(self, cmd, user_socket, user)</code></h3>
<p>Processes a command received from a user and sends it to bot clients.</p>

<h3><code>ping(self)</code></h3>
<p>Sends periodic ping commands to bot clients to check their status.</p>

<h3><code>login(self, **kwargs)</code></h3>
<p>Checks if a user login is valid based on provided credentials.</p>

<h3><code>send_command(self, command, user_socket, user, is_ping=False)</code></h3>
<p>Sends a command to bot clients or user and handles responses.</p>

<h3><code>handle_bot(self, client_socket)</code></h3>
<p>Handles bot clients, sends initial commands, and manages bot connections.</p>

<h3><code>handle_user(self, client_socket)</code></h3>
<p>Handles user connections, performs login, and processes user commands.</p>

<h3><code>run_bots_server(self)</code></h3>
<p>Starts the server for accepting connections from bot clients and handles bot connections.</p>

<h3><code>run_users_server(self)</code></h3>
<p>Starts the server for accepting connections from users and handles user connections.</p>

<h3><code>kill(self)</code></h3>
<p>Cleans up and terminates the C&C server.</p>

<h2>Method Parameters</h2>
<p>Here are the parameters used by the class methods:</p>

<ul>
<li><code>data</code> (str): The data to be sent.</li>
<li><code>sock</code> (socket object): The socket connection.</li>
<li><code>xor_key</code> (str, optional): XOR encryption key. Default is None.</li>
<li><code>read_output</code> (bool, optional): Whether to read and return the output. Default is False.</li>
<li><code>is_bot</code> (bool, optional): Indicates if the operation is performed on a bot client. Default is True.</li>
<li><code>user_socket</code> (socket object): The user socket connection.</li>
<li><code>user</code> (str): The username of the user.</li>
<li><code>command</code> (str): The command to send to bot clients or user.</li>
<li><code>is_ping</code> (bool, optional): Indicates if the command is a ping. Default is False.</li>
<li><code>kwargs</code> (dictionary): Keyword arguments for user login.</li>
<li><code>users_host</code> (str): Host for user connections. Default is '0.0.0.0'.</li>
<li><code>ping_command</code> (str): The ping command to be sent to bot clients.</li>
<li><code>pings_interval</code> (int): Interval for sending ping commands. Default is 5 seconds.</li>
<li><code>threads_daemon</code> (bool, optional): Whether to set threads as daemons. Default is False.</li>
<li><code>users_encryption_key</code> (str): Encryption key for user connections.</li>
<li><code>users_port</code> (int): Port for user connections. Default is 22222.</li>
<li><code>bots_host</code> (str): Host for bot connections. Default is '0.0.0.0'.</li>
<li><code>bots_port</code> (int): Port for bot connections. Default is 7777.</li>
<li><code>socket_buffer_size</code> (int): Size of the socket buffer. Default is 4096.</li>
<li><code>max_users</code> (int): Maximum number of user connections. Default is 5.</li>
<li><code>max_bots</code> (int): Maximum number of bot connections. Default is 100.</li>
<li><code>logs</code> (bool): Enable or disable logging. Default is False.</li>
<li><code>initial_commands_list</code> (list): List of initial commands to send to bot clients.</li>
<li><code>bots_encryption_key</code> (str): Encryption key for bot connections.</li>
<li><code>users</code> (list): List of user credentials for login.</li>
</ul>

<h2>Example Usage</h2>
<p>Here's an example of how to use the <code>Botnet_C_C_Server</code> class:</p>

<pre>
<code>
import time
from bane import Botnet_C_C_Server

#Create an instance of Botnet_C_C_Server
cnc_server = Botnet_C_C_Server()

#The server will listen for bot clients and user connections in separate threads.
#The server can be killed with cnc_server.kill() when no longer needed.
</code>
</pre>
<h1>Botnet_Malware_Download_Server Class</h1>

<h2>Class Overview</h2>
<p>The <code>Botnet_Malware_Download_Server</code> class is used for creating a server to download malware files from a specified folder while preventing path traversal vulnerabilities.</p>

<h2>Class Methods</h2>

<h3><code>download(self, filename)</code></h3>
<p>Downloads a malware file from the specified folder while preventing path traversal vulnerabilities.</p>

<h3><code>__init__(self, malwares_folder, host='0.0.0.0', port=6666, debug=True)</code></h3>
<p>Class constructor to initialize the malware download server with the following parameters:</p>
<ul>
<li><code>malwares_folder</code> (str): The folder where malware files are stored.</li>
<li><code>host</code> (str): Host for the server. Default is '0.0.0.0'.</li>
<li><code>port</code> (int): Port for the server. Default is 6666.</li>
<li><code>debug</code> (bool): Enable or disable debugging. Default is True.</li>
</ul>

<h3><code>run(self)</code></h3>
<p>Starts the malware download server with the specified host and port.</p>

<h3><code>set_route(self, *args, **kwargs)</code></h3>
<p>Sets custom routes for the server using Flask's add_url_rule method.</p>

<h2>Method Parameters</h2>
<p>Here are the parameters used by the class methods:</p>
<ul>
<li><code>filename</code> (str): The name of the malware file to download.</li>
<li><code>path</code> (str): The path to the malware file.</li>
<li><code>malwares_folder</code> (str): The folder where malware files are stored.</li>
<li><code>host</code> (str): Host for the server.</li>
<li><code>port</code> (int): Port for the server.</li>
<li><code>debug</code> (bool): Enable or disable debugging.</li>
<li><code>args</code> (tuple): Positional arguments for setting custom routes.</li>
<li><code>kwargs</code> (dict): Keyword arguments for setting custom routes.</li>
</ul>

<h2>Example Usage</h2>
<p>Here's an example of how to use the <code>Botnet_Malware_Download_Server</code> class:</p>
<pre>
<code>
import time
from bane import Botnet_Malware_Download_Server

#Create an instance of Botnet_Malware_Download_Server
malware_server = Botnet_Malware_Download_Server(malwares_folder='/path/to/malwares')

#Set custom routes if needed
#malware_server.set_route('/custom_route', endpoint='custom_endpoint', view_func=custom_function)

#Start the malware download server
malware_server.run()
</code>
</pre>
<h1>Botnet_Reporting_Server Class</h1>

<h2>Class Overview</h2>
<p>The <code>Botnet_Reporting_Server</code> class is used for creating a server for reporting and retrieving data from a specified folder.</p>

<h2>Class Methods</h2>

<h3><code>get_server(self)</code></h3>
<p>Retrieves the Flask server instance used in the reporting server.</p>

<h3><code>__init__(self, malwares_folder, host='0.0.0.0', port=11111, debug=True)</code></h3>
<p>Class constructor to initialize the reporting server with the following parameters:</p>
<ul>
<li><code>malwares_folder</code> (str): The folder where data is stored.</li>
<li><code>host</code> (str): Host for the server. Default is '0.0.0.0'.</li>
<li><code>port</code> (int): Port for the server. Default is 11111.</li>
<li><code>debug</code> (bool): Enable or disable debugging. Default is True.</li>
</ul>

<h3><code>run(self)</code></h3>
<p>Starts the reporting server with the specified host and port.</p>

<h3><code>set_route(self, *args, **kwargs)</code></h3>
<p>Sets custom routes for the server using Flask's add_url_rule method.</p>

<h2>Method Parameters</h2>
<p>Here are the parameters used by the class methods:</p>
<ul>
<li><code>host</code> (str): Host for the server.</li>
<li><code>port</code> (int): Port for the server.</li>
<li><code>debug</code> (bool): Enable or disable debugging.</li>
<li><code>malwares_folder</code> (str): The folder where data is stored.</li>
<li><code>args</code> (tuple): Positional arguments for setting custom routes.</li>
<li><code>kwargs</code> (dict): Keyword arguments for setting custom routes.</li>
</ul>

<h2>Example Usage</h2>
<p>Here's an example of how to use the <code>Botnet_Reporting_Server</code> class:</p>
<pre>
<code>
import time
from bane import Botnet_Reporting_Server

#Create an instance of Botnet_Reporting_Server
reporting_server = Botnet_Reporting_Server()

#Set custom routes if needed
#reporting_server.set_route('/custom_route', endpoint='custom_endpoint', view_func=custom_function)

#Start the reporting server
reporting_server.run()
</code></pre>

<h1>Botnet_Web_Interface_Server Class</h1>

<h2>Class Overview</h2>
<p>The <code>Botnet_Web_Interface_Server</code> class is used for creating a web interface server for managing data from a specified folder.</p>

<h2>Class Methods</h2>

<h3><code>get_server(self)</code></h3>
<p>Retrieves the Flask server instance used in the web interface server.</p>

<h3><code>__init__(self, data_folder, host='0.0.0.0', port=33333, debug=True)</code></h3>
<p>Class constructor to initialize the web interface server with the following parameters:</p>
<ul>
    <li><code>data_folder</code> (str): The folder where data is managed.</li>
    <li><code>host</code> (str): Host for the server. Default is '0.0.0.0'.</li>
    <li><code>port</code> (int): Port for the server. Default is 33333.</li>
    <li><code>debug</code> (bool): Enable or disable debugging. Default is True.</li>
</ul>

<h3><code>run(self)</code></h3>
<p>Starts the web interface server with the specified host and port.</p>

<h3><code>set_route(self, *args, **kwargs)</code></h3>
<p>Sets custom routes for the server using Flask's add_url_rule method.</p>

<h2>Method Parameters</h2>
<p>Here are the parameters used by the class methods:</p>
<ul>
    <li><code>host</code> (str): Host for the server.</li>
    <li><code>port</code> (int): Port for the server.</li>
    <li><code>debug</code> (bool): Enable or disable debugging.</li>
    <li><code>data_folder</code> (str): The folder where data is managed.</li>
    <li><code>args</code> (tuple): Positional arguments for setting custom routes.</li>
    <li><code>kwargs</code> (dict): Keyword arguments for setting custom routes.</li>
</ul>

<h2>Example Usage</h2>
<p>Here's an example of how to use the <code>Botnet_Web_Interface_Server</code> class:</p>
<pre>
    <code>
import time
from bane import Botnet_Web_Interface_Server

#Create an instance of Botnet_Web_Interface_Server
web_interface_server = Botnet_Web_Interface_Server()

#Set custom routes if needed
#web_interface_server.set_route('/custom_route', endpoint='custom_endpoint', view_func=custom_function)

#Start the web interface server
web_interface_server.run()
    </code>
</pre>
