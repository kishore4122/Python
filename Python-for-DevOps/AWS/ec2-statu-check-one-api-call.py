import boto3

ec2_client = boto3.client('ec2', region_name="eu-central-1")
ec2_resource = boto3.resource('ec2', region_name="eu-central-1")

#describe_instance_status() function is used to get status of all instances from a region
statuses = ec2_client.describe_instance_status(
    IncludeAllInstances = True
)
#print(statuses) This gives a dictionary
for status in statuses['InstanceStatuses']:
    #print(status) This gives a dictionary
    ins_status = status['InstanceStatus']['Status']
    sys_status = status['SystemcStatus']['Status']
    state = status['InsatanceState']['Name']
    print(f"Instance {status['InstanceID']} is {state} with instance status {ins_status} and Systemc status is {sys_status}")

