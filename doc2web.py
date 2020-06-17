import sys
index1=0
index2=0
globalLine="awesome"
count=1;

def topic(line):
    line=line.replace("topic:","")
    global globalLine
    globalLine=line
    global index1
    index1=0
    global index2
    index2=1

def code(line):
    line=line.replace("code:","")
    if "<" in line:
        line=line.replace("<","&lt;")
    if ">" in line:
        line=line.replace(">","&gt;")
    global globalLine
    globalLine=line
    global index1
    index1=2
    global index2
    index2=3

def description(line):
    line=line.replace("description:","")
    global globalLine
    globalLine=line
    global index1
    index1=4
    global index2
    index2=5

def image(line):
    line=line.replace("image:","")
    global globalLine
    globalLine=line
    global index1
    index1=6
    global index2
    index2=7

def subtopic(line):
    global count
    line=line.replace("subtopic:",str(count)+". ")
    count+=1
    global globalLine
    globalLine=line
    global index1
    index1=8
    global index2
    index2=9

def link(line):
    line=line.replace("link:","")
    global globalLine
    globalLine=line
    global index1
    index1=10
    global index2
    index2 =11



if len(sys.argv)<3 or len(sys.argv)>3:
    print("Invalid number of arguments: 1st argument=reading textfile 2nd argument: output html file")

else:
    print("Processing data")
    htmlList=["<h1>","</h1>","<code>","</code>","<p1>","</p1>","<img src=\"","\">","<h2>","</h2>","<a href=","</a>"]
    
    readfile=open(sys.argv[1],"r")
    outputfile=open(sys.argv[2],"w")
    structure= open("./utils/beginning.html","r")
    for line in structure:
        outputfile.write(line)
    structure.close()
    for line in readfile:
        if line=="\n":
            # print("empty line")
            continue
        else:
            first=line.split()[0]
        if "topic:"==first:
            outputfile.write("<div class=\"topic\">")
            topic(line)
        elif "code:"==first:
            outputfile.write("</div>")
            outputfile.write("</pre>")
            outputfile.write("<pre class=\"code\">")
            code(line)
        elif "description:"==first:
            outputfile.write("</div>")
            outputfile.write("</pre>")
            outputfile.write("<div class=\"description\">")
            description(line)
        elif "image:"==first:
            outputfile.write("</div>")
            outputfile.write("</pre>")
            outputfile.write("<div class=\"image\">")
            image(line)
        elif "subtopic:"==first:
            outputfile.write("</div>")
            outputfile.write("</pre>")
            outputfile.write("<div class=\"subtopic\">")
            subtopic(line)
        elif "link:"==first:
            outputfile.write("</div>")
            outputfile.write("</pre>")
            outputfile.write("<div class=\"link\">")
            link(line)
        else:
            globalLine=line
        outputfile.write(htmlList[index1]+globalLine+htmlList[index2])

    outputfile.write("</div>")
    outputfile.write("</pre>")
    structure =open("./utils/end.html","r")
    for line in structure:
        outputfile.write(line)
    structure.close()
    readfile.close()
    outputfile.close()
    print("Processing done Open your output html file in a browser or webserver ")

