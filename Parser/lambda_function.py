from tests import test_parser

def lambda_handler(event, context):
    test_parser.t_parser()
    print("Completed")