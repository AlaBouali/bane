<h1>BASE64 Class</h1>

<h2>Class Overview</h2>
<p>The <code>BASE64</code> class is part of the "bane" module and provides methods for encoding and decoding data using Base64 encoding.</p>

<h2>Methods</h2>

<h3><code>encode(w, encode=None)</code></h3>
<p>This method encodes a string or bytes-like object using Base64 encoding.</p>
<ul>
    <li><code>w</code> (str or bytes): The data to be encoded.</li>
    <li><code>encode</code> (str, optional): The encoding type to use (e.g., 'utf-8'). If not specified, the default encoding is used.</li>
</ul>
<p>Returns the Base64 encoded string as bytes.</p>

<h3><code>decode(w, encode=None)</code></h3>
<p>This method decodes a Base64 encoded string back to its original form.</p>
<ul>
    <li><code>w</code> (str or bytes): The Base64 encoded data to be decoded.</li>
    <li><code>encode</code> (str, optional): The encoding type to use when decoding (e.g., 'utf-8'). If not specified, the default encoding is used.</li>
</ul>
<p>Returns the decoded string as bytes.</p>

<h3><code>encode_file(f)</code></h3>
<p>This method encodes the contents of a file using Base64 encoding.</p>
<ul>
    <li><code>f</code> (str): The path to the file to be encoded.</li>
</ul>
<p>Returns the Base64 encoded file content as bytes.</p>

<h3><code>decode_file(f)</code></h3>
<p>This method decodes the contents of a Base64 encoded file back to its original form.</p>
<ul>
    <li><code>f</code> (str): The path to the file with Base64 encoded content.</li>
</ul>
<p>Returns the decoded file content as bytes.</p>

<h2>Example Usage</h2>
<p>To use the <code>BASE64</code> class, you can encode and decode data as follows:</p>

<pre><code>
from bane.cryptographers import BASE64

# Encoding a string
data = "Hello, World!"
encoded_data = BASE64.encode(data)
print("Encoded Data:", encoded_data)

# Decoding the encoded string
decoded_data = BASE64.decode(encoded_data)
print("Decoded Data:", decoded_data)

# Encoding and decoding a file
file_path = "example.txt"
encoded_file = BASE64.encode_file(file_path)
decoded_file = BASE64.decode_file(file_path)

# You can now work with the encoded_file and decoded_file as needed.
</code></pre>

<h1>CAESAR Class</h1>

<h2>Class Overview</h2>
<p>The <code>CAESAR</code> class is a part of the "bane" module and provides methods for encoding and decoding text using the Caesar cipher.</p>

<h2>Methods</h2>

<h3><code>encode(w, k)</code></h3>
<p>This method encodes a text using the Caesar cipher with a specified key.</p>
<ul>
    <li><code>w</code> (str): The text to be encoded.</li>
    <li><code>k</code> (int): The key to shift characters in the Caesar cipher. It must be an integer between 1 and 26.</li>
</ul>
<p>Returns the encoded text as a string.

<h3><code>decode(w, k)</code></h3>
<p>This method decodes a Caesar cipher encoded text using the specified key.</p>
<ul>
    <li><code>w</code> (str): The text to be decoded.</li>
    <li><code>k</code> (int): The key used for the Caesar cipher encoding. It must be the same key used for encoding.</li>
</ul>
<p>Returns the decoded text as a string.

<h2>Example Usage</h2>
<p>To use the <code>CAESAR</code> class, you can encode and decode text as follows:</p>

<pre><code>
from bane.cryptographers import CAESAR

# Encoding a text with a Caesar cipher
original_text = "Hello, World!"
key = 3
encoded_text = CAESAR.encode(original_text, key)
print("Encoded Text:", encoded_text)

# Decoding the encoded text with the same key
decoded_text = CAESAR.decode(encoded_text, key)
print("Decoded Text:", decoded_text)
</code></pre>
