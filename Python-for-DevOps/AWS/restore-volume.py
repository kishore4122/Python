import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2', region_name="eu-west-3")
ec2_resource = boto3.resource('ec2', region_name="eu-west-3")

'''
#describe_instances() function is used to get all instances from a region
reservations = ec2_client.describe_instances()
#print(reservations) This gives a dictionary
for reservation in reservations['Reservations']:
    #print(reservation) This gives a List of dictionary
    instances = reservation['Instances']
    for instance in instances:
        #print(instance) This gives a dictionary
        #print(instance['State']['Name'])
        print(f"Instance {instance['InstanceId']} is {instance['State']['Name']}")

we can use this logic to get the Instance ID of a particular region

But for now we are hard coding the Instance ID.
'''

instance_id = "i-04f01be7a765eaf7e"

volumes = ec2_client.describe_volumes(
    Filters = [
        {
            'Name': 'attachment.instance-id',
            'Values': [instance_id]
        },
    ]
)

instance_volume = volumes['Volumes'][0]
#print(instance_volume) This gives a list of dictionary

snapshots = ec2_client.describe_snapshots(
    OwnerIds = ['self'],
    Filters = [
        {
            'Name': 'volume-id',
            'Values': [instance_volume['VolumeId']]
        },
    ]
)

#print(snapshots) This gives a list

latest_snapshot = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)[0]

new_volume = ec2_client.create_volume(
    SnapshotID = latest_snapshot['SnapshotId'],
    AvailabilityZone = "eu-west-3b",
    TagSpecifications = [
        {
            'ResourceType': 'volume',
            "Tags": [
                {
                    'key': 'Name',
                    'Values': 'prod'
                }
            ]
        }
    ]
)

while True:
    vol = ec2_resource.Volume(new_volume['VolumeId'])
    print(vol.state)
    if vol.state == 'available':
        ec2_resource.Instance(instance_id).attach_volume(
            Device = '/dev/xvdb',
            VolumeId = new_volume['VolumeId'] 
        )
    break


