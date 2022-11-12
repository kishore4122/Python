import boto3

client = boto3.client('eks', region_name="eu-west3")

clusters = client.list_clusters()['clusters']
#print(clusters) This gives a dictionary
#print(clusters['clusters']) This gives a list

for cluster in clusters:
    response = client.describe_cluster(
        name = cluster
    )
    #print(responce) This gives a dictionary
    cluster_status = response['cluster']['status']
    cluster_endpoint = response['cluster']['endpoint']
    cluster_version = response['cluster']['version']
    print(f"Cluster {cluster} status is {cluster_status}")
    print(f"Cluster endpoint is {cluster_endpoint}")
    print(f"Cluster version is {cluster_version}")