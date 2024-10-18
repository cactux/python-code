# https://github.com/DocstringFr/la-formation-complete-python/tree/master/chp-006_le-logging
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="app.log",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("msg debug")
logging.info("msg info")
logging.warning("msg warn")
logging.error("msg err")
logging.critical("msg crit")

