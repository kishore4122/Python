import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="eu-west-3")


def create_volume_snapshot():
    volumes = ec2_client.describe_volume()
    # print(volumes) This gives a dictionary
    # print(volumes['Volumes']) This gives a list

    for volume in volumes['Volumes']:
        new_snapshot = ec2_client.create_snapshot(
            VolumeId=volume['VolumeId']
        )
        print(new_snapshot)



schedule.every().day().do(create_volume_snapshot)

while True:
    schedule.run_pending()