# Use boto3 and Python to query a table, remove an item from a table, done-create a table, and delete a table.
import boto3

# initialize dynamodb table creation by defining a variable and giving it boto3.client value of (dynamodb)
dynamodb = boto3.resource('dynamodb')


# ------- CREATE TABLE-----

# table = dynamodb.create_table(
#     # define table name
#     TableName="users",
#     # define table keys
#     KeySchema=[
#      {
#       'AttributeName': 'username',
#       'KeyType': 'HASH' #partition key
#      },
#      {
#          'AttributeName':'last_name',
        #  'KeyType': 'RANGE' # sort key
#      }
#     ],
#     # define the keys above
#     AttributeDefinitions=[
#      {
#          'AttributeName': 'username',
#          'AttributeType': 'S'
#      }, 
#      {
#          'AttributeName': 'last_name',
#          'AttributeType': 'S'
#      }
#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 5,
#         'WriteCapacityUnits': 5
#     },
# )



# ------- Populate TABLE-------

# users_table = dynamodb.Table('users')
# use batch items to input multiple items at once
# with users_table.batch_writer() as batch: 
#     batch.put_item(Item = {'username': " The internet of money", 'last_name': 'Biographical' }),
#     batch.put_item(Item = {'username': " Harry Potter ", 'last_name': 'Fantasy' }),
#     batch.put_item(Item = {'username': " Gane of thrones", 'last_name': 'Fantasy' }),
#     batch.put_item(Item = {'username': " FightClud", 'last_name': 'Fiction' }),
#     batch.put_item(Item = {'username': " Basic Economics", 'last_name': 'Non-Fiction' }),
#     batch.put_item(Item = {'username': " Range", 'last_name': 'Self Help' }),
#     batch.put_item(Item = {'username': " Haunted ", 'last_name': 'Fiction' }),
#     batch.put_item(Item = {'username': " A clock work orange", 'last_name': 'Fiction' }),
#     batch.put_item(Item = {'username': " Thinking fast and slow", 'last_name': 'Psychologocal' })
    
# print(users_table)# print table name



# -----SCAN TABLE-----

# users_table = dynamodb.Table('users')

# # scan items in our users table
# items = users_table.scan()

# # Print items in our users table
# print(items['Items'])


# ------QUERY TABLE-----
# from boto3.dynamodb.conditions import Key, Attr

# users_table = dynamodb.Table('users')

# items = users_table.query(
# #the only acceptable arguements for KeyConditionExpression is the partition key
# #and it's value
# KeyConditionExpression= Key('username').eq(' Range')
# )

# print(items['Items'])



# ------DELETE TABLE------

# users_table = dynamodb.Table('users')
# users_table.delete()
