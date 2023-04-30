xquery version "3.1";

declare variable $fileContent := string-join(
let $bojack := collection('/db/bojack')
let $title := $bojack
let $all := $bojack//* ! name() => distinct-values()
let $music := $bojack//music/normalize-space() ! lower-case(.) => distinct-values()
let $nonVerb := $bojack//nonVerbComm/normalize-space() ! lower-case(.) => distinct-values()
for $m in $music
    let $fileMatches := $bojack[.//music/normalize-space() ! lower-case(.) = $m] 
   (:  : let $countPerFile := 
        for $f in $fileMatches
            let $countM := $f//music[normalize-space() ! lower-case(.) = $m] => count()
            return $countM :)
    let $countMatches := $fileMatches//music[normalize-space() ! lower-case(.) = $m] => count()
    let $idNum := $fileMatches/base-uri() ! tokenize(.,"/")[last()] ! substring-before(.,".xml")
    let $epNum := $idNum ! substring(.,2,2)
    let $szn := $idNum ! substring(.,1,1) => distinct-values()
    for $i in $idNum
        let $iMatches := $fileMatches[/base-uri() ! tokenize(.,"/")[last()] ! substring-before(.,".xml") = $i] => count()
    order by $iMatches descending

return ( "Music:"|| "&#x9;"||$m || "&#x9;" || "id Count:"||"&#x9;"|| $iMatches ||"&#x9;"|| "i:" || $i),"&#10;" 
);

let $filename := "BojackMusicPerEp.tsv"
let $doc-db-uri := xmldb:store("/db/xquery", $filename, $fileContent, "text/plain")
return $doc-db-uri