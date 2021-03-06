import boto3
from typing import Dict


class Route53Helper:
    def __init__(self, region: str, credentials: Dict[str, str]) -> None:
        self.client = boto3.client(
            'route53',
            aws_access_key_id=credentials['public_key'],
            aws_secret_access_key=credentials['secret_key'],
            region_name=region
        )

    def update_dns_with_ip(self, hosted_zone_id: str, dns: str, ip: str) -> None:
        print("Updating A in hosted zone {}: {} -> {}".format(hosted_zone_id, dns, ip))
        self.client.change_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            ChangeBatch={
                'Changes': [
                    {
                        'Action': 'UPSERT',
                        'ResourceRecordSet': {
                            'Name': dns,
                            'Type': 'A',
                            'TTL': 60,
                            'ResourceRecords': [
                                {'Value': ip},
                            ],
                        }
                    },
                ]
            }
        )
