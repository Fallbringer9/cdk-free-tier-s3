from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_s3 as s3,
)
from constructs import Construct

class CdkFreeTierS3Stack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Bucket S3 "propre" et free-tier friendly
        bucket = s3.Bucket(
            self,
            "AppBucket",
            versioned=True,                                  # Versioning ON
            encryption=s3.BucketEncryption.S3_MANAGED,       # SSE-S3 (AES-256)
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,  # Bloque tout accès public
            enforce_ssl=True,                                # Requiert HTTPS (ajoute une bucket policy deny si pas SSL)
            object_ownership=s3.ObjectOwnership.BUCKET_OWNER_ENFORCED,  # évite les ACL
            removal_policy=RemovalPolicy.RETAIN,             # Sécurité : ne pas supprimer les données par accident
            auto_delete_objects=False                        # Pas de suppression auto des objets (sécurité)


        )
