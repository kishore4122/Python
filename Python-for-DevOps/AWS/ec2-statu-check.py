import boto3

ec2_client = boto3.client('ec2', region_name="eu-central-1")
ec2_resource = boto3.resource('ec2', region_name="eu-central-1")

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


statuses = ec2_client.describe_instance_status(
    IncludeAllInstances = True
)
#print(statuses) This gives a dictionary
for status in statuses['InstanceStatuses']:
    #print(status) This gives a dictionary
    ins_status = status['InstanceStatus']['Status']
    sys_status = status['SystemcStatus']['Status']
    print(f"Instance {status['InstanceID']} status is {ins_status} and Systemc status is {sys_status}")

