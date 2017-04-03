import draw
from os import getenv
import logging
import sys

app = draw.app
app.debug = False
port = int(getenv("PORT", 8080))

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)

if __name__ == "__main__":
    app.run(port=port, host='0.0.0.0')
