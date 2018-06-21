import colors;

def main():

    html_header = "\
        <!DOCTYPE html> \
        <html> \
        <head> \
            <title>PyGame3 color reference</title> \
        </head> \
        <body>"

    html_end = "</body></html>"

    html = "<table style='width:100%'>"
    html += "<tr style='text-align:left'><th>Name</th><th>CSS</th><th>RGB</th><th>Color</th></tr>"

    for k,v in colors.THECOLORS.items():
        value_hex = "#%02x%02x%02x" % (v[0], v[1], v[2])
        html += "<tr>"
        html += "<td>" + k + "</td>"
        html += "<td>" + value_hex + "</td>"
        html += "<td>" + str(v) + "</td>"
        html += "<td style='background:" + value_hex + "'></td>"
        html += "</tr>"

    html += "</table>"

    file = open("./index.html", "w")
    file.write(html_header)
    file.write(html)
    file.write(html_end)

if __name__== "__main__":
  main()