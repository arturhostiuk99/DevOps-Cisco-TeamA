import xml.etree.ElementTree as ET

def find_passwords(xml_file_path):
    try:
        root = ET.parse(xml_file_path).getroot()
        return [password.text for password in root.findall('.//password')]

    except ET.ParseError:
        print("Invalid XML format.")
        return None

if __name__ == "__main__":
    xml_file_path = "config.xml"
    
    passwords = find_passwords(xml_file_path)
    
    if passwords:
        for password_value in passwords:
            print(password_value)
    else:
        print("Passwords not found in the XML data.")