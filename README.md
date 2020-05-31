# Language List for Python - RFC5646 (inc ISO-639, ISO-15924, ISO-3166)
RFC5646 is an effort to define "Tags for Identifying Language."
This RFC5646 is also known as **BCP-47** (Best Current Practice #47)

You can see the full text here: [https://tools.ietf.org/html/rfc5646](https://tools.ietf.org/html/rfc5646)

-----

## TL;DR; RFC5646 summary
The language tag based on this RFC can be very complex. While `en-US` is simple enough to mean 'English as used in the United States", it can get more complicated such as: `hy-Latn-IT-arevela` which means 'Eastern Armenian language written in Latin script, as used in Italy'

The tag is designed to have a maximum of 35 character (para 4.4.1)
[language:8]-[script:5]-[region:4]-[variant1:9]-[variant2:9]

Internet Assigned Number Authority maintains the official record of all approved language tags ([iana](https://www.iana.org/)).

Extracted from those official record are these 7 python files that contain the tag and the description of all the language tag. While the typical application probably deals with the "language tag" section only, you might need some other part as well.

There are currently 9116 language tag records.

### "Language Tag" - RFC5646_language.py - 8177 records
Basically **ISO-639** list (2 or 3 characters) or other sublanguage/future use.
This is the primary language tag

### "Extended Language Tag" - RFC5646_extlang.py -239 records
Also part of **ISO-639** or some reserved used.

### "Script Tag" - RFC5646_script.py - 202 records
This part is from **ISO-15924**

### "Region Tag" - RFC5646_region.py - 304 records
This part is either from **ISO-3166-1** or 3 digit United Nation UN M.49 code

### "Variant Tag" - RFC5646_variant.py - 102 records
Some registered variants.

### "Grandfathered Tag" - RFC5646_grandfathered.py - 26 records
Non-redundant tags registered during the RFC 3066 era. This includes "i-klingon" and "i-enochian" language tag if you must know.

### "Redundant Tag" - RFC5646_redundant.py - 66 records
Some rare and almost-never-been-used tag.

## Language Tag List: 
Source: [iana.org](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry)

### Data example:
    ```
    %%
    Type: language
    Subtag: bi
    Description: Bislama
    Added: 2005-10-16
    %%
    Type: language
    Subtag: bm
    Description: Bambara
    Added: 2005-10-16
    %%
    Type: language
    Subtag: bn
    Description: Bengali
    Description: Bangla
    Added: 2005-10-16
    Suppress-Script: Beng
    %%
    ```
### Format
* Each entry separated by "%%"
* The number of records each entry can vary. E.g., multiple descriptions, additionals field, etc

## How to use
* The easiest is copy and paste the content into your file. If it is too much, just include it as a module.
* If you use other programming languages than python, copy-paste the content in a text editor to reformat according to the language requirement.

### To update the record
* Save the display from iana.org database to a text file. In this repository, name it "language-subtag-registry.txt"
* Use the included `extractor.py` to generate the new file
* Note, if iana.org changes the display/format, a fiddle around `extractor.py` to get a correct parsing is required