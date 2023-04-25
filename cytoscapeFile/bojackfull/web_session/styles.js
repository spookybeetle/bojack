var styles = [ {
  "format_version" : "1.0",
  "generated_by" : "cytoscape-3.9.1",
  "target_cytoscapejs_version" : "~2.1",
  "title" : "default",
  "style" : [ {
    "selector" : "node",
    "css" : {
      "font-size" : 12,
      "text-opacity" : 1.0,
      "border-color" : "rgb(204,204,204)",
      "text-valign" : "center",
      "text-halign" : "center",
      "border-opacity" : 1.0,
      "font-family" : "SansSerif.plain",
      "font-weight" : "normal",
      "height" : 35.0,
      "background-opacity" : 1.0,
      "border-width" : 0.0,
      "color" : "rgb(0,0,0)",
      "shape" : "roundrectangle",
      "background-color" : "rgb(137,208,245)",
      "width" : 35.0,
      "content" : "data(name)"
    }
  }, {
    "selector" : "node[Column_1 = 'Music:']",
    "css" : {
      "font-family" : "Arial Black",
      "font-weight" : "normal"
    }
  }, {
    "selector" : "node[Column_1 = 'Music:']",
    "css" : {
      "background-color" : "rgb(253,141,60)"
    }
  }, {
    "selector" : "node[BetweennessCentrality > 1]",
    "css" : {
      "font-size" : 1
    }
  }, {
    "selector" : "node[BetweennessCentrality = 1]",
    "css" : {
      "font-size" : 127
    }
  }, {
    "selector" : "node[BetweennessCentrality > 0][BetweennessCentrality < 1]",
    "css" : {
      "font-size" : "mapData(BetweennessCentrality,0,1,19,127)"
    }
  }, {
    "selector" : "node[BetweennessCentrality = 0]",
    "css" : {
      "font-size" : 19
    }
  }, {
    "selector" : "node[BetweennessCentrality < 0]",
    "css" : {
      "font-size" : 1
    }
  }, {
    "selector" : "node:selected",
    "css" : {
      "background-color" : "rgb(255,255,0)"
    }
  }, {
    "selector" : "edge",
    "css" : {
      "content" : "",
      "line-style" : "solid",
      "line-color" : "rgb(132,132,132)",
      "font-size" : 10,
      "width" : 2.0,
      "source-arrow-shape" : "none",
      "text-opacity" : 1.0,
      "target-arrow-color" : "rgb(0,0,0)",
      "target-arrow-shape" : "none",
      "opacity" : 1.0,
      "source-arrow-color" : "rgb(0,0,0)",
      "font-family" : "Dialog.plain",
      "font-weight" : "normal",
      "color" : "rgb(0,0,0)"
    }
  }, {
    "selector" : "edge[Column_4 > 12]",
    "css" : {
      "line-color" : "rgb(73,0,106)"
    }
  }, {
    "selector" : "edge[Column_4 = 12]",
    "css" : {
      "line-color" : "rgb(122,1,119)"
    }
  }, {
    "selector" : "edge[Column_4 > 7.41482997][Column_4 < 12]",
    "css" : {
      "line-color" : "mapData(Column_4,7.41482997,12,rgb(253,224,221),rgb(122,1,119))"
    }
  }, {
    "selector" : "edge[Column_4 > 1][Column_4 < 7.41482997]",
    "css" : {
      "line-color" : "mapData(Column_4,1,7.41482997,rgb(247,104,161),rgb(253,224,221))"
    }
  }, {
    "selector" : "edge[Column_4 = 1]",
    "css" : {
      "line-color" : "rgb(247,104,161)"
    }
  }, {
    "selector" : "edge[Column_4 < 1]",
    "css" : {
      "line-color" : "rgb(255,247,243)"
    }
  }, {
    "selector" : "edge[Column_4 > 12]",
    "css" : {
      "width" : 1.0
    }
  }, {
    "selector" : "edge[Column_4 = 12]",
    "css" : {
      "width" : 30.0
    }
  }, {
    "selector" : "edge[Column_4 > 1][Column_4 < 12]",
    "css" : {
      "width" : "mapData(Column_4,1,12,1.7073170731707317,30.0)"
    }
  }, {
    "selector" : "edge[Column_4 = 1]",
    "css" : {
      "width" : 1.7073170731707317
    }
  }, {
    "selector" : "edge[Column_4 < 1]",
    "css" : {
      "width" : 1.0
    }
  }, {
    "selector" : "edge:selected",
    "css" : {
      "line-color" : "rgb(255,0,0)"
    }
  } ]
} ]