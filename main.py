from src.core.engine import RPCengine
import time

CONFIG = "settings.json"

if __name__ == "__main__":
    engine = RPCengine(config_path=CONFIG)
    engine.run()