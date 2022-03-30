import boto3
from retrying import retry

org = boto3.client('organizations', region_name='us-east-1')


@retry
def close_account(account_to_close):

    print("Closing Account {}".format(account_to_close))

    org.close_account(AccountId=account_to_close['Id'])

    print("Closed Account {}".format(account_to_close))


accounts = org.list_accounts()['Accounts']
for account in accounts:
    if account['JoinedMethod'] != 'CREATED' or account['Status'] != 'ACTIVE':
        continue
    close_account(account)
