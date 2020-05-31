""" Extract the language tag data from Iana.org database
    https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry

"""
import string
file = open('language-subtag-registry.txt', 'r', encoding="utf8")

no_of_record = 0
record_type = []
data = []
the_list = []
the_type = set([])
counter = {}
the_tag = {}
for row in file:
    # print(row)
    data_in_record_type = len(record_type)
    if "%%" in row and data_in_record_type > 1:
        the_list.append(record_type)
        tag_type = ""
        for (current_field, current_record) in record_type:
            if "type" in current_field:
                tag_type = current_record
                if current_record in counter:
                    counter[current_record] += 1
                else:
                    counter[current_record] = 1
                    the_tag[current_record] = []
            if "tag" in current_field:
                the_tag[tag_type].append(record_type)
        record_type = []
        no_of_record += 1
        continue

    if ":" in row:
        data = row.split(":")
        field = data[0].translate(
            {ord(c): None for c in string.whitespace}).lower()
        record = data[1].replace('\n', '').strip()
        record_type.append([field, record])
    if "type" in field:
        the_type.add(record)

for type in the_type:
    new_file = open("RFC5646_"+type+".py", mode="w", encoding="utf-8")
    print("RFC5646_"+type+"= {")
    new_file.writelines("RFC5646_"+type+"= {\n")

    for item in the_tag[type]:
        tag_desc = ""
        tag_data = ""
        for field, data in item:
            if 'tag' in field:
                tag_data = data
            if 'desc' in field:
                tag_desc += data.translate(str.maketrans({"'":  r"\'",
                                                          "]":  r"\]",
                                                          "\\": r"\\",
                                                          "^":  r"\^",
                                                          "$":  r"\$",
                                                          "*":  r"\*"}))+". "
        print("    '"+tag_data+"':'"+tag_desc+"',")
        new_file.writelines("    '"+tag_data+"':'"+tag_desc+"',\n")
    print("}")
    new_file.writelines("}\n")
    new_file.close()
file.close()

print("The type:", the_type)
print("The counter:", counter)
print("Total record:", no_of_record)
