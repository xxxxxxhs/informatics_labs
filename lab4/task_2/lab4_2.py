import xmltodict
import yaml

with open('lab4_2.yaml', 'r') as yaml_file:
    input_file = yaml.safe_load(yaml_file)

result = xmltodict.unparse(input_file, pretty=True)
with open('lab4_2.xml', 'w') as xml_file:
    xml_file.write(result)
