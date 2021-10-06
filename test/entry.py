from flask import make_response

def get_document():
    with open('pdf.pdf', 'rb') as f:
        file = f.read()
    r = make_response(file, 200)
    r.headers.set('Content-Type', 'application/pdf')
    r.headers.set('Content-Disposition', 'attachment', filename=f'test.pdf')
    return r
    