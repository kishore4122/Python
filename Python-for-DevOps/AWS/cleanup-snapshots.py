import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2', region_name="eu-west-3")

# describe_snapshots() function gives all snapshots which was created by ourself and store it in a variable 
snapshots = ec2_client.describe_snapshots(
        OwnerIds = ['self',]
    )
# print (snapshots) This gives a dictionary
# print(snapshots['Snapshots]) This gives a List of dictionary which are unsorted


# sorted() function is used to sort the snapshots based on the 'StartTime' key
sorted_by_date = sorted(snapshots['Snapshots'], key=itemgetter('StartTime', reverse=True))

'''
# print all the unsorted snapshots
for snap in snapshots['Snapshots']:
    print(snap['StartTime'])

print("###########")

# print all the sorted snapshots
for snap in sorted_by_date:
    print(snap['StartTime'])

'''

for snap in sorted_by_date[2:]:
    response = ec2_client.delete_snapshot(
        SnapshotId = snap['SnapshotId']
    )
    print(response)




