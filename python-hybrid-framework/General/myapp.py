import logging
import mylib


def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO, encoding='utf-8', filemode='w')
    logging.info('Started1')
    mylib.do_something()
    logging.info('Finished')


if __name__ == '__main__':
    main()
