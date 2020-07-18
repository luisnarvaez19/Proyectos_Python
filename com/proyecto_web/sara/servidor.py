import csv
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

#HOST_ADDRESS = "212.128.254.65"
HOST_ADDRESS = "127.0.0.1"
HOST_PORT = 20022

class ServidorCovid19(BaseHTTPRequestHandler):
    def set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

    def do_GET(self):
        self.set_response()
        if (self.path == "/index.html" or self.path == "/index.htm" or self.path == "/"):
            msg = '''
                <!DOCTYPE html>
                    <head>
                        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
                    </head>
                    <body>
                        <div id="forma_19" style="margin-left: 300px;margin-top: 50px;">
                            <h1>Bienvenido a la p&aacute;gina del Covid 19&nbsp;</h1>
                            <form action="respuestaconsulta" enctype="text/plain" id="covid19" method="get" name="covid19">
                                <h2>Formulario de Consulta del Covid 19</h2>
                                <p>Country:&nbsp; &nbsp;&nbsp;
                                    <input maxlength="30" name="country" size="20" type="text" />
                                </p>
                                <p>Fecha:&nbsp; &nbsp; &nbsp; &nbsp;
                                    <input maxlength="10" name="fecha" size="12" type="text" />&nbsp; (mm-dd-yyyy)
                                </p>
                                <p>&nbsp;</p>
                                <p>
                                    <input name="consulta" type="submit" value="Consulta" />
                                </p>
                            </form>
                        </div> 
                        <p>&nbsp;</p>
                    </body>
                </html>
            '''
        elif (self.path == "/autor"):
            msg = '''<html>
                          <head>
                             <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
                          </head>
                          <body>
                                <hr />
                                    <h2 style="text-align: center;">Autor:&nbsp; &nbsp; Sara Altuna</h2>
                                    <h2 style="text-align: center;">Gitlab:&nbsp; s.altuna.2019</h2>
                                <hr />
                                <p>&nbsp;</p>
                          </body>
                        </html>'''
        # more info about URL encoding at https://www.w3schools.com/tags/ref_urlencode.ASP
        else:
            inicial=self.path
            parsed = urlparse(inicial)
            url = parsed._replace(query=None).geturl()
            if url == '/respuestaconsulta':
                index1 = inicial.find('country');
                index2 = inicial.find('fecha');
                if index1 != -1 and index2 != -1:
                    path = inicial.rsplit("?")
                    params = path[1].rsplit("&")
                    country = params[0].rsplit("=")[1]
                    fecha = params[1].rsplit("=")[1]

                    if int(fecha[0:2]) < 13:
                        csv_path = '/home/luis/Proyectos/Cursos/Curso Python/Codigo/com/proyecto_web/sara/'+fecha+'.csv'
                        header = '''<html>
                                  <head>
                                     <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
                                  </head>
                                  <body>
                                    <table>\n '''
                        tabla = ''
                        espacios = '&nbsp;'
                        try:
                            with open(csv_path, encoding="utf8") as csvFile:
                                reader = csv.DictReader(csvFile, delimiter=',')
                                #  Titulos de la tabla (Encabezado)
                                tabla = '<tr>{}</tr>'.format(
                                    ''.join(['<th>{}</th>'.format(header) for header in reader.fieldnames]))
                                tabla += '\n'
                                imprime_error = True
                                country = country.strip('+')
                                for row in reader:
                                    if row['Country_Region'].find(country) != -1:
                                        imprime_error = False
                                        table_row = '<tr>'
                                        contador = 0
                                        for fn in reader.fieldnames:
                                            table_row += '<td>{}</td>\n'.format(row[fn])
                                        table_row += '</tr>\n'
                                        tabla += table_row
                                if imprime_error :
                                    msg = '''<html>
                                                 <head>
                                                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
                                                     <meta http-equiv=”Content-Type” content=”text/html; charset=UTF-8″ />
                                                 </head>
                                                 <body>
                                                       <hr />
                                                           <h2 style="text-align: center;">No existe ninguna región con ese nombre.</h2>
                                                       <hr />
                                                       <p>&nbsp;</p>
                                                 </body>
                                               </html>'''
                                else:
                                    footer = '''
                                                    </table>
                                                </body>
                                        </html>'''
                                    pagina = header + tabla + footer
                                    msg = pagina
                        except IOError:
                            msg = '''<html>
                                         <head>
                                            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
                                         </head>
                                         <body>
                                               <hr />
                                                   <h2 style="text-align: center;">No se disponen datos de la fecha {}</h2>
                                               <hr />
                                               <p>&nbsp;</p>
                                         </body>
                                     </html>'''.format(fecha[3:5]+'-'+fecha[0:2]+'-'+fecha[6:])
                    else:
                        msg = '''<html>
                                                      <head>
                                                         <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
                                                      </head>
                                                      <body>
                                                            <hr />
                                                                <h2 style="text-align: center;">La fecha introducida es err&oacute;nea.</h2>
                                                            <hr />
                                                            <p>&nbsp;</p>
                                                      </body>
                                                    </html>'''
                else:
                    msg = '''<html>
                                                  <head>
                                                     <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
                                                  </head>
                                                  <body>
                                                        <hr />
                                                            <h2 style="text-align: center;">La consulta no tiene los datos bien formados</h2>
                                                        <hr />
                                                        <p>&nbsp;</p>
                                                  </body>
                                                </html>'''
            else:
                msg = '''<html>
                          <head>
                             <meta http-equiv=”Content-Type” content=”text/html; charset=UTF-8″ />v
                             <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
                          </head>
                          <body>
                                <hr />
                                    <h2 style="text-align: center;">Página no encontrada.</h2>
                                <hr />
                                <p>&nbsp;</p>
                          </body>
                        </html>'''

        self.wfile.write(msg.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        print(post_data)
        post_data = self.rfile.read(content_length).decode('utf-8') # <--- Gets the data itself
        self.set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
        self.wfile.write("POST request for {}, data is {}".format(self.path, post_data).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
# follows example shown on docs.cursoLN.org
    server_address = (HOST_ADDRESS, HOST_PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    run(handler_class=ServidorCovid19)
