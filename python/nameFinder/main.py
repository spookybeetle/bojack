# STAGE 5: LET'S CLEAN THIS UP: DEALING WITH MESSY NLP TAGGING
# We will try adding an EntityRuler to guide spaCy.
# pip install saxonche
# The library above lets you read and pull data with XPath
import os
import spacy
from spacy.pipeline import EntityRuler
import re as regex
from saxonche import PySaxonProcessor
# ebb: The line above imports the PySaxonProcessor from SaxonCHE (free "home edition")
# for work with XPath


# nlp = spacy.cli.download("en_core_web_lg")
nlp = spacy.load('en_core_web_lg')

###############################################################################
################################################################################
# 1. ebb: Define the paths to the source collection and the target collection.
# We can use a relative path defined from this Python file's location.
##################################################################################
CollPath = '../../xmlFile/originalXML'
TargetPath = '../../xmlFile/outputXML'

#########################################################################################
# ebb: After reading the sorted dictionary output, we know spaCy is making some mistakes.
# So, here let's try adding an EntityRuler to customize spaCy's classification. We need
# to configure this BEFORE we send the tokens off to nlp() for processing.
##########################################################################################
# Create the EntityRuler and set it so the ner comes after, so OUR rules take precedence
# Sources:
#   W. J. B. Mattingly: https://ner.pythonhumanities.com/02_01_spaCy_Entity_Ruler.html
#   spaCy documentation on NER Entity Ruler: https://spacy.io/usage/rule-based-matching#entityruler

config = {"spans_key": None, "annotate_ents": True, "overwrite": True, "validate": True}
ruler = nlp.add_pipe("span_ruler", before="ner", config=config)
# 2023-04-07: ebb: NOTE: before="ner" setting seems to allow the spaCy NER rules to prevail over these patterns where
# there is a conflict.
# after="ner" means that the spaCy ner is TOTALLY OVERWRITTEN and invalidated by our patterns.

# Notes: Mattingly has this: ruler = nlp.add_pipe("entity_ruler", after="ner", config={"validate": True})
# But this only works when spaCy doesn't recognize a word / phrase as a named entity of any kind.
# If it recognizes a named entity but tags it wrong, we correct it with the span_ruler, not the entity_ruler
patterns = [
    {"label": "NULL", "pattern": [{"TEXT" : {"REGEX": "^-[A-z0-9]+?"}}]},
    {"label": "NULL", "pattern": [{"TEXT" : {"REGEX": "^[\"-]"}}]},
    {"label": "NULL", "pattern": [{"TEXT" : {"REGEX": "^[a-z0-9]"}}]},
    {"label": "NULL", "pattern": [{"TEXT" : {"REGEX": "[A-z0-9]*--"}}]},
    {"label": "NULL", "pattern": [{"TEXT" : {"REGEX": "[A-z0-9]+[^A-z^0-9]+[A-z0-9]+"}}]},
    {"label": "NULL", "pattern": [{"TEXT" : {"REGEX": "^.$"}}]},
    {"label": "NULL", "pattern": [{"TEXT" : {"REGEX": "^.{2}$"}}]},
    {"label": "NULL", "pattern": [{"TEXT" : {"REGEX": "^[Mm]+$"}}]},
    {"label": "NULL", "pattern": [{"TEXT" : {"REGEX": "^Oo"}}]},
    {"label": "NULL", "pattern": [{"TEXT" : {"REGEX": "^[A-Z][a-z]*[A-Z][a-z]*"}}]},
    {"label": "NULL", "pattern": "sun"},
    {"label": "NULL", "pattern": "Bo"},
    {"label": "NULL", "pattern": "gonna"},
    {"label": "NULL", "pattern": "Jack"},
    {"label": "NULL", "pattern": "Horse"},
    {"label": "NULL", "pattern": "Horsin"},
    {"label": "NULL", "pattern": "Mm-mmm"},
    {"label": "LOC", "pattern": "Gooba Gooberry Falls"},
    {"label": "PERSON", "pattern": "BoJack Horseman"},
    {"label": "PERSON", "pattern": "BoJack"},
    {"label": "PERSON", "pattern": "Charlotte"},
    {"label": "ORG", "pattern": "What Time Is It Right Now"},
    {"label": "ORG", "pattern": "whattimeisitrightnow.com"},
    {"label": "PERSON", "pattern": "Secretariat"},
    {"label": "PERSON", "pattern": "Hollyhock"},

]
ruler.add_patterns(patterns)

# 3. Here, the function imports each individual file, one at a time
# (received from the for-loop below.
def readTextFiles(filepath):
    # with open(filepath, 'r', encoding='utf8') as f:
    with PySaxonProcessor(license=False) as proc:
        xml = open(filepath, encoding='utf-8').read()
        # ebb: Here we changed to the Saxon processor to read files with XPath.
        # From here on, we change how we formulate the string that Python will send to NLP.
        xp = proc.new_xpath_processor()
        node = proc.parse_xml(xml_text=xml)
        xp.set_context(xdm_item=node)

        xpath = xp.evaluate('//script//line/text() ! normalize-space() => string-join()')
        # ebb: Let's get the string() value of all the <p> elements that are descendants of <book>.
        # The XPath function normalize-space() gets the string value and removes extra spaces.
        # That way we avoid the prologue, preface material.
        # I'm sending the whole thing to string-join() to bundle it together as one string
        # instead of a new string for every <p> element.
        # string = xpath.__str__()
        string = str(xpath)
        # ebb: Doing some regex replacements to clean up punctuation issues that are getting in the way of the NER tagger
        cleanedUp = regex.sub("_", " ", string)
        # cleanedUp = regex.sub(r"'([A-Z])]", r" \1", cleanedUp)
        cleanedUp = regex.sub(r"([.!?;'`])([A-Z'`]])", r"\1 \2", cleanedUp)
        # send to spaCy to collect nlp data on the big string
        tokens = nlp(cleanedUp)
        # tokens = nlp.pipe(cleanedUp, disable=["tagger", "parser", "attribute_ruler", "lemmatizer"])

        dictEntities = entitycollector(tokens)
        # ebb: The line above sends our nlp tokens to the named entity collector function.
        # THIS current function will receive and print a simple form of their output in the next line.
        print(f"{dictEntities=}")
        return(dictEntities)

#########################################################################################
# ebb: NEXT AFTER RETURNING ALL THE ENTITIES
# Remove duplicates (get the distinct values of the list of entities
# Output this information in a useful way
# Map it back into the XML files
# GO LOOK AT 2. and 5. below: functions involved: assemblAllNames and xmlTagger
##########################################################################################

# 4. ebb: The function below returns a simple list of named entities.
# But on the way, we're printing out as much we can from spaCy's classification of named entities:
def entitycollector(tokens):
    entities = {}
    for ent in sorted(tokens.ents):
        if ent.label_ == "LOC" or ent.label_=="ORG" or ent.label_=="GPE" or ent.label_=="NORP" or ent.label_=="PERSON":
            if not regex.match(r"^\w*[.,!?;:'\[\]]+\w*$", ent.text):
        # ebb: The line helps experiment with different spaCy named entity classifiers, in combination if you like:
        # When using it, remember to indent the next lines for the for loop.
            # stringify = (ent.text + ': ' + ent.label_ + ': ' + spacy.explain(ent.label_) + '\n')
            # stringify is a string-formatted version of this designed to provide an easily readable file output.
            # print(f"{stringify=}")
                entities[ent.text] = ent.label_
    print(f"{entities=}")
    return entities
    # ebb: Keep the return line in position at same indentation level as the definition of the entities variable.


# 2. and 5. ebb: The for loop below is working with your CollPath, and going through each file inside,
# and sending it up to readTextFiles, where the nlp processing will happen.
def assembleAllNames(CollPath):
    AllNames = {}
    for file in os.listdir(CollPath):
        if file.endswith(".xml"):
            filepath = f"{CollPath}/{file}"

            eachFileDict = readTextFiles(filepath)
            # The line above is effectively the return of readTextFiles()
            print(f"{eachFileDict=}")
            AllNames.update(eachFileDict)
            # ebb: The line above adds each file's new NLP data to the dictionary.

    print(f"{AllNames=}")
    AllNamesKeys = list(AllNames.keys())
    AllNamesKeys.sort()
    SortedDict =  {i: AllNames[i] for i in AllNamesKeys}
    print(f"{SortedDict=}")
    writeSortedEntries(SortedDict)
        # ebb: The function call in the above line will print the file to a useful output for review.
        # In a previous version of this file, we were printing the entire dictionary out to a file, and it was printing all the entries
        # out in one extremely long line. So I defined a simple function that will
        # output each entry as a string, line-by-line in the output file so the entries are easy
        # to read and review. We keep the dictionary as key-value pairs to send on to the xmlTagger function.

    for file in os.listdir(CollPath):
        if file.endswith(".xml"):
            sourcePath = f"{CollPath}/{file}"
            eachFileData = xmlTagger(sourcePath, SortedDict)
            # ebb: In the lines above, we send to the xmlTagger to add the nlp info as XML elements and attributes to the source files.
    return eachFileData
    # Python functions don't really need to have return lines, but we can set the return to the function's most important output.

def writeSortedEntries(dictionary):
    with open('distTrained-ORG-LOC-GPE-NORP.txt', 'w') as f:
        for key, value in dictionary.items():
            f.write(key + ' : ' + value + '\n')
def xmlTagger(sourcePath, SortedDict):
    with open(sourcePath, 'r', encoding='utf8') as f:
        readFile = f.read()
        stringFile = str(readFile)

        # ebb: Get the current filename. We need to know it to write its new output version
        filename = os.path.basename(f.name)
        print(f"{filename=}")
        targetFile = f"{TargetPath}/{filename}"
        print(f"{targetFile=}")

        # ebb: Work with stringFile variable to look for matches from the distinctNames set.
        for key, val in SortedDict.items():
            replacement = '<name type="' + val + '">' + key + '</name>'
            # print(f"{replacement=}")
            stringFile = stringFile.replace(key, replacement)
            cleanedUp = regex.sub(r"(<name type='[A-z]+?'>[^<>]*?)<name type='[^<>]+?'>([^<>]+?)</name>([^<]*?</name>)", r"\1\2\3", stringFile)
            cleanedUp = regex.sub(r"(\w+)<name type=[^<>]+>(\w+)</name>(\w*)", r"\1\2\3", cleanedUp)
            cleanedUp = regex.sub(r"(\w*)<name type=[^<>]+>(\w+)</name>(\w+)", r"\1\2\3", cleanedUp)
            cleanedUp = regex.sub(r"(<nonV[^<>]+?)<name type=\"[^<>]+?\">([^<>]+?)</name>([^<>]*>)", r"\1\2\3", cleanedUp)
            cleanedUp = regex.sub(r"(<name[^<>]+?>BoJack)</name>(\s+)<name[^<>]+?>(Horseman</name>)", r"\1\2\3", cleanedUp)

            # <nonVerbCo<name type="PERSON">mm</name>>
            # print(f"{stringFile=}")

        # ebb: Output goes in the taggedOutput directory: ../taggedOutput
        with open(targetFile, 'w') as f:
            f.write(cleanedUp)

assembleAllNames(CollPath)

# ebb: The functions are all initiated here now.
# This just delivers the collection path up to the first function in the sequence.