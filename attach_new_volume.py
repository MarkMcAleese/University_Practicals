import boto3

# AWS credentials and region
aws_access_key = 'YOUR_ACCESS_KEY'
aws_secret_key = 'YOUR_SECRET_KEY'
aws_region = 'us-east-1'  # Change this to your preferred region

# EC2 instance settings
instance_type = 't2.micro'
ami_id = 'YOUR_AMI_ID'  # Replace with the desired AMI ID
key_name = 'YOUR_KEY_PAIR_NAME'  # Replace with your key pair name

# EBS volume settings
volume_size = 10  # Size of the EBS volume in GB
availability_zone = f'{aws_region}a'

# Initialize the Boto3 EC2 client
ec2 = boto3.client('ec2', region_name=aws_region, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

# Create an EBS volume
volume = ec2.create_volume(
    Size=volume_size,
    AvailabilityZone=availability_zone,
)

# Create an EC2 instance
instances = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_name,
    MinCount=1,
    MaxCount=1,
)

instance_id = instances['Instances'][0]['InstanceId']

# Wait for the EC2 instance to be running
ec2.get_waiter('instance_running').wait(InstanceIds=[instance_id])

# Attach the EBS volume to the EC2 instance
ec2.attach_volume(
    Device='/dev/sdf',  # Change the device name as needed
    InstanceId=instance_id,
    VolumeId=volume['VolumeId'],
)