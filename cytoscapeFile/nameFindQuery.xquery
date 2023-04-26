xquery version "3.1";
(: Example XQuery to output TSV formatted network data for Cytoscape network analysis 
Redoing this for running on a local computer with oXygen XML Editor
In oXygen we don't need the complex setup to save the file, but you do still need to output a string-join to 
bundle the text file together.
:)
    (: For a text output, start with a half-open string-join to bundle the file together  :)
(: This line below is for eXist-dB: :)
(: let $lotrLoc := collection('/db/lotrLoc') :)
(: For oXygen XML Editor and your collection files loaded nearby: make sure you add the part to filter out non-XML files from your local system.:)

declare variable $textFileContent := string-join(
let $bojack := collection('../xmlFile/?select=*.xml')

let $names := $bojack//name
let $distinctNames := $names ! normalize-space() => distinct-values() => sort()
let $epTitle := $bojack//title
(: Okay, let's get data on which book-chapters the various names turn up in, 
 : and what kinds of names they are:)
    for $d in $distinctNames
    let $dType := ($bojack//name[. ! normalize-space() = $d])[1]/@type ! string()
    (:  SOURCE NODE ($d) + CATEGORY DESCRIPTOR ($dType)
    Pick up the type from just the very first match: we need a sequence of exactly one for the string concatenation :)
    let $eps := $bojack/xml[.//name ! normalize-space() = $d]
    (: We should splice the book info to the chapter info for these :)
        for $e in $eps
            let $eID := $e/@xml:id ! data()
            let $script := $e//script[.//name ! normalize-space() = $e]
                (: Now we find the connected names in each chapter :)
                for $s in $script
                    (: EDGE CONNECTOR is $cID. We can use $bID (the book title info) as an EDGE DESCRIPTOR for styling :)
                    let $connectedNames := $s[.//name ! normalize-space() = $e]//name[not(. ! normalize-space() = $e)]
                    (: This says, find the connected names in the chapter that are NOT the same as the source node:)
                    let $distinctTargets := $connectedNames => distinct-values() 
                    (: Taking distinct values to simplify the output :)
                        for $t in $distinctTargets
                        (: This is a tab character that we use for a separator in preparing the network data:  "&#x9;":)
            return ($e (: source :) ||  "&#x9;" || $dType (: source att :) || "&#x9;" || $eID  (: edge :)|| "&#x9;" ||  $t (: target :)), "&#10;");
        (: The string-join that ties the file together wraps up with a line-return at the 
        end of each row with "&#10;" You have to end the global variable with the ; (a semicolon). :)
 $textFileContent