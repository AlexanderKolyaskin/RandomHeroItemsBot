from config.config_read import read_config
from app import Application


def import_config():
    return read_config()

def main():
    settings = import_config()
    app = Application(settings=settings)
    app.run()

if __name__ == '__main__':
    main()