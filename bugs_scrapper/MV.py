def get_MV(id):
    html_text = """
        <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <iframe
                id="ytplayer"
                type="text/html"
                width="720"
                height="405"
                src=f"https://www.youtube.com/embed/{id}"
                frameborder="0"
                allowfullscreen="allowfullscreen"></iframe>
        </body>
    </html>
    """

    html_file = open('MV/html_file.html', 'w')
    html_file.write(html_text)
    html_file.close()