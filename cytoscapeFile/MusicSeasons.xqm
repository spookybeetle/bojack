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
    for $s in $szn
        let $sMatches := $bojack[.//music/normalize-space() ! lower-case(.) = $m][/base-uri() ! tokenize(.,"/")[last()] ! substring-before(.,".xml") ! substring(.,1,1) = $s] => count()
        
    (:  :order by $sMatches descending :)
    
     (:  :for $f in $fileMatches :)

return ( "Music:"|| "&#x9;"||$m || "&#x9;" || "Season Count:"||"&#x9;"|| $sMatches ||"&#x9;"|| "S:" || $s),"&#10;" 
);

let $filename := "BojackMusicSeasoned.tsv"
let $doc-db-uri := xmldb:store("/db/xquery", $filename, $fileContent, "text/plain")
return $doc-db-uri



