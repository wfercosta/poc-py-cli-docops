"""
Usage:
    apoio configure [--database-host=<host> --database-port=<port> --database-pwd=<password> ]
    apoio generate-data (--output=<path> --laboratories=<laboratories>) [--amount-files=<amount> --amount-patients=<patients> --amount-doctors=<doctors> --amount-orders=<orders> --amount-exams=<exams> --amount-samples=<samples> --percent-exams-curve=<percent-curve> --percent-exams-standard=<percent-standard>]
    apoio generate-user (--output=<path> --clone-laboratories=<laboratories>)

Options:

    --database-host=<host>                                  The database hostname [default: localhost].
    --database-port=<port>                                  The database port [default: 1433].
    --database-pwd=<password>                               The database password [default: apoiob2b].
    --amount-files=<amount>                                 The amount of files to be generated [default: 1].
    --amount-patients=<patients>                            The amount of patient to be generated [default: 12].
    --amount-doctors=<doctors>                              The amount of doctors to be generated [default: 12].
    --amount-orders=<orders>                                The amount of orders to be generated [default: 12].
    --amount-exams=<exams>                                  The amount of exams to be generated [default: 7].
    --amount-samples=<samples>                              The amount of samples to be generated [default: 3].
    --percent-exams-curve=<percent-curve>                   The percentage distribution of exams type curve [default: 5].
    --percent-exams-standard=<percent-standard>             The percentage distribution of exams type standard [default: 96].
    --percent-exams-additional=<percent-additional>         The percentage distribution of exams type additional [default: 0].
"""
import imp
from docopt import docopt
import generate_data


def dispatch(arguments):

    filtered = {k: v for k, v in arguments.iteritems() if v is True and not k.startswith('--')}

    print(filtered)

    # imp.find_module('generate_data')

    # for arg in arguments:
    #     print arg



if __name__ == '__main__':
    dispatch(docopt(__doc__))