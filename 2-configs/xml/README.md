# XML Password Extractor

This Python script allows you to extract and display passwords from an XML file.

## Getting Started

1.  Create or have an XML file containing user data with password elements. The XML file should have a structure similar to this:

```xml
<users>
    <user>
        <username>user1</username>
        <password>password1</password>
        <email>user1@example.com</email>
    </user>
</users>
```

Place the XML file in the same directory as the `xml_parser.py` script.

2. Navigate to the directory containing the `xml_parser.py` script and the XML file.

3. Run the script using the following command:

```
python3 xml_parser.py
```
The script will search for and display all the password values found in the XML file.

4. Example Output
```
password1
password2
password3
password4
password5
password6
```