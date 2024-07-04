import xmltodict
import yaml
import time

start = time.perf_counter()

for timer in range(100):
    with open('lab4_2.yaml', 'r') as yaml_file:
        input_file = yaml.safe_load(yaml_file)

    result = xmltodict.unparse(input_file, pretty=True)
    with open('lab4_2.xml', 'w') as xml_file:
        xml_file.write(result)

finish = time.perf_counter()
print(finish - start)