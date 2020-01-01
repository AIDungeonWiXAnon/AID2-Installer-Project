import configparser
import logging

config = configparser.ConfigParser()
config.read("config.ini")
settings = config["Settings"]
colors = config["Colors"]

logger = logging.getLogger(__name__)
logLevel = settings.getint("log-level")
oneLevelUp = 20

# I don't know if this will work before loading the transformers module?
# silence transformers outputs when loading model
logging.getLogger("transformers.tokenization_utils").setLevel(logLevel + oneLevelUp)
logging.getLogger("transformers.modeling_utils").setLevel(logLevel + oneLevelUp)
logging.getLogger("transformers.configuration_utils").setLevel(logLevel + oneLevelUp)

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logLevel + oneLevelUp,
)
logger.setLevel(logLevel)
