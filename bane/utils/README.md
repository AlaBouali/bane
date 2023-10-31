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
</html>
