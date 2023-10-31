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
<h1>SHA1 Class</h1>

<h2>Class Overview</h2>
<p>The <code>SHA1</code> class is part of the "bane" module and provides methods for generating and comparing SHA-1 hash values for text and files.</p>

<h2>Methods</h2>

<h3><code>hash(w, encode=None)</code></h3>
<p>This method generates a SHA-1 hash value for the provided string or bytes-like object.</p>
<ul>
    <li><code>w</code> (str or bytes): The data for which the SHA-1 hash will be generated.</li>
    <li><code>encode</code> (str, optional): The encoding type to use (e.g., 'utf-8'). If not specified, the default encoding is used.</li>
</ul>
<p>Returns the SHA-1 hash value as a hexadecimal string.

<h3><code>hash_file(f)</code></h3>
<p>This method generates a SHA-1 hash value for the contents of a file.</p>
<ul>
    <li><code>f</code> (str): The path to the file for which the SHA-1 hash will be generated.</li>
</ul>
<p>Returns the SHA-1 hash value of the file's contents as a hexadecimal string.

<h3><code>compare_hash(word, hash)</code></h3>
<p>This method compares a given word with a SHA-1 hash value to check if they match.</p>
<ul>
    <li><code>word</code> (str): The word or data to be hashed and compared.</li>
    <li><code>hash</code> (str): The SHA-1 hash value to compare with the hashed <code>word</code>.</li>
</ul>
<p>Returns <code>True</code> if the hashed <code>word</code> matches the provided <code>hash</code>; otherwise, it returns <code>False</code>.

<h2>Example Usage</h2>
<p>To use the <code>SHA1</code> class, you can generate SHA-1 hash values for data and compare them as follows:</p>

<pre><code>
from bane.cryptographers import SHA1

# Generating a SHA-1 hash for a string
data = "Hello, World!"
hash_value = SHA1.hash(data)
print("SHA-1 Hash:", hash_value)

# Generating a SHA-1 hash for the contents of a file
file_path = "example.txt"
file_hash = SHA1.hash_file(file_path)
print("File SHA-1 Hash:", file_hash)

# Comparing a word with a SHA-1 hash
word_to_compare = "OpenAI"
given_hash = "2d3ac8bc1b411156957c5733bb7c4b69f9e7780d"
is_matched = SHA1.compare_hash(word_to_compare, given_hash)
print("Matched:", is_matched)
</code></pre>

<h1>SHA224 Class</h1>

<h2>Class Overview</h2>
<p>The <code>SHA224</code> class is part of the "bane" module and provides methods for generating and comparing SHA-224 hash values for text and files.</p>

<h2>Methods</h2>

<h3><code>hash(w, encode=None)</code></h3>
<p>This method generates a SHA-224 hash value for the provided string or bytes-like object.</p>
<ul>
    <li><code>w</code> (str or bytes): The data for which the SHA-224 hash will be generated.</li>
    <li><code>encode</code> (str, optional): The encoding type to use (e.g., 'utf-8'). If not specified, the default encoding is used.</li>
</ul>
<p>Returns the SHA-224 hash value as a hexadecimal string.

<h3><code>hash_file(f)</code></h3>
<p>This method generates a SHA-224 hash value for the contents of a file.</p>
<ul>
    <li><code>f</code> (str): The path to the file for which the SHA-224 hash will be generated.</li>
</ul>
<p>Returns the SHA-224 hash value of the file's contents as a hexadecimal string.

<h3><code>compare_hash(word, hash)</code></h3>
<p>This method compares a given word with a SHA-224 hash value to check if they match.</p>
<ul>
    <li><code>word</code> (str): The word or data to be hashed and compared.</li>
    <li><code>hash</code> (str): The SHA-224 hash value to compare with the hashed <code>word</code>.</li>
</ul>
<p>Returns <code>True</code> if the hashed <code>word</code> matches the provided <code>hash</code>; otherwise, it returns <code>False</code>.

<h2>Example Usage</h2>
<p>To use the <code>SHA224</code> class, you can generate SHA-224 hash values for data and compare them as follows:</p>

<pre><code>
from bane.cryptographers import SHA224

# Generating a SHA-224 hash for a string
data = "Hello, World!"
hash_value = SHA224.hash(data)
print("SHA-224 Hash:", hash_value)

# Generating a SHA-224 hash for the contents of a file
file_path = "example.txt"
file_hash = SHA224.hash_file(file_path)
print("File SHA-224 Hash:", file_hash)

# Comparing a word with a SHA-224 hash
word_to_compare = "OpenAI"
given_hash = "6d3549a83a1c75e1b29229ab5dd9b8ab02986f465bf48cf2a1bf8ebd"
is_matched = SHA224.compare_hash(word_to_compare, given_hash)
print("Matched:", is_matched)
</code></pre>


<h1>SHA256 Class</h1>

<h2>Class Overview</h2>
<p>The <code>SHA256</code> class is part of the "bane" module and provides methods for generating and comparing SHA-256 hash values for text and files.</p>

<h2>Methods</h2>

<h3><code>hash(w, encode=None)</code></h3>
<p>This method generates a SHA-256 hash value for the provided string or bytes-like object.</p>
<ul>
    <li><code>w</code> (str or bytes): The data for which the SHA-224 hash will be generated.</li>
    <li><code>encode</code> (str, optional): The encoding type to use (e.g., 'utf-8'). If not specified, the default encoding is used.</li>
</ul>
<p>Returns the SHA-256 hash value as a hexadecimal string.

<h3><code>hash_file(f)</code></h3>
<p>This method generates a SHA-256 hash value for the contents of a file.</p>
<ul>
    <li><code>f</code> (str): The path to the file for which the SHA-256 hash will be generated.</li>
</ul>
<p>Returns the SHA-256 hash value of the file's contents as a hexadecimal string.

<h3><code>compare_hash(word, hash)</code></h3>
<p>This method compares a given word with a SHA-256 hash value to check if they match.</p>
<ul>
    <li><code>word</code> (str): The word or data to be hashed and compared.</li>
    <li><code>hash</code> (str): The SHA-256 hash value to compare with the hashed <code>word</code>.</li>
</ul>
<p>Returns <code>True</code> if the hashed <code>word</code> matches the provided <code>hash</code>; otherwise, it returns <code>False</code>.

<h2>Example Usage</h2>
<p>To use the <code>SHA256</code> class, you can generate SHA-224 hash values for data and compare them as follows:</p>

<pre><code>
from bane.cryptographers import SHA256

# Generating a SHA-256 hash for a string
data = "Hello, World!"
hash_value = SHA256.hash(data)
print("SHA-256 Hash:", hash_value)

# Generating a SHA-256 hash for the contents of a file
file_path = "example.txt"
file_hash = SHA256.hash_file(file_path)
print("File SHA-256 Hash:", file_hash)

# Comparing a word with a SHA-256 hash
word_to_compare = "OpenAI"
given_hash = "6d3549a83a1c75e1b29229ab5dd9b8ab02986f465bf48cf2a1bf8ebd"
is_matched = SHA256.compare_hash(word_to_compare, given_hash)
print("Matched:", is_matched)
</code></pre>


<h1>SHA384 Class</h1>

<h2>Class Overview</h2>
<p>The <code>SHA384</code> class is part of the "bane" module and provides methods for generating and comparing SHA-224 hash values for text and files.</p>

<h2>Methods</h2>

<h3><code>hash(w, encode=None)</code></h3>
<p>This method generates a SHA-384 hash value for the provided string or bytes-like object.</p>
<ul>
    <li><code>w</code> (str or bytes): The data for which the SHA-384 hash will be generated.</li>
    <li><code>encode</code> (str, optional): The encoding type to use (e.g., 'utf-8'). If not specified, the default encoding is used.</li>
</ul>
<p>Returns the SHA-384 hash value as a hexadecimal string.

<h3><code>hash_file(f)</code></h3>
<p>This method generates a SHA-224 hash value for the contents of a file.</p>
<ul>
    <li><code>f</code> (str): The path to the file for which the SHA-224 hash will be generated.</li>
</ul>
<p>Returns the SHA-384 hash value of the file's contents as a hexadecimal string.

<h3><code>compare_hash(word, hash)</code></h3>
<p>This method compares a given word with a SHA-384 hash value to check if they match.</p>
<ul>
    <li><code>word</code> (str): The word or data to be hashed and compared.</li>
    <li><code>hash</code> (str): The SHA-384 hash value to compare with the hashed <code>word</code>.</li>
</ul>
<p>Returns <code>True</code> if the hashed <code>word</code> matches the provided <code>hash</code>; otherwise, it returns <code>False</code>.

<h2>Example Usage</h2>
<p>To use the <code>SHA384</code> class, you can generate SHA-384 hash values for data and compare them as follows:</p>

<pre><code>
from bane.cryptographers import SHA384

# Generating a SHA-384 hash for a string
data = "Hello, World!"
hash_value = SHA384.hash(data)
print("SHA-384 Hash:", hash_value)

# Generating a SHA-384 hash for the contents of a file
file_path = "example.txt"
file_hash = SHA384.hash_file(file_path)
print("File SHA-384 Hash:", file_hash)

# Comparing a word with a SHA-384 hash
word_to_compare = "OpenAI"
given_hash = "6d3549a83a1c75e1b29229ab5dd9b8ab02986f465bf48cf2a1bf8ebd"
is_matched = SHA384.compare_hash(word_to_compare, given_hash)
print("Matched:", is_matched)
</code></pre>


<h1>SHA512 Class</h1>

<h2>Class Overview</h2>
<p>The <code>SHA512</code> class is part of the "bane" module and provides methods for generating and comparing SHA-512 hash values for text and files.</p>

<h2>Methods</h2>

<h3><code>hash(w, encode=None)</code></h3>
<p>This method generates a SHA-512 hash value for the provided string or bytes-like object.</p>
<ul>
    <li><code>w</code> (str or bytes): The data for which the SHA-512 hash will be generated.</li>
    <li><code>encode</code> (str, optional): The encoding type to use (e.g., 'utf-8'). If not specified, the default encoding is used.</li>
</ul>
<p>Returns the SHA-512 hash value as a hexadecimal string.

<h3><code>hash_file(f)</code></h3>
<p>This method generates a SHA-512 hash value for the contents of a file.</p>
<ul>
    <li><code>f</code> (str): The path to the file for which the SHA-512 hash will be generated.</li>
</ul>
<p>Returns the SHA-512 hash value of the file's contents as a hexadecimal string.

<h3><code>compare_hash(word, hash)</code></h3>
<p>This method compares a given word with a SHA-512 hash value to check if they match.</p>
<ul>
    <li><code>word</code> (str): The word or data to be hashed and compared.</li>
    <li><code>hash</code> (str): The SHA-512 hash value to compare with the hashed <code>word</code>.</li>
</ul>
<p>Returns <code>True</code> if the hashed <code>word</code> matches the provided <code>hash</code>; otherwise, it returns <code>False</code>.

<h2>Example Usage</h2>
<p>To use the <code>SHA512</code> class, you can generate SHA-512 hash values for data and compare them as follows:</p>

<pre><code>
from bane.cryptographers import SHA512

# Generating a SHA-512 hash for a string
data = "Hello, World!"
hash_value = SHA512.hash(data)
print("SHA-512 Hash:", hash_value)
0
# Generating a SHA-512 hash for the contents of a file
file_path = "example.txt"
file_hash = SHA256.hash_file(file_path)
print("File SHA-512 Hash:", file_hash)

# Comparing a word with a SHA-512 hash
word_to_compare = "OpenAI"
given_hash = "6d3549a83a1c75e1b29229ab5dd9b8ab02986f465bf48cf2a1bf8ebd"
is_matched = SHA512.compare_hash(word_to_compare, given_hash)
print("Matched:", is_matched)
</code></pre>
<h1>XOR Class</h1>

<h2>Class Overview</h2>
<p>The <code>XOR</code> class is part of the "bane" module and provides methods for performing XOR encryption / decryption ( "encrypt" method does both ) on data and files using a given key.</p>

<h2>Methods</h2>

<h3><code>encrypt(data, key)</code></h3>
<p>This method performs XOR encryption on the provided data using the specified key.</p>
<ul>
    <li><code>data</code> (str or bytes): The data to be XOR encrypted.</li>
    <li><code>key</code> (str): The key used for XOR encryption.</li>
</ul>
<p>Returns the XOR encrypted data as a string.

<h3><code>encrypt_file(f, key)</code></h3>
<p>This method performs XOR encryption on the contents of a file using the specified key.</p>
<ul>
    <li><code>f</code> (str): The path to the file whose contents will be XOR encrypted.</li>
    <li><code>key</code> (str): The key used for XOR encryption.</li>
</ul>
<p>Returns the XOR encrypted contents of the file as a string.

<h2>Example Usage</h2>
<p>To use the <code>XOR</code> class, you can encrypt data and files using XOR encryption as follows:</p>

<pre><code>
from bane.cryptographers import XOR

# Encrypting a string using XOR encryption
data = "Hello, World!"
key = "SecretKey"
encrypted_data = XOR.encrypt(data, key)
print("XOR Encrypted Data:", encrypted_data)

# Encrypting the contents of a file using XOR encryption
file_path = "example.txt"
file_key = "AnotherSecretKey"
encrypted_file = XOR.encrypt_file(file_path, file_key)
print("XOR Encrypted File Contents:", encrypted_file)
</code></pre>
