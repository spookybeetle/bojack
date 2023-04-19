declare variable $bojack := collection("../xmlFile/outputXML/?select=*.xml");

declare variable $colors := ("lightblue", "lightgreen", "blue", "green", "lightpink");
declare variable $xSpacer := 5;
declare variable $ySpacer := 20;

(: These are the different kinds of name types to look for :)


declare variable $allNames := $bojack//name/@type => distinct-values();

declare variable $nameTotal := $bojack//name/@type => count();


(:I want to find how many distinct strings come up matching to each name Type :)




<svg
    width="100%"
    height="100%"
    xmlns="http://www.w3.org/2000/svg">
    
    
    <g
        transform="translate(50, 20)">
        
        {
            for $n at $pos in $allNames
            let $countType := $bojack//Q{}name[@type=$n]/@type => count()
            
            let $namePerc := $countType div $nameTotal
            
            let $perc := $namePerc => format-number('01%')
           
          
            
            
    
(: This is going to have it travel to the bojack collection, look for every name attribute and 
cycle through $n type for the attribute. Then it will travel to the attribute and count what kind of 
attribute it is. :)


(: Look to output percentage type (Add everything up then divide it by how much it appears) :)


            return
                <g
                    id="{$n}">
                    
                    <line
                        x1='{0}'
                        y1='{$pos * $ySpacer}'
                        x2='{$xSpacer * $namePerc * 100}'
                        y2="{$pos * $ySpacer}"
                        stroke='{$colors[position() = $pos]}'
                        stroke-width='5'/>
                        
                      
                
                
                </g>
        }
    </g>

</svg>

