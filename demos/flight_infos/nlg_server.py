#!/usr/bin/env python3
# adapted from https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7
# - to parse and return json
# - to connect to the pyrealb realizer in query_flight_db
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging, json

# specific to flight_infos demo
import realize_example
import query_flight_db
from Entities import Entities, Entity

logRequestParameters = False


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):  # this is not called by RASA
        if logRequestParameters:
            logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length).decode('utf-8')  # <--- Gets the data itself
        if logRequestParameters:
            logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                         str(self.path), str(self.headers), post_data)
        fields = json.loads(post_data)
        response = fields["response"]
        message = fields["tracker"]["latest_message"]
        intent = message["intent"]["name"]
        entities = message.get("entities", [])  # fields: entity, value
        text = message.get("text")
        # log input received and paraphrase
        logging.info("** Response:%s Intent:%s Text:%s\n%s",
                     response, intent, text, "\n - ".join(str(Entity(e)) for e in entities))
        logging.info("pyrealb:%s", realize_example.realize_example(intent, Entities(entities)))
        # answer using pyrealb
        self._set_response()
        response_text = query_flight_db.process_intent(intent, entities)
        # there seems to be an undocumented limit on the length of the response accepted by RASA from an NLG server
        # around 1K but we use slightly less to take into account the transformation into JSON
        limit = 900
        if len(response_text) > limit:
            last_nl_idx = response.rfind("\n")  # skip to previous NL
            response_text = response_text[:(last_nl_idx if last_nl_idx > 0 else limit)] + "\n..."
        response_json = json.dumps({"text": response_text}).encode("utf-8")
        logging.info("response lengths: text:%d json:%d" % (len(response_text), len(response_json)))
        self.wfile.write(response_json)


def run(server_class=HTTPServer, handler_class=S, port=8081):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd... on port %d\n' % port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
