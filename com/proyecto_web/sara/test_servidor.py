import threading
import time
import unittest
from http.server import HTTPServer

import requests
from servidor import ServidorCovid19

#TestCase.maxDiff=None

IP = "127.0.0.1"
PORT = 12345
class TestRequests(unittest.TestCase):

    # Se comprueba la pagina principal
    def test_request01(self):
        # start our server
        server = HTTPServer((IP, PORT), ServidorCovid19)
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.start()
        # Wait a bit for the server to come up
        time.sleep(1)
        try:
             response = requests.get("http://localhost:12345/")
             html = response.text
             self.assertEqual(html, '''
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
            ''')
        finally:
             # and shutdown the server
             server.shutdown()
             server.server_close()

    # Se comprueba la pagina principal
    def test_request02(self):
        # start our server
        server = HTTPServer((IP, PORT), ServidorCovid19)
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.start()
        # Wait a bit for the server to come up
        time.sleep(1)
        try:
            response = requests.get("http://localhost:12345/index.html")
            html = response.text
            self.assertEqual(html, '''
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
            ''')
        finally:
            # and shutdown the server
            server.shutdown()
            server.server_close()

    def test_request03(self):
        # start our server
        server = HTTPServer((IP, PORT), ServidorCovid19)
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.start()
        # Wait a bit for the server to come up
        time.sleep(1)
        try:
            response = requests.get("http://localhost:12345/index.htm")
            html = response.text
            self.assertEqual(html, '''
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
            ''')
        finally:
            # and shutdown the server
            server.shutdown()
            server.server_close()

    # Se comprueba la pagina autor
    def test_request04(self):
        # start our server
        server = HTTPServer((IP, PORT), ServidorCovid19)
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.start()
        # Wait a bit for the server to come up
        time.sleep(1)
        try:
             response = requests.get("http://localhost:12345/autor")
             html = response.text
             self.assertEqual(html, '''<html>
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
                        </html>''')
        finally:
             # and shutdown the server
             server.shutdown()
             server.server_close()

    # Se comprueba que no este el parametro country
    def test_request05(self):
        # start our server
        server = HTTPServer((IP, PORT), ServidorCovid19)
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.start()
        # Wait a bit for the server to come up
        time.sleep(1)
        try:
             response = requests.get("http://localhost:12345/respuestaconsulta?fecha='03-23-2020'")
             html = response.text
             self.assertEqual(html, '''<html>
                                                  <head>
                                                     <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
                                                  </head>
                                                  <body>
                                                        <hr />
                                                            <h2 style="text-align: center;">La consulta no tiene los datos bien formados</h2>
                                                        <hr />
                                                        <p>&nbsp;</p>
                                                  </body>
                                                </html>''')
        finally:
             # and shutdown the server
             server.shutdown()
             server.server_close()

    # Se comprueba que no este el parametro fecha
    def test_request06(self):
        # start our server
        server = HTTPServer((IP, PORT), ServidorCovid19)
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.start()
        # Wait a bit for the server to come up
        time.sleep(1)
        try:
             response = requests.get("http://localhost:12345/respuestaconsulta?country=''")
             html = response.text
             self.assertEqual(html, '''<html>
                                                  <head>
                                                     <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
                                                  </head>
                                                  <body>
                                                        <hr />
                                                            <h2 style="text-align: center;">La consulta no tiene los datos bien formados</h2>
                                                        <hr />
                                                        <p>&nbsp;</p>
                                                  </body>
                                                </html>''')
        finally:
             # and shutdown the server
             server.shutdown()
             server.server_close()

    # Se comprueba que no existe el pais introducido en el parametro country
    def test_request07(self):
        # start our server
        server = HTTPServer((IP, PORT), ServidorCovid19)
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.start()
        # Wait a bit for the server to come up
        time.sleep(1)
        try:
            response = requests.get("http://localhost:12345/respuestaconsulta?country=wweew&fecha=03-23-2020")
            html = response.text
            self.assertEqual(html, '''<html>
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
                                               </html>''')
        finally:
            # and shutdown the server
            server.shutdown()
            server.server_close()

    # Se comprueba que no existe el archivo de una fecha dada
    def test_request08(self):
        # start our server
        server = HTTPServer((IP, PORT), ServidorCovid19)
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.start()
        # Wait a bit for the server to come up
        time.sleep(1)
        try:
            response = requests.get("http://localhost:12345/respuestaconsulta?country=ain&fecha=02-23-2020")
            html = response.text
            self.assertEqual(html, '''<html>
                                         <head>
                                            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
                                         </head>
                                         <body>
                                               <hr />
                                                   <h2 style="text-align: center;">No se disponen datos de la fecha 23-02-2020</h2>
                                               <hr />
                                               <p>&nbsp;</p>
                                         </body>
                                     </html>''')
        finally:
            # and shutdown the server
            server.shutdown()
            server.server_close()

    # Se comprueba que la fecha introducida es erronea
    def test_request09(self):
        # start our server
        server = HTTPServer((IP, PORT), ServidorCovid19)
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.start()
        # Wait a bit for the server to come up
        time.sleep(1)
        try:
            response = requests.get("http://localhost:12345/respuestaconsulta?country=ain&fecha=22-03-2020")
            html = response.text
            self.assertEqual(html, '''<html>
                                                      <head>
                                                         <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
                                                      </head>
                                                      <body>
                                                            <hr />
                                                                <h2 style="text-align: center;">La fecha introducida es err&oacute;nea.</h2>
                                                            <hr />
                                                            <p>&nbsp;</p>
                                                      </body>
                                                    </html>''')
        finally:
            # and shutdown the server
            server.shutdown()
            server.server_close()


if __name__ == "__main__":
        unittest.main()
