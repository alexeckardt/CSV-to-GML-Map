# CSV to GML Map.
 
Running the python script, (in the directory of an accompaning 3 column soulflamelang.csv), will return a gml script that creates a map with the data of the csv.

Column one of the csv is the map's key.
Column two is the generic text.
Column three is any additional info. Any info will be split up by commas are stored as an array.

For example, the line in the example csv:

    c.cutscene_name.example,generic text,"c,s,v"
   
Can be written as the GML line:

    lang[? "c.cutscene_name.example"]       = [["generic text", "c", "s", "v", ]];
    
    
The script will combine similar keys into an arrays of arrays (GML allows for multi variable array sizes),
 
    c.cutscene_name.example,generic text,"c,s,v"
    c.cutscene_name.example,generic text 2,"c,s,v, a"
    
    ...
    
    lang[? "c.cutscene_name.example"]       = [["generic text", "c", "s", "v", ], ["generic text 2", "c", "s", "v", " a", ]];

And Single Reference Text (where no info is given)

    c.cutscene_name.example,generic text,
    
    ...
    
    lang[? "c.cutscene_name.example"] = "generic text"
    
