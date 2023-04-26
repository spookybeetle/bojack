declare variable $bojack := collection("../xmlFile/outputXML/?select=*.xml");

declare variable $colors := ("lightsalmon", "mediumorchid", "darkseagreen", "tomato", "palevioletred");
declare variable $xSpacer := 5;
declare variable $ySpacer := 35;

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
                        stroke-width='20'/>
                        
                  <text x="150" y="220" fill="wblack">Name Type Percentiles</text>
                  
                 <line x1="0" y1="200" x2="500" y2="200" style="stroke:rgb(0,0,0);stroke-width:2" />
        <line x1="0" y1="0" x2="0" y2="200" style="stroke:rgb(0,0,0);stroke-width:2" />
                <text x="-45" y="40" fill="black">Person</text>
                <text x="-35" y="75" fill="black">GPE</text>
                <text x="-35" y="110" fill="black">ORG</text>
                <text x="-45" y="145" fill="black">NORP</text>
                <text x="-35" y="180" fill="black">LOC</text>
                
                <text x="420" y="40" fill="black">82.2%</text>
                <text x="48" y="75" fill="black">7.9%</text>
                <text x="47" y="110" fill="black">7.7%</text>
                <text x="16" y="145" fill="black">1.4%</text>
                <text x="13" y="180" fill="black">0.82%</text>
                </g>
        }
    </g>

</svg>

