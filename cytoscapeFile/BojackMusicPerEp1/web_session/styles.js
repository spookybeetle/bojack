var styles = [ {
  "format_version" : "1.0",
  "generated_by" : "cytoscape-3.9.1",
  "target_cytoscapejs_version" : "~2.1",
  "title" : "default",
  "style" : [ {
    "selector" : "node",
    "css" : {
      "shape" : "roundrectangle",
      "border-width" : 0.0,
      "text-opacity" : 1.0,
      "font-size" : 12,
      "color" : "rgb(0,0,0)",
      "background-opacity" : 1.0,
      "border-opacity" : 1.0,
      "text-valign" : "center",
      "text-halign" : "center",
      "width" : 75.0,
      "height" : 35.0,
      "font-family" : "Comic Sans MS Bold",
      "font-weight" : "normal",
      "background-color" : "rgb(199,233,192)",
      "border-color" : "rgb(204,204,204)",
      "content" : "data(name)"
    }
  }, {
    "selector" : "node[Degree > 50]",
    "css" : {
      "font-size" : 1
    }
  }, {
    "selector" : "node[Degree = 50]",
    "css" : {
      "font-size" : 47
    }
  }, {
    "selector" : "node[Degree > 1][Degree < 50]",
    "css" : {
      "font-size" : "mapData(Degree,1,50,10,47)"
    }
  }, {
    "selector" : "node[Degree = 1]",
    "css" : {
      "font-size" : 10
    }
  }, {
    "selector" : "node[Degree < 1]",
    "css" : {
      "font-size" : 1
    }
  }, {
    "selector" : "node[Degree > 50]",
    "css" : {
      "color" : "rgb(68,1,84)"
    }
  }, {
    "selector" : "node[Degree = 50]",
    "css" : {
      "color" : "rgb(37,37,37)"
    }
  }, {
    "selector" : "node[Degree > 27.20930314][Degree < 50]",
    "css" : {
      "color" : "mapData(Degree,27.20930314,50,rgb(153,112,171),rgb(37,37,37))"
    }
  }, {
    "selector" : "node[Degree > 1][Degree < 27.20930314]",
    "css" : {
      "color" : "mapData(Degree,1,27.20930314,rgb(174,95,203),rgb(153,112,171))"
    }
  }, {
    "selector" : "node[Degree = 1]",
    "css" : {
      "color" : "rgb(174,95,203)"
    }
  }, {
    "selector" : "node[Degree < 1]",
    "css" : {
      "color" : "rgb(253,231,37)"
    }
  }, {
    "selector" : "node[Column_1 = 'Music:']",
    "css" : {
      "background-color" : "rgb(158,188,218)"
    }
  }, {
    "selector" : "node:selected",
    "css" : {
      "background-color" : "rgb(255,255,0)"
    }
  }, {
    "selector" : "edge",
    "css" : {
      "width" : 2.0,
      "line-style" : "solid",
      "content" : "",
      "target-arrow-shape" : "none",
      "text-opacity" : 1.0,
      "font-size" : 10,
      "color" : "rgb(0,0,0)",
      "opacity" : 1.0,
      "target-arrow-color" : "rgb(0,0,0)",
      "source-arrow-shape" : "none",
      "source-arrow-color" : "rgb(0,0,0)",
      "font-family" : "Dialog.plain",
      "font-weight" : "normal",
      "line-color" : "rgb(132,132,132)"
    }
  }, {
    "selector" : "edge[Column_4 > 2]",
    "css" : {
      "width" : 1.0
    }
  }, {
    "selector" : "edge[Column_4 = 2]",
    "css" : {
      "width" : 22.4390243902439
    }
  }, {
    "selector" : "edge[Column_4 > 1][Column_4 < 2]",
    "css" : {
      "width" : "mapData(Column_4,1,2,1.4634146341463414,22.4390243902439)"
    }
  }, {
    "selector" : "edge[Column_4 = 1]",
    "css" : {
      "width" : 1.4634146341463414
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