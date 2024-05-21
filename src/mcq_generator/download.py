import pdfkit
from io import BytesIO

def download_pdf(df, filename):
    # Convert DataFrame to HTML table
    html_table = df.to_html(index=False)

    options={'encoding' : 'UTF-8'}

    # Generate PDF from HTML
    pdf = pdfkit.from_string(html_table, False, options=options)

    # Convert PDF bytes to BytesIO object
    buffer = BytesIO(pdf)
    buffer.seek(0)
    return buffer


