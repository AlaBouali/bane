<!DOCTYPE html>
<html>
<head>
</head>
<body>
<h1>Brute Force Hash Decryptor</h1>

<p>This Python code provides a tool for brute-forcing various types of hashes, including MD5, SHA1, SHA256, SHA224, SHA384, SHA512, base64, and Caesar ciphers. It can be used by security researchers to find matching plaintext values for given hash inputs.</p>

<h2>Class: decrypt</h2>
<p>The <code>decrypt</code> class is used to initiate the hash cracking process.</p>

<h3>Parameters:</h3>
<ul>
    <li><code>u</code>: The hash value to be cracked.</li>
    <li><code>word_list</code>: A list of words to be used for the brute force attack (default is an empty list).</li>
    <li><code>threads_daemon</code>: A boolean flag indicating whether threads should run as daemons (default is True).</li>
    <li><code>md5_hash</code>: A boolean flag to enable MD5 hash cracking (default is False).</li>
    <li><code>sha1_hash</code>: A boolean flag to enable SHA1 hash cracking (default is False).</li>
    <li><code>sha256_hash</code>: A boolean flag to enable SHA256 hash cracking (default is False).</li>
    <li><code>sha224_hash</code>: A boolean flag to enable SHA224 hash cracking (default is False).</li>
    <li><code>sha384_hash</code>: A boolean flag to enable SHA384 hash cracking (default is False).</li>
    <li><code>sha512_hash</code>: A boolean flag to enable SHA512 hash cracking (default is False).</li>
    <li><code>base64_string</code>: A boolean flag to enable base64 string decoding (default is False).</li>
    <li><code>caesar_hash</code>: A boolean flag to enable Caesar cipher cracking (default is False).</li>
    <li><code>logs</code>: A boolean flag to enable logging (default is False).</li>
</ul>

<h3>Methods:</h3>
<ul>
    <li><code>crack</code>: Initiates the hash cracking process.</li>
    <li><code>done</code>: Returns a boolean indicating whether the cracking process has finished.</li>
</ul>

<p>The <code>crack</code> method runs the brute force attack using the specified parameters and updates the result dictionary. The process can be stopped using the <code>stop</code> attribute. The <code>done</code> method can be used to check if the cracking process has finished.</p>

<h2>Example Usage:</h2>
<p>Below is an example of how to use the <code>decrypt</code> class to crack a hash:</p>

<pre><code>
from bane.bruteforce import *

# Initialize the decrypt class with appropriate parameters
d = decrypt(
    u="your_hash_here",
    word_list=[...],
    md5_hash=True,
    sha1_hash=True,
    sha256_hash=True,
    logs=True
)

# Check if the cracking process has finished
if d.done():
    # Get the result
    result = d.result
    print("Cracking result:", result)
</code></pre>

<p>Ensure that you have the required libraries and a valid word list for successful cracking.</p>
</body>
</html>
